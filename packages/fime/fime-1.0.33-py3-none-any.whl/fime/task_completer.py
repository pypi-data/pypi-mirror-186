import os
import re
import threading
from enum import Enum, auto
from functools import reduce, partial
from queue import Queue, Empty

from loguru import logger
from requests import Response

try:
    from PySide6 import QtCore, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtWidgets
from requests_futures.sessions import FuturesSession

from fime.config import Config


class TaskCompleter(QtWidgets.QCompleter):
    class RifState(Enum):
        RUNNING = auto()
        STOPPED = auto()

    running = QtCore.Signal()
    stopped = QtCore.Signal()

    def __init__(self, config: Config, parent=None, *args, **kwargs):
        super().__init__([], parent, *args, **kwargs)
        self.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        self.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.session = FuturesSession()
        self.config = config
        self.picker_url = None
        self.search_url = None
        self.issue_url_tmpl = None
        self.issue_key_regex = re.compile(r"^[a-zA-Z0-9]+-[0-9]+")
        self.update_urls()
        self.text = ""
        self.response_text = ""
        self.model_data = set()
        self.escalate = False
        self.update_timer = QtCore.QTimer(self)
        self.update_timer.timeout.connect(self.process_response)
        self.update_timer.setInterval(200)
        self.queue = Queue()
        # Request In Flight
        self.rif_counter = 0
        self.rif_counter_lock = threading.Lock()
        self.last_rif_state = TaskCompleter.RifState.STOPPED

    def update_urls(self):
        self.picker_url = os.path.join(self.config.jira_url, "rest/api/2/issue/picker")
        self.search_url = os.path.join(self.config.jira_url, "rest/api/2/search")
        self.issue_url_tmpl = os.path.join(self.config.jira_url, "rest/api/2/issue/{}")

    @QtCore.Slot()
    def process_response(self):
        with self.rif_counter_lock:
            if self.last_rif_state is TaskCompleter.RifState.STOPPED and self.rif_counter != 0:
                self.last_rif_state = TaskCompleter.RifState.RUNNING
                self.running.emit()
            if self.last_rif_state is TaskCompleter.RifState.RUNNING and self.rif_counter == 0:
                self.last_rif_state = TaskCompleter.RifState.STOPPED
                self.stopped.emit()
        try:
            while not self.queue.empty():
                result_dict = self.queue.get_nowait()
                if result_dict["response_text"] == self.text:
                    if self.text == self.response_text:
                        self.response_text = result_dict["response_text"]
                        self.model_data = set(result_dict["result"])
                    else:
                        self.model_data = self.model_data.union(set(result_dict["result"]))
                    self.model().setStringList(self.model_data)
                    self.complete()
        except Empty:
            return

    @QtCore.Slot(str)
    def update_picker(self, text):
        self.text = text
        if self.text == self.currentCompletion():
            # do not update, after auto completion was used
            return
        if self.escalate:
            self.update_search()
            self.update_issue()
        if not self.update_timer.isActive():
            self.update_timer.start()
        future = self.session.get(
            url=self.picker_url,
            params={
                "query": self.text
            },
            headers={
                "Authorization": f"Bearer {self.config.jira_token}",
                "Accept": "application/json",
            },
        )
        with self.rif_counter_lock:
            self.rif_counter += 1
        future.add_done_callback(partial(self.picker_response_callback, self.text))

    def picker_response_callback(self, text, future):
        with self.rif_counter_lock:
            self.rif_counter -= 1
        try:
            result = future.result()
            issues = reduce(lambda x, y: x + (y["issues"]), result.json()["sections"], [])
            extracted = list(map(lambda x: f"{x['key']} {x['summaryText']}", issues))
            if extracted:
                self.queue.put({
                    "response_text": text,
                    "result": extracted,
                })
            else:
                if not self.escalate:
                    logger.debug("No picker results. Escalating")
                    self.escalate = True
                    self.update_search()
                    self.update_issue()
        except Exception:
            logger.exception("Ignoring exception, as it only breaks autocompletion")
            return

    def update_search(self):
        for jql in [f"text = {self.text}", f"key = {self.text}"]:
            future = self.session.get(
                url=self.search_url,
                params={
                    "jql": jql,
                    "maxResults": 10,
                    "fields": "key,summary",
                },
                headers={
                    "Authorization": f"Bearer {self.config.jira_token}",
                    "Accept": "application/json",
                },
            )
            with self.rif_counter_lock:
                self.rif_counter += 1
            future.add_done_callback(partial(self.search_response_callback, self.text))

    def search_response_callback(self, text, future):
        with self.rif_counter_lock:
            self.rif_counter -= 1
        try:
            result = future.result()
            json_result = result.json()
            if "issues" in json_result:
                extracted = list(map(lambda x: f"{x['key']} {x['fields']['summary']}", json_result["issues"]))
                self.queue.put({
                    "response_text": text,
                    "result": extracted,
                })
        except Exception:
            logger.exception("Ignoring exception, as it only breaks autocompletion")
            return

    def update_issue(self):
        stripped = self.text.strip()
        if not self.issue_key_regex.match(stripped):
            return
        future = self.session.get(
            self.issue_url_tmpl.format(stripped.upper()),
            headers={
                "Authorization": f"Bearer {self.config.jira_token}",
                "Accept": "application/json",
            },
        )
        with self.rif_counter_lock:
            self.rif_counter += 1
        future.add_done_callback(partial(self.issue_response_callback, self.text))

    def issue_response_callback(self, text: str, future):
        with self.rif_counter_lock:
            self.rif_counter -= 1
        try:
            resp: Response = future.result()
            if resp.status_code < 199 or resp.status_code >= 300:
                return
            json_result = resp.json()
            extracted = f'{text.strip().upper()} {json_result["fields"]["summary"]}'
            self.queue.put({
                "response_text": text,
                "result": extracted,
            })
        except Exception:
            logger.exception("Ignoring exception, as it only breaks autocompletion")
            return
