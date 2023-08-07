import os
from concurrent.futures import Future
from datetime import date, datetime, timedelta, time
from functools import partial
from textwrap import dedent
from threading import Lock
from typing import List, Dict, Tuple, Optional

import requests
from loguru import logger
from requests_futures.sessions import FuturesSession

from fime.config import Config
from fime.exceptions import FimeException
from fime.util import Status


class WorklogRest:
    def __init__(self, config: Config):
        self.config = config
        self.user_url = os.path.join(config.jira_url, "rest/api/2/myself")
        self.issue_url = os.path.join(config.jira_url, "rest/api/2/issue/{}")
        self.worklog_url = os.path.join(config.jira_url, "rest/api/2/issue/{}/worklog")
        self.worklog_update_url = os.path.join(config.jira_url, "rest/api/2/issue/{issue_key}/worklog/{worklog_id}")
        self.session = FuturesSession()
        self._user = None
        self._user_future = self._req_user()
        self._issue_state: Dict[str, Tuple[Status, str]] = dict()
        self._issue_previous_comments: Dict[str, str] = dict()
        self._issue_worklog_id: Dict[str, str] = dict()
        self._issues_lock = Lock()

    def _req_user(self):
        future = self.session.get(
            self.user_url,
            headers={
                "Authorization": f"Bearer {self.config.jira_token}",
                "Accept": "application/json",
            },
        )
        future.add_done_callback(self._resp_user)
        return future

    @logger.catch(message="Could not get user key")
    def _resp_user(self, future):
        self._user = future.result().json()["key"]

    def get_issues_state(self, issue_keys: List[str], pdate: date) -> List[Tuple[Status, str, Optional[str]]]:
        ret = []
        with self._issues_lock:
            for issue_key in issue_keys:
                if issue_key not in self._issue_state:
                    self._issue_state[issue_key] = (Status.PROGRESS, "Working")
                    self._req_issue(issue_key, pdate)
                if issue_key in self._issue_previous_comments:
                    prev_comment = self._issue_previous_comments[issue_key]
                else:
                    prev_comment = None
                ret.append((*self._issue_state[issue_key], prev_comment))
        return ret

    def _req_issue(self, issue_key: str, pdate: date):
        future = self.session.get(
            self.issue_url.format(issue_key),
            headers={
                "Authorization": f"Bearer {self.config.jira_token}",
                "Accept": "application/json",
            },
        )
        future.add_done_callback(partial(self._resp_issue, issue_key, pdate))

    def _resp_issue(self, issue_key: str, pdate: date, future: Future):
        resp: requests.Response = future.result()
        with self._issues_lock:
            if resp.status_code == 200:
                issue_title = f'{issue_key} {resp.json()["fields"]["summary"]}'
                self._req_worklog_check(issue_key, issue_title, pdate)
            else:
                self._issue_state[issue_key] = (Status.ERROR, "Could not find specified issue")

    def _req_worklog_check(self, issue_key: str, issue_title: str, pdate: date):
        future = self.session.get(
            self.worklog_url.format(issue_key),
            headers={
                "Authorization": f"Bearer {self.config.jira_token}",
                "Accept": "application/json",
            },
        )
        future.add_done_callback(partial(self._resp_worklog_check, issue_key, issue_title, pdate))

    def _resp_worklog_check(self, issue_key: str, issue_title: str, pdate: date, future: Future):
        resp = future.result()
        worklogs = resp.json()["worklogs"]
        worklogs = sorted(
            worklogs, key=lambda x: datetime.strptime(x["started"], "%Y-%m-%dT%H:%M:%S.%f%z"), reverse=True)
        self._user_future.result()
        if not self._user:
            with self._issues_lock:
                self._issue_state[issue_key] = (Status.OK, issue_title)
            return
        worklog_found = False
        with self._issues_lock:
            for log in worklogs:
                if log["author"]["key"] == self._user:
                    if datetime.strptime(log["started"], "%Y-%m-%dT%H:%M:%S.%f%z").date() == pdate:
                        self._issue_worklog_id[issue_key] = log["id"]
                        worklog_found = True
                    else:
                        self._issue_previous_comments[issue_key] = log["comment"].strip()
                        worklog_found = True
                    break
            if worklog_found:
                logger.debug(f"Found existing worklog for issue {issue_key}")
            else:
                logger.debug(f"Did not find existing worklog for issue {issue_key}")
            self._issue_state[issue_key] = (Status.OK, issue_title)

    def _upload_sanity_check(self, issue_keys: List[str]):
        if not self._user:
            raise FimeException("Could not get user key")
        # lock is held by caller
        for issue_key in issue_keys:
            if issue_key not in self._issue_state or self._issue_state[issue_key][0] is not Status.OK:
                raise FimeException(f"Issue with key {issue_key} in unexpected state")

    def upload(self, issues: List[Tuple[str, str, timedelta]], pdate: date):
        """@:param issues: [(
            "ISS-1234",
            "I did some stuff",
            timedelta(seconds=300),
        ), ... ]
        """
        with self._issues_lock:
            self._upload_sanity_check(list(map(lambda x: x[0], issues)))
            for issue in issues:
                issue_key, comment, time_spent = issue
                if issue_key in self._issue_worklog_id:
                    self._worklog_update(issue_key, self._issue_worklog_id[issue_key], comment, time_spent, pdate)
                else:
                    self._worklog_create(issue_key, comment, time_spent, pdate)
                self._issue_state[issue[0]] = (Status.PROGRESS, "Working")

    def _worklog_create(self, issue_key: str, comment: str, time_spent: timedelta, pdate: date):
        future = self.session.post(
            self.worklog_url.format(issue_key),
            headers={
                "Authorization": f"Bearer {self.config.jira_token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            json={
                "started": datetime.combine(
                    pdate, time(8, 0), datetime.now().astimezone().tzinfo).strftime("%Y-%m-%dT%H:%M:%S.000%z"),
                "timeSpentSeconds": time_spent.seconds,
                "comment": comment,
            }
        )
        future.add_done_callback(partial(self._worklog_resp, issue_key))

    def _worklog_update(self, issue_key: str, worklog_id: str, comment: str, time_spent: timedelta, pdate: date):
        future = self.session.put(
            self.worklog_update_url.format(issue_key=issue_key, worklog_id=worklog_id),
            headers={
                "Authorization": f"Bearer {self.config.jira_token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            json={
                "started": datetime.combine(
                    pdate, time(8, 0), datetime.now().astimezone().tzinfo).strftime("%Y-%m-%dT%H:%M:%S.000%z"),
                "timeSpentSeconds": time_spent.seconds,
                "comment": comment,
            }
        )
        future.add_done_callback(partial(self._worklog_resp, issue_key))

    def _worklog_resp(self, issue_key: str, future: Future):
        resp: requests.Response = future.result()
        with self._issues_lock:
            if resp.status_code in (200, 201):
                self._issue_state[issue_key] = (Status.OK, "Successfully uploaded")
                logger.info(f"Successfully uploaded issue {issue_key}")
            else:
                msg = dedent(f"""\
                    Worklog upload failed:
                    Method: {resp.request.method}
                    URL: {resp.request.url}
                    Response code: {resp.status_code}
                    Response: {resp.text}
                    """)
                self._issue_state[issue_key] = (Status.ERROR, msg)
                logger.error(msg)
