try:
    from PySide6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets

from fime.config import Config
from fime.progressindicator import ProgressIndicator
from fime.task_completer import TaskCompleter
from fime.util import get_icon


class ImportTask(QtWidgets.QDialog):
    def __init__(self, config: Config, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowTitle("New Tasks")

        self.config = config

        self.line_edit = QtWidgets.QLineEdit(self)
        self.completer = TaskCompleter(config)
        self.line_edit.setCompleter(self.completer)
        self.line_edit.textChanged.connect(self.completer.update_picker)
        self.line_edit.setFocus()

        self.indicator = ProgressIndicator(self)
        self.indicator.setAnimationDelay(70)
        self.indicator.setDisplayedWhenStopped(False)
        self.completer.running.connect(self.spin)
        self.completer.stopped.connect(self.no_spin)

        self.auto_change_task_check_box = QtWidgets.QCheckBox()
        self.auto_change_task_check_box.setText("Set as active task after import")

        ok_button = QtWidgets.QPushButton()
        ok_button.setText("OK")
        ok_button.setIcon(get_icon("dialog-ok"))
        ok_button.pressed.connect(self.accept)
        ok_button.setAutoDefault(True)

        cancel_button = QtWidgets.QPushButton()
        cancel_button.setText("Cancel")
        cancel_button.setIcon(get_icon("dialog-cancel"))
        cancel_button.pressed.connect(self.reject)
        cancel_button.setAutoDefault(False)

        alayout = QtWidgets.QStackedLayout()
        alayout.setStackingMode(QtWidgets.QStackedLayout.StackAll)
        alayout.addWidget(self.line_edit)
        size = self.line_edit.height()
        self.indicator.setMaximumSize(QtCore.QSize(size * 0.75, size * 0.75))
        aalayout = QtWidgets.QVBoxLayout()
        aalayout.addWidget(self.indicator, alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        marg = aalayout.contentsMargins()
        marg.setRight(size * 0.15)
        aalayout.setContentsMargins(marg)
        aawidget = QtWidgets.QWidget()
        aawidget.setLayout(aalayout)
        alayout.addWidget(aawidget)
        alayout.setCurrentWidget(aawidget)

        blayout = QtWidgets.QHBoxLayout()
        blayout.addSpacing(300)
        blayout.addWidget(self.auto_change_task_check_box)
        blayout.addWidget(cancel_button)
        blayout.addWidget(ok_button)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(alayout)
        layout.addLayout(blayout)
        self.setLayout(layout)
        self.resize(500, 0)

    @QtCore.Slot()
    def spin(self):
        self.indicator.startAnimation()

    @QtCore.Slot()
    def no_spin(self):
        self.indicator.stopAnimation()

    @property
    def task_text(self):
        return self.line_edit.text()

    @property
    def change_task(self):
        return self.auto_change_task_check_box.isChecked()

    def showEvent(self, _):
        self.auto_change_task_check_box.setChecked(self.config.import_auto_change_task)
        # pick up config changes
        self.completer.update_urls()
        self.line_edit.setText("")
        self.raise_()
        self.activateWindow()
        self.line_edit.setFocus()
