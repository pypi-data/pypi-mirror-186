import atexit
import base64
import json
import os
from collections.abc import MutableMapping
from copy import deepcopy
from datetime import datetime, date, timedelta, time
from threading import Thread, Event
from typing import List, Tuple, Dict, Union

from loguru import logger

try:
    from PySide6 import QtCore
except ImportError:
    from PySide2 import QtCore

save_delay = 3 * 60
max_jira_tasks = 50


class Data(MutableMapping):
    def __init__(self):
        data_dir_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.AppDataLocation)
        self.data_path = os.path.join(data_dir_path, "data_{}.json")
        if not os.path.exists(data_dir_path):
            os.mkdir(data_dir_path)
        self._cache = {}
        self._hot_keys = set()
        self._trunning = False
        self._tevent = Event()
        self._thread = None

        def cleanup():
            self._trunning = False
            self._tevent.set()
            if self._thread:
                self._thread.join()

        atexit.register(cleanup)

    def __getitem__(self, key):
        dpath = self.data_path.format(key)
        if key not in self._cache and os.path.exists(dpath):
            with open(dpath, "r") as f:
                self._cache[key] = json.loads(f.read())
        return self._cache[key]

    def __setitem__(self, key, value):
        self._cache[key] = value
        self._hot_keys.add(key)
        self._schedule_save()

    def _schedule_save(self):
        if self._trunning:
            return
        self._trunning = True
        self._thread = Thread(target=self._executor, daemon=True)
        self._thread.start()

    def _executor(self):
        while self._trunning:
            self._tevent.wait(save_delay)
            self._save()

    def _save(self):
        for key in self._hot_keys:
            logger.info(f"saving dict {key}")
            to_write = self._cache[key]  # apparently thread-safe
            with open(self.data_path.format(key), "w+") as f:
                f.write(json.dumps(to_write))
        self._hot_keys = set()
        self._saving = False

    def __delitem__(self, key):
        return NotImplemented

    def __iter__(self):
        return NotImplemented

    def __len__(self):
        # TODO use glob?
        return NotImplemented

    def __repr__(self):
        return f"{type(self).__name__}({self._cache})"


class Tasks:
    def __init__(self, data: Data):
        self._data = data
        if "tasks" in self._data:
            self._tasks = list(map(lambda x: base64.b64decode(x.encode("utf-8")).decode("utf-8"), self._data["tasks"]))
        else:
            self._tasks = []
        if "jira_tasks" in self._data:
            self._jira_tasks_usage = dict()
            for k, v in self._data["jira_tasks"].items():
                key = base64.b64decode(k.encode("utf-8")).decode("utf-8")
                self._jira_tasks_usage[key] = datetime.fromisoformat(v)
                self._jira_tasks = sorted(self._jira_tasks_usage.keys(), key=lambda x: self._jira_tasks_usage[x])
        else:
            self._jira_tasks_usage = dict()
            self._jira_tasks = []

    @property
    def tasks(self) -> List[str]:
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        self._tasks = tasks
        encoded_tasks = list(map(lambda x: base64.b64encode(x.encode("utf-8")).decode("utf-8"), self._tasks))
        self._data["tasks"] = encoded_tasks

    @property
    def jira_tasks(self):
        return self._jira_tasks

    def add_jira_task(self, task_name):
        if task_name in self._jira_tasks_usage:
            self._jira_tasks.remove(task_name)  # move to end, to make visible again
        self._jira_tasks.append(task_name)
        self._jira_tasks_usage[task_name] = datetime.now()
        if len(self._jira_tasks_usage) > max_jira_tasks:
            sorted_tasks = sorted(self._jira_tasks_usage.keys(), key=lambda x: self._jira_tasks_usage[x])
            overhang_tasks = sorted_tasks[:len(sorted_tasks) - max_jira_tasks]
            for task in overhang_tasks:
                del self._jira_tasks_usage[task]
        self._save_jira_tasks()

    def update_jira_task_usage(self, task_name):
        if task_name in self._jira_tasks_usage:
            self._jira_tasks_usage[task_name] = datetime.now()
            self._save_jira_tasks()

    def _save_jira_tasks(self):
        serialized = dict()
        for k, v in self._jira_tasks_usage.items():
            key = base64.b64encode(k.encode("utf-8")).decode("utf-8")
            serialized[key] = datetime.isoformat(v)
        self._data["jira_tasks"] = serialized

    @property
    def all_tasks(self):
        return self.tasks + self.jira_tasks


class LogCommentsData:
    _init_day = {"log": [], "comments": {}}

    # Data.__setitem__ only gets triggered, when there is a direct assignment (in contrast to assignment down the tree)
    # this necessitates reassigning the whole month, when triggering a save is intended
    def __init__(self, data: Data):
        self._data = data
        self._converted = set()

    def _ensure_format(self, pdate: date):
        month_str = pdate.strftime("%Y-%m")
        if month_str in self._converted:
            return
        if month_str not in self._data:
            return
        for day, log in self._data[month_str].items():
            if type(log) is list:
                self._data[month_str][day] = {
                    "log": log,
                    "comments": {}
                }
        self._converted.add(month_str)

    def get_log(self, pdate: date) -> List[Tuple[datetime, str]]:
        self._ensure_format(pdate)
        month_str = pdate.strftime("%Y-%m")
        day_str = pdate.strftime("%d")
        if month_str not in self._data:
            return []
        if day_str not in self._data[month_str]:
            return []
        log_data = self._data[month_str][day_str]["log"]
        ret = []
        for entry in log_data:
            tstr, b64str = entry.split()
            start_time = datetime.combine(pdate, datetime.strptime(tstr, "%H:%M").time())
            task = base64.b64decode(b64str.encode("utf-8")).decode("utf-8")
            ret.append((start_time, task))
        return ret

    def set_log(self, pdate: date, log: List[Tuple[datetime, str]]):
        self._ensure_format(pdate)
        encoded = []
        for entry in log:
            tstr = entry[0].strftime("%H:%M")
            b64str = base64.b64encode(entry[1].encode("utf-8")).decode("utf-8")
            encoded.append(f"{tstr} {b64str}")
        month_str = pdate.strftime("%Y-%m")
        day_str = pdate.strftime("%d")
        month = self._data.setdefault(month_str, {})
        if month.setdefault(day_str, self._init_day)["log"] == encoded:
            return  # no changes
        month.setdefault(day_str, self._init_day)["log"] = encoded
        # trigger save
        self._data[month_str] = month

    def add_log_entry(self, task: str, start_time=None):
        if not start_time:
            start_time = datetime.now()
        self._ensure_format(start_time)
        tstr = start_time.strftime("%H:%M")
        b64str = base64.b64encode(task.encode("utf-8")).decode("utf-8")
        encoded = f"{tstr} {b64str}"
        month_str = start_time.strftime("%Y-%m")
        day_str = start_time.strftime("%d")
        month = self._data.setdefault(month_str, {})
        month.setdefault(day_str, self._init_day)["log"].append(encoded)
        self._data[month_str] = month

    def get_prev_next_avail(self, pdate: date) -> Tuple[date, date]:
        prev = None
        next = None
        for i in range(1, 32):
            new_date = pdate - timedelta(days=i)
            if new_date.strftime("%Y-%m") not in self._data:
                break
            if new_date.strftime("%d") in self._data[new_date.strftime("%Y-%m")]:
                prev = new_date
                break
        for i in range(1, 32):
            new_date = pdate + timedelta(days=i)
            if new_date > date.today():
                break
            if new_date.strftime("%Y-%m") not in self._data:
                break
            if new_date.strftime("%d") in self._data[new_date.strftime("%Y-%m")]:
                next = new_date
                break
        return prev, next

    def get_comments(self, pdate: date) -> Dict[str, str]:
        self._ensure_format(pdate)
        month_str = pdate.strftime("%Y-%m")
        day_str = pdate.strftime("%d")
        if month_str not in self._data:
            return dict()
        if day_str not in self._data[month_str]:
            return dict()
        comment_data = self._data[month_str][day_str]["comments"]
        ret = dict()
        for k, v in comment_data.items():
            k_dec = base64.b64decode(k.encode("utf-8")).decode("utf-8")
            v_dec = base64.b64decode(v.encode("utf-8")).decode("utf-8")
            ret[k_dec] = v_dec
        return ret

    def set_comments(self, pdate: date, comments: Dict[str, str]):
        self._ensure_format(pdate)
        encoded = dict()
        for k, v in comments.items():
            k_enc = base64.b64encode(k.encode("utf-8")).decode("utf-8")
            v_enc = base64.b64encode(v.encode("utf-8")).decode("utf-8")
            encoded[k_enc] = v_enc
        month_str = pdate.strftime("%Y-%m")
        day_str = pdate.strftime("%d")
        month = self._data.setdefault(month_str, {})
        if month.setdefault(day_str, self._init_day)["comments"] == encoded:
            return  # no changes
        month.setdefault(day_str, self._init_day)["comments"] = encoded
        # trigger save
        self._data[month_str] = month


class Log:
    def __init__(self, data: LogCommentsData):
        self._data = data
        self._start_date = date.today()

        def cleanup():
            self.log("End")

        atexit.register(cleanup)

    def log(self, task):
        if self._start_date != date.today():
            yesterday = date.today() - timedelta(days=1)
            yesterday_log = self.last_log(yesterday)
            if yesterday_log:
                self._data.add_log_entry("End", datetime.combine(yesterday, time(23, 59)))
                self._data.add_log_entry(yesterday_log, datetime.combine(date.today(), time(0, 0)))
            self._start_date = date.today()
        self._data.add_log_entry(task)

    def last_log(self, day=date.today()):
        log = self._data.get_log(day)
        if not log:
            return None
        if log[-1][1] == "End":
            del log[-1]
            self._data.set_log(day, log)
            if not log:
                return None
        return log[-1][1]


def summary(lcd: LogCommentsData, pdate: date) -> Tuple[Dict[str, timedelta], timedelta]:
    log = lcd.get_log(pdate)
    if pdate == date.today():
        log.append((datetime.now(), "End"))
    tasks_sums = {}
    total_sum = timedelta()
    for i, le in enumerate(log):
        start_time, task = le
        if i < len(log) - 1:
            end_time = log[i+1][0]
            duration = end_time - start_time
            if task != "Pause":
                task_sum = tasks_sums.setdefault(task, timedelta())
                task_sum += duration
                tasks_sums[task] = task_sum
                total_sum += duration
    return tasks_sums, total_sum


def duration_to_str(duration: timedelta) -> str:
    dhours, rem = divmod(duration.seconds, 3600)
    dmins, _ = divmod(rem, 60)
    return f"{dhours:02d}:{dmins:02d}"


class PrevNextable:
    def __init__(self, data: LogCommentsData):
        self._data = data
        self._prev = None
        self._next = None
        self._date = date.today()

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._prev, self._next = self._data.get_prev_next_avail(value)
        self._date = value

    def prev_next_avail(self) -> Tuple[bool, bool]:
        return self._prev is not None, self._next is not None

    def previous(self):
        self.date = self._prev

    def next(self):
        self.date = self._next

    def date_str(self) -> str:
        return self.date.strftime("%Y-%m-%d")


class Report(PrevNextable):
    def __init__(self, data: LogCommentsData):
        super().__init__(data)
        self._not_log_len = 0

    def report(self) -> Tuple[List[List[str]], int]:
        log = self._data.get_log(self.date)
        if self.date == date.today():
            log.append((datetime.now(), "End"))
        ret = []
        for i, t in enumerate(log):
            start_time, task = t
            if i < len(log) - 1:
                end_time = log[i+1][0]
                duration = end_time - start_time
                ret.append([task, start_time.strftime("%H:%M"), duration_to_str(duration)])
            else:
                ret.append([task, start_time.strftime("%H:%M"), ""])

        ret.append(["", "", ""])
        ret.append(["", "Sums", ""])

        tasks_summary, total_sum = summary(self._data, self.date)
        for task, duration in tasks_summary.items():
            ret.append([task, "", duration_to_str(duration)])
        ret.append(["Total sum", "", duration_to_str(total_sum)])
        self._not_log_len = 3 + len(tasks_summary)
        if self.date == date.today():
            self._not_log_len += 1
        editable_len = len(ret) - (4 + len(tasks_summary))

        return ret, editable_len

    def save(self, report):
        report = report[:-self._not_log_len]
        if not report:
            return
        report = list(map(
            lambda x: (datetime.combine(self.date, datetime.strptime(x[1], "%H:%M").time()), x[0]),
            report
        ))
        self._data.set_log(self.date, report)


class Worklog(PrevNextable):
    def __init__(self, data: LogCommentsData):
        super().__init__(data)
        self._worklog = []

    @property
    def worklog(self) -> List[List[Union[str, timedelta]]]:
        tasks_summary, total_sum = summary(self._data, self.date)
        comments = self._data.get_comments(self.date)
        self._worklog = []
        for task, duration in tasks_summary.items():
            self._worklog.append([task, comments.setdefault(task, ""), duration])
        self._worklog.append(["Total sum", "", total_sum])
        return deepcopy(self._worklog)

    @worklog.setter
    def worklog(self, worklog: List[List[str]]):
        log = self._data.get_log(self.date)
        set_comments = dict()
        for i, (task, comment, duration) in enumerate(worklog[:-1]):
            set_comments[task] = comment
            if self._worklog[i][0] != task:
                log = list(map(lambda x: (x[0], x[1].replace(self._worklog[i][0], task)), log))
        self._data.set_comments(self.date, set_comments)
        self._data.set_log(self.date, log)
