from typing import List, Optional

try:
    from PySide6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets

from datetime import datetime, date

from fime.data import Tasks, Report
from fime.util import get_screen_height, get_icon, EditStartedDetector


class ReportDialog(QtWidgets.QDialog):
    class TaskItemCompleter(EditStartedDetector):
        def __init__(self, tasks: Tasks, parent=None):
            super().__init__(parent)
            self._tasks = tasks

        def createEditor(self, parent, option, index):
            editor = super().createEditor(parent, option, index)
            completer = QtWidgets.QCompleter(self._tasks.all_tasks, parent)
            completer.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
            completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            editor.setCompleter(completer)
            return editor

    def __init__(self, tasks: Tasks, report: Report, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._report = report
        self._report_data: Optional[List[List[str]]] = None
        self._changing_items = False
        self._new_log_task = ""
        self._new_log_pos = -1
        self._edit_len = -1

        self.setWindowTitle("Report")

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Task", "Start time", "Duration"])
        self.tableWidget.cellChanged.connect(self.cell_changed)
        taskItemCompleter = ReportDialog.TaskItemCompleter(tasks, self)
        taskItemCompleter.editStarted.connect(self.disable_buttons)
        taskItemCompleter.editFinished.connect(self.enable_buttons)
        self.tableWidget.setItemDelegateForColumn(0, taskItemCompleter)
        editStartedDetector = EditStartedDetector(self)
        editStartedDetector.editStarted.connect(self.disable_buttons)
        editStartedDetector.editFinished.connect(self.enable_buttons)
        self.tableWidget.setItemDelegateForColumn(1, editStartedDetector)
        self.header = QtWidgets.QHeaderView(QtCore.Qt.Orientation.Horizontal)
        self.header.setMinimumSectionSize(1)
        self.header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeader(self.header)
        self.header.setSectionResizeMode(self.header.logicalIndex(0), QtWidgets.QHeaderView.Stretch)

        self.previous_button = QtWidgets.QPushButton()
        self.previous_button.setText("Previous")
        self.previous_button.setIcon(get_icon("arrow-left"))
        self.previous_button.pressed.connect(self.previous)
        self.previous_button.setAutoDefault(False)

        self.next_button = QtWidgets.QPushButton()
        self.next_button.setText("Next")
        self.next_button.setIcon(get_icon("arrow-right"))
        self.next_button.pressed.connect(self.next)
        self.next_button.setAutoDefault(False)

        self.new_button = QtWidgets.QPushButton()
        self.new_button.setText("New item")
        self.new_button.setIcon(get_icon("list-add"))
        self.new_button.pressed.connect(self.new_log)
        self.new_button.setAutoDefault(False)

        self.del_button = QtWidgets.QPushButton()
        self.del_button.setText("Delete item")
        self.del_button.setIcon(get_icon("list-remove"))
        self.del_button.pressed.connect(self.del_log)
        self.del_button.setAutoDefault(False)

        self.ok_button = QtWidgets.QPushButton()
        self.ok_button.setText("OK")
        self.ok_button.setIcon(get_icon("dialog-ok"))
        self.ok_button.pressed.connect(self._accept)
        self.ok_button.setAutoDefault(True)

        blayout = QtWidgets.QHBoxLayout()
        blayout.addWidget(self.previous_button)
        blayout.addWidget(self.next_button)
        blayout.addWidget(self.new_button)
        blayout.addWidget(self.del_button)
        blayout.addWidget(self.ok_button)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.tableWidget)
        layout.addLayout(blayout)
        self.setLayout(layout)

    def showEvent(self, _):
        self._report.date = date.today()
        self.update_title()
        self.refresh_table()
        self.update_prev_next()
        self.raise_()
        self.activateWindow()

    def save(self):
        self._report.save(self._report_data)

    def update_title(self):
        self.setWindowTitle(f"Report {self._report.date_str()}")

    def refresh_table(self):
        self._report_data, self._edit_len = self._report.report()
        self.tableWidget.setRowCount(len(self._report_data))

        self._changing_items = True
        for row, _ in enumerate(self._report_data):
            item0 = QtWidgets.QTableWidgetItem(self._report_data[row][0])
            self.tableWidget.setItem(row, 0, item0)
            item1 = QtWidgets.QTableWidgetItem(self._report_data[row][1])
            self.tableWidget.setItem(row, 1, item1)
            item2 = QtWidgets.QTableWidgetItem(self._report_data[row][2])
            self.tableWidget.setItem(row, 2, item2)
            item2.setFlags(item2.flags() & QtCore.Qt.ItemIsEnabled)
            if row >= self._edit_len:
                item0.setFlags(item1.flags() & QtCore.Qt.ItemIsEnabled)
            if row > self._edit_len:
                item1.setFlags(item0.flags() & QtCore.Qt.ItemIsEnabled)
        self._changing_items = False

        self.tableWidget.resizeColumnToContents(0)

        if self.tableWidget.rowCount() > 4:
            self.tableWidget.setMinimumHeight(
                min(
                    (self.tableWidget.rowCount()) * self.tableWidget.rowHeight(0) + self.header.height() + 4,
                    get_screen_height(self.tableWidget) * 0.8
                )
            )

    def update_prev_next(self):
        prev, next_ = self._report.prev_next_avail()
        self.previous_button.setEnabled(prev)
        self.next_button.setEnabled(next_)

    @QtCore.Slot()
    def del_log(self):
        row = self.tableWidget.currentRow()
        if row > len(self._report_data) - 4:
            return
        del self._report_data[row]
        self.save()
        self.refresh_table()

    @QtCore.Slot()
    def new_log(self):
        after = min(self.tableWidget.currentItem().row(), self._edit_len-1) + 1
        self._new_log_pos = after
        self.tableWidget.insertRow(after)
        self.tableWidget.setCurrentCell(after, 0)
        item = QtWidgets.QTableWidgetItem()
        self._changing_items = True
        self.tableWidget.setItem(after, 0, item)
        self._changing_items = False
        self.tableWidget.editItem(item)

    @QtCore.Slot()
    def disable_buttons(self):
        self.previous_button.setEnabled(False)
        self.next_button.setEnabled(False)
        self.del_button.setEnabled(False)
        self.new_button.setEnabled(False)
        self.ok_button.setEnabled(False)

    @QtCore.Slot()
    def enable_buttons(self):
        self.del_button.setEnabled(True)
        self.new_button.setEnabled(True)
        self.ok_button.setEnabled(True)
        self.update_prev_next()

    @QtCore.Slot()
    def _accept(self):
        self.save()
        self.accept()

    @QtCore.Slot()
    def previous(self):
        self.save()
        self._report.previous()
        self.update_title()
        self.refresh_table()
        self.update_prev_next()

    @QtCore.Slot()
    def next(self):
        self.save()
        self._report.next()
        self.update_title()
        self.refresh_table()
        self.update_prev_next()

    @QtCore.Slot()
    def cell_changed(self, row, column):
        if self._changing_items:
            return
        if column == 2:
            self.tableWidget.item(row, column).setText(self._report_data[row][column])
            return
        item = self.tableWidget.item(row, column)
        if column == 0:
            if self._new_log_pos == row:
                self._new_log_task = self.tableWidget.item(row, column).text() or "Unnamed"
                return
            else:
                self._report_data[row][column] = item.text() or "Unnamed"
        if column == 1:
            try:
                new_time = datetime.strptime(item.text(), "%H:%M").time()
            except ValueError:
                item.setText(self._report_data[row][column])
                return
            if self._new_log_pos == row:
                self._report_data.insert(row, [self._new_log_task, new_time.strftime("%H:%M"), ""])
            else:
                self._report_data[row][column] = new_time.strftime("%H:%M")
            self._new_log_pos = -1
            self._new_log_task = ""
        self.save()
        self.refresh_table()
