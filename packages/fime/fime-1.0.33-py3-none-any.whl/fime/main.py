#!/usr/bin/env python3
import signal
import sys
from functools import partial
from pathlib import Path
from typing import Optional

from loguru import logger

try:
    from PySide6 import QtCore, QtWidgets
    PYSIDE_6 = True
except ImportError:
    from PySide2 import QtCore, QtWidgets
    PYSIDE_6 = False

from fime.about import About
from fime.config import Config
from fime.worklog import WorklogDialog
from fime.data import Tasks, Log, Data, LogCommentsData, Worklog, Report
from fime.exceptions import FimeException
from fime.import_task import ImportTask
from fime.report import ReportDialog
from fime.settings import Settings
from fime.task_edit import TaskEdit
from fime.util import get_screen_height, get_icon


class App:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)

        data = Data()
        self.tasks = Tasks(data)
        lcd = LogCommentsData(data)
        self.log = Log(lcd)
        self._active_task = self.log.last_log() or "Nothing"

        self.config = Config()

        self.menu = QtWidgets.QMenu(None)

        self.import_task = ImportTask(self.config, None)
        self.import_task.accepted.connect(self.new_task_imported)

        self.taskEdit = TaskEdit(self.tasks, None)
        self.taskEdit.accepted.connect(self.tasks_edited)

        self.reportDialog = ReportDialog(self.tasks, Report(lcd), None)
        self.reportDialog.accepted.connect(self.log_edited)

        self.worklogDialog = WorklogDialog(self.config, Worklog(lcd), None)
        self.worklogDialog.accepted.connect(self.log_edited)

        self.settings = Settings(self.config, None)
        self.settings.accepted.connect(self.update_icon)
        self.settings.accepted.connect(self.update_tray_menu)

        self.about = About(None)

        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setContextMenu(self.menu)
        self.update_icon()
        self.tray.show()
        self.tray.setToolTip("fime")
        self.update_tray_menu()

        self.last_dialog: Optional[QtWidgets.QDialog] = None

    def update_icon(self):
        if self.config.tray_theme == "light":
            icon = get_icon("appointment-new-light")
        else:
            icon = get_icon("appointment-new")
        self.tray.setIcon(icon)

    @QtCore.Slot()
    def new_task_imported(self):
        if self.import_task.task_text:
            self.tasks.add_jira_task(self.import_task.task_text)
            if self.import_task.change_task:
                self.change_task(self.import_task.task_text)
            self.update_tray_menu()

    @QtCore.Slot()
    def tasks_edited(self):
        self.tasks.tasks = self.taskEdit.tasks
        self.update_tray_menu()

    @QtCore.Slot()
    def log_edited(self):
        self.active_task = self.log.last_log() or "Nothing"

    @property
    def active_task(self):
        return self._active_task

    @active_task.setter
    def active_task(self, task):
        self._active_task = task
        self.tray.setToolTip(f"{task} - fime")
        self.update_tray_menu()

    def close_open_dialog(self):
        if self.last_dialog and self.last_dialog.isVisible():
            self.last_dialog.reject()

    def change_task(self, task):
        self.close_open_dialog()
        self.active_task = task
        self.log.log(task)
        self.tasks.update_jira_task_usage(task)

    def open_new_dialog(self, new_dialog: QtWidgets.QDialog):
        self.close_open_dialog()
        self.last_dialog = new_dialog
        new_dialog.show()

    def update_tray_menu(self):
        menu_items = []
        tmp_action = self.menu.addAction("tmp")
        action_height = self.menu.actionGeometry(tmp_action).height()

        def add_tasks(tasks):
            for t in tasks:
                menu_items.append((t, partial(self.change_task, t)))

        self.menu.clear()
        add_tasks(self.tasks.tasks)

        menu_items.append((1, None))
        already_taken = (len(self.tasks.tasks) + 6) * action_height
        available_space = get_screen_height(self.menu) * 0.8 - already_taken
        jira_entry_count = int(available_space // action_height)
        add_tasks(self.tasks.jira_tasks[-jira_entry_count:])

        menu_items.append((1, None))
        add_tasks(["Pause"])
        if self.active_task == "Nothing":
            add_tasks(["Nothing"])

        menu_items.append((1, None))
        jira_integration = self.config.jira_url and self.config.jira_token
        if jira_integration:
            menu_items.append(("Import Jira task", partial(self.open_new_dialog, self.import_task)))
        menu_items.append(("Edit tasks", partial(self.open_new_dialog, self.taskEdit)))
        menu_items.append(("Report", partial(self.open_new_dialog, self.reportDialog)))
        if jira_integration:
            menu_items.append(("Worklog", partial(self.open_new_dialog, self.worklogDialog)))

        menu_items.append((1, None))

        menu_items.append(("Settings", partial(self.open_new_dialog, self.settings)))
        menu_items.append(("About", partial(self.open_new_dialog, self.about)))
        menu_items.append(("Close", self.app.quit))

        if self.config.flip_menu:
            menu_items.reverse()

        seps = 0
        for item in menu_items:
            if item[0] == 1:
                self.menu.addSeparator()
                seps += 1
                continue
            action = self.menu.addAction(item[0])
            if item[0] == self.active_task and seps <= 2:
                action.setIcon(get_icon("go-next"))
            action.triggered.connect(item[1])

    def sigterm_handler(self, signo, _frame):
        logger.debug(f'handling signal "{signal.strsignal(signo)}"')
        self.app.quit()

    def run(self):
        timer = QtCore.QTimer(None)
        # interrupt event loop regularly for signal handling
        timer.timeout.connect(lambda: None)
        timer.start(500)
        signal.signal(signal.SIGTERM, self.sigterm_handler)
        signal.signal(signal.SIGINT, self.sigterm_handler)
        if PYSIDE_6:
            self.app.exec()
        else:
            self.app.exec_()


def init_logging():
    log_dir_path = Path(QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.AppDataLocation)) / "logs"
    logger.add(log_dir_path / "fime_{time:YYYY-MM-DD}.log", rotation="1d", retention="30d", compression="zip", level="DEBUG")


def excepthook(e_type, e_value, tb_obj):
    if e_type is FimeException:
        QtWidgets.QMessageBox.critical(None, "Error", str(e_value), QtWidgets.QMessageBox.Ok)
    elif issubclass(e_type, KeyboardInterrupt):
        sys.__excepthook__(e_type, e_value, tb_obj)
    else:
        logger.critical("Unhandled exception", exc_info=(e_type, e_value, tb_obj))
        sys.__excepthook__(e_type, e_value, tb_obj)


def main():
    # important for QStandardPath to be correct
    QtCore.QCoreApplication.setApplicationName("fime")
    init_logging()
    # also catches exceptions in other threads
    sys.excepthook = excepthook
    app = App()
    app.run()


if __name__ == "__main__":
    main()
