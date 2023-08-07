import sys
from copy import copy
from pathlib import Path
from textwrap import dedent
from threading import Lock
from typing import Optional

from loguru import logger
from packaging.version import Version
from requests_futures.sessions import FuturesSession

try:
    from PySide6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets

import fime
from fime.progressindicator import ProgressIndicator
from fime.util import get_icon

URL = "https://gitlab.com/faerbit/fime/-/releases/permalink/latest"


class UpdateChecker:
    def __init__(self):
        self.session = FuturesSession()
        future = self.session.get(URL, allow_redirects=False)
        future.add_done_callback(self.process_response)
        self.lock = Lock()
        self._done = False
        self.result = "Could not determined latest fime version"

    @property
    def done(self):
        with self.lock:
            ret = copy(self._done)
        return ret

    def process_response(self, future):
        try:
            resp = future.result()
            if resp.status_code != 302 or "Location" not in resp.headers:
                raise RuntimeError("Requested unexpectedly did not redirect")
            latest_version = resp.headers["Location"].split("/")[-1]
            latest_version = Version(latest_version)
            own_version = Version(fime.__version__)
            if own_version == latest_version:
                self.result = "Latest fime version installed"
            elif own_version > latest_version:
                self.result = f"Older fime version available: {latest_version}"
            else:
                self.result = f"Newer fime version available: {latest_version}"
        except Exception:
            logger.exception("Could not get update info")
        finally:
            with self.lock:
                self._done = True


class About(QtWidgets.QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowTitle("About")

        log_dir_path = Path(QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.AppDataLocation)) / "logs"

        text = dedent(f"""\
        fime
        Copyright (c) 2020 - 2022 Faerbit
        <a href="https://fime.faerb.it">Website</a> <a href="https://gitlab.com/faerbit/fime/-/blob/main/LICENSE">License</a>
        
        fime Version {fime.__version__}
        Qt Version {QtCore.__version__}
        Python Version {sys.version}
        
        Log directory: <a href="{log_dir_path}">{log_dir_path}</a>
        """)
        text = text.replace("\n", "<br/>")
        version_label = QtWidgets.QLabel(self)
        version_label.setText(text)
        version_label.setTextFormat(QtCore.Qt.RichText)
        version_label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        version_label.setOpenExternalLinks(True)
        version_label.setAlignment(QtCore.Qt.AlignHCenter)

        self.update_layout = QtWidgets.QHBoxLayout()

        self.ok_button = QtWidgets.QPushButton()
        self.ok_button.setText("OK")
        self.ok_button.setIcon(get_icon("dialog-ok"))
        self.ok_button.pressed.connect(self.accept)
        self.ok_button.setAutoDefault(True)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addStretch(66)
        hlayout.addWidget(self.ok_button, 33)

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(version_label)
        vlayout.addLayout(self.update_layout)
        vlayout.addLayout(hlayout)

        self.setLayout(vlayout)

        self.update_checker: Optional[UpdateChecker] = None
        self.update_timer = QtCore.QTimer(self)
        self.update_timer.setInterval(500)
        self.update_timer.timeout.connect(self.timer_callback)

    def clear_update_layout(self):
        while self.update_layout.count():
            child = self.update_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def timer_callback(self):
        if self.update_checker.done:
            self.clear_update_layout()
            update_label = QtWidgets.QLabel(self)
            update_label.setText(self.update_checker.result)
            update_label.setAlignment(QtCore.Qt.AlignHCenter)

            self.update_layout.addWidget(update_label)
            self.update_timer.stop()

    def showEvent(self, _):
        self.clear_update_layout()

        progress_indicator = ProgressIndicator(self)
        progress_indicator.setAnimationDelay(70)
        progress_indicator.startAnimation()

        update_label = QtWidgets.QLabel(self)
        update_label.setText("Checking for latest version...")

        self.update_layout.addStretch()
        self.update_layout.addWidget(progress_indicator)
        self.update_layout.addWidget(update_label)
        self.update_layout.addStretch()

        self.update_checker = UpdateChecker()
        self.update_timer.start()
