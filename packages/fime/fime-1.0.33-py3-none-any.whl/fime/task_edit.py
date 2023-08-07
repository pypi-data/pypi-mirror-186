try:
    from PySide6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets

from fime.data import Tasks
from fime.util import get_icon, EditStartedDetector


class TaskEdit(QtWidgets.QDialog):
    def __init__(self, tasks: Tasks, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._task_data = tasks

        self.setWindowTitle("Edit Tasks")
        self.list = QtCore.QStringListModel()

        self.tableView = QtWidgets.QTableView()
        self.tableView.setModel(self.list)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().hide()
        self.tableView.verticalHeader().hide()
        editStartedDetector = EditStartedDetector(self)
        editStartedDetector.editStarted.connect(self.disable_buttons)
        editStartedDetector.editFinished.connect(self.enable_buttons)
        self.tableView.setItemDelegate(editStartedDetector)

        self.new_button = QtWidgets.QPushButton()
        self.new_button.setText("New item")
        self.new_button.setIcon(get_icon("list-add"))
        self.new_button.pressed.connect(self.new_task)
        self.new_button.setAutoDefault(False)

        self.del_button = QtWidgets.QPushButton()
        self.del_button.setText("Delete item")
        self.del_button.setIcon(get_icon("list-remove"))
        self.del_button.pressed.connect(self.del_task)
        self.del_button.setAutoDefault(False)

        self.ok_button = QtWidgets.QPushButton()
        self.ok_button.setText("OK")
        self.ok_button.setIcon(get_icon("dialog-ok"))
        self.ok_button.pressed.connect(self.accept)
        self.ok_button.setAutoDefault(True)

        blayout = QtWidgets.QHBoxLayout()
        blayout.addWidget(self.new_button)
        blayout.addWidget(self.del_button)
        blayout.addWidget(self.ok_button)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tableView)
        layout.addLayout(blayout)
        self.setLayout(layout)

    @QtCore.Slot()
    def disable_buttons(self):
        self.del_button.setEnabled(False)
        self.new_button.setEnabled(False)
        self.ok_button.setEnabled(False)

    @QtCore.Slot()
    def enable_buttons(self):
        self.del_button.setEnabled(True)
        self.new_button.setEnabled(True)
        self.ok_button.setEnabled(True)

    @QtCore.Slot()
    def new_task(self):
        l = self.list.stringList()
        l.append("")
        self.list.setStringList(l)
        i = self.list.index(len(l)-1)
        self.tableView.setCurrentIndex(i)
        self.tableView.edit(i)

    @QtCore.Slot()
    def del_task(self):
        l = self.list.stringList()
        del l[self.tableView.currentIndex().row()]
        self.list.setStringList(l)

    @property
    def tasks(self):
        ret = self.list.stringList()
        return list(filter(None, ret))  # filter empty strings

    def showEvent(self, _):
        self.list.setStringList(self._task_data.tasks)
        self.raise_()
        self.activateWindow()
