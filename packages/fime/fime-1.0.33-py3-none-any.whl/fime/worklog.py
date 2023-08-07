from datetime import date
from functools import reduce, partial
from typing import List, Tuple

from fime.config import Config
from fime.data import Worklog, duration_to_str
from fime.progressindicator import ProgressIndicator
from fime.task_completer import TaskCompleter
from fime.util import get_icon, EditStartedDetector, Status, get_screen_height, get_screen_width
from fime.worklog_rest import WorklogRest

try:
    from PySide6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets


class WorklogDialog(QtWidgets.QDialog):
    class TabTable(QtWidgets.QTableWidget):
        def __init__(self, parent, *args, **kwargs):
            super().__init__(parent, *args, **kwargs)

        def focusNextPrevChild(self, next_):
            if self.currentColumn() == 1:
                event = QtGui.QKeyEvent(QtCore.QEvent.KeyPress,
                                        QtCore.Qt.Key_Down if next_ else QtCore.Qt.Key_Up,
                                        QtCore.Qt.NoModifier)
                self.keyPressEvent(event)
                if event.isAccepted():
                    return True
            return super().focusNextPrevChild(next_)

    class ClickWidget(QtWidgets.QWidget):
        def __init__(self, item, table, parent, *args, **kwargs):
            super().__init__(parent, *args, **kwargs)
            self.item = item
            self.table = table

        def mouseDoubleClickEvent(self, event):
            self.table.removeCellWidget(self.item.row(), self.item.column())
            self.table.openPersistentEditor(self.item)
            editor = self.table.cellWidget(self.table.currentRow(), self.table.currentColumn())
            editor.setFocus()

    class TableTextEdit(QtWidgets.QTextEdit):
        text_changed = QtCore.Signal(str, int)

        def __init__(self, text, row, parent, *args, **kwargs):
            super().__init__(parent, *args, **kwargs)
            self.row = row
            self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
            self.setAcceptRichText(False)
            self.setTabChangesFocus(True)
            self.setText(text)
            self.document().adjustSize()
            self.on_text_changed()
            self.moveCursor(QtGui.QTextCursor.End)
            self.textChanged.connect(self.on_text_changed)

        @QtCore.Slot()
        def on_text_changed(self):
            self.setFixedHeight(self.document().size().toSize().height())
            self.text_changed.emit(self.document().toPlainText(), self.row)

    class TaskItemCompleter(EditStartedDetector):
        edit_finished_row = QtCore.Signal(int)

        def __init__(self, config, parent=None):
            super().__init__(parent)
            self.config = config
            self.return_ = False
            self.initial_text = ""
            self.editor = None

        def createEditor(self, parent, option, index):
            self.editor = super().createEditor(parent, option, index)
            self.editFinished.connect(partial(self.edit_finished_row_target, index.row()))
            self.return_ = False
            self.initial_text = index.data()
            self.editor.returnPressed.connect(self.return_pressed)
            completer = TaskCompleter(self.config)
            completer.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
            completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            self.editor.setCompleter(completer)
            self.editor.textChanged.connect(completer.update_picker)
            return self.editor

        @QtCore.Slot()
        def return_pressed(self):
            self.return_ = True

        @QtCore.Slot()
        def edit_finished_row_target(self, row):
            if not self.return_ or self.editor.text() == self.initial_text:
                self.edit_finished_row.emit(row)

    def __init__(self, config: Config, worklog: Worklog, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.config = config
        self.rest = None

        self._changing_items = False
        self._worklog = worklog
        self._worklog_data: List[List[str]] = []
        self._statuses: List[Tuple[Status, str]] = []
        self.row_height = None
        self._focussed = False

        self.setWindowTitle("Worklog")

        self.tableWidget = WorklogDialog.TabTable(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Task", "Comment", "Duration"])
        self.tableWidget.cellChanged.connect(self.cell_changed)
        taskItemCompleter = WorklogDialog.TaskItemCompleter(config, self)
        taskItemCompleter.editStarted.connect(self.disable_buttons)
        taskItemCompleter.editFinished.connect(self.enable_buttons)
        taskItemCompleter.edit_finished_row.connect(self.update_status_view)
        self.tableWidget.setItemDelegateForColumn(0, taskItemCompleter)
        self.hheader = QtWidgets.QHeaderView(QtCore.Qt.Orientation.Horizontal)
        self.hheader.setMinimumSectionSize(10)
        self.tableWidget.setHorizontalHeader(self.hheader)
        self.hheader.setSectionResizeMode(self.hheader.logicalIndex(0), QtWidgets.QHeaderView.Fixed)
        self.hheader.setSectionResizeMode(self.hheader.logicalIndex(1), QtWidgets.QHeaderView.Fixed)
        self.hheader.resizeSection(self.hheader.logicalIndex(1), get_screen_width(self) * 0.2)
        self.hheader.setSectionResizeMode(self.hheader.logicalIndex(2), QtWidgets.QHeaderView.ResizeToContents)
        self.vheader = QtWidgets.QHeaderView(QtCore.Qt.Orientation.Vertical)
        self.vheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.vheader.hide()
        self.tableWidget.setVerticalHeader(self.vheader)
        self.tableWidget.setMaximumWidth(get_screen_width(self) * 0.8)

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

        self.upload_button = QtWidgets.QPushButton()
        self.upload_button.setText("Upload")
        self.upload_button.setIcon(get_icon("cloud-upload"))
        self.upload_button.pressed.connect(self.upload)
        self.upload_button.setAutoDefault(False)
        self.upload_button.setMinimumWidth(self.upload_button.minimumSizeHint().width() * 1.33)
        self.upload_button.setEnabled(False)

        self.ok_button = QtWidgets.QPushButton()
        self.ok_button.setText("OK")
        self.ok_button.setIcon(get_icon("dialog-ok"))
        self.ok_button.pressed.connect(self._accept)
        self.ok_button.setAutoDefault(True)

        alayout = QtWidgets.QHBoxLayout()
        alayout.addWidget(self.previous_button)
        alayout.addWidget(self.next_button)
        alayout.addSpacerItem(QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Expanding))
        alayout.addWidget(self.upload_button)
        alayout.addWidget(self.ok_button)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.tableWidget)
        layout.addLayout(alayout)
        self.setLayout(layout)

        self.update_timer = QtCore.QTimer(self)
        self.update_timer.setInterval(500)
        self.update_timer.timeout.connect(self.update_statuses)

    def showEvent(self, _):
        # reinitialize to purge caches and pick up config changes
        self.rest = WorklogRest(self.config)
        self._worklog.date = date.today()
        self.update_all()
        self.upload_button.setEnabled(False)
        self.raise_()
        self.activateWindow()

    def update_all(self):
        self.refresh_table()
        self.update_title()
        self.update_prev_next()
        self._statuses = []
        self.update_statuses()
        self.update_timer.start()

    def update_statuses(self):
        issue_keys = []
        for row in self._worklog_data[:-1]:
            issue_keys.append(row[0].split()[0])
        old_statuses = self._statuses
        self._statuses = self.rest.get_issues_state(issue_keys, self._worklog.date)
        for row, status in enumerate(self._statuses):
            if len(old_statuses) != len(self._statuses) or old_statuses[row][0] != status[0]:
                self.update_status_view(row)
            if not self._worklog_data[row][1] and status[2]:
                self._worklog_data[row][1] = status[2]
                self.tableWidget.cellWidget(row, 1).setPlainText(status[2])
        all_ok = reduce(lambda acc, it: acc and it[0] is Status.OK, self._statuses, True)
        if all_ok:
            self.upload_button.setEnabled(True)
        all_done = reduce(lambda acc, it: acc and it[0] is not Status.PROGRESS, self._statuses, True)
        if all_done:
            self.update_timer.stop()

    def save(self):
        self._worklog.worklog = self._worklog_data

    def update_title(self):
        self.setWindowTitle(f"Worklog {self._worklog.date_str()}")

    def refresh_table(self):
        self._worklog_data = self._worklog.worklog
        self._changing_items = True
        if not self.row_height:
            self.tableWidget.setRowCount(1)
            item = QtWidgets.QTableWidgetItem("test")
            self.tableWidget.setItem(0, 0, item)
            self.row_height = self.tableWidget.rowHeight(0)
        self.tableWidget.setRowCount(len(self._worklog_data))

        for row, _ in enumerate(self._worklog_data):
            item0 = QtWidgets.QTableWidgetItem(self._worklog_data[row][0])
            self.tableWidget.setItem(row, 0, item0)
            if row == len(self._worklog_data) - 1:
                self.tableWidget.removeCellWidget(row, 0)
                item0.setFlags(item0.flags() & QtCore.Qt.ItemIsEnabled)
                item1 = QtWidgets.QTableWidgetItem("")
                self.tableWidget.setItem(row, 1, item1)
                item1.setFlags(item1.flags() & QtCore.Qt.ItemIsEnabled)
            else:
                text_edit = WorklogDialog.TableTextEdit(self._worklog_data[row][1], row, self)
                text_edit.textChanged.connect(self.on_resize)
                text_edit.setFrameStyle(QtWidgets.QFrame.NoFrame)
                text_edit.text_changed.connect(self.text_edit_changed)
                self.tableWidget.setCellWidget(row, 1, text_edit)
                if row == 0 and not self._focussed:
                    text_edit.setFocus()
                    self._focussed = True
            item2 = QtWidgets.QTableWidgetItem(duration_to_str(self._worklog_data[row][2]))
            self.tableWidget.setItem(row, 2, item2)
            item2.setFlags(item2.flags() & QtCore.Qt.ItemIsEnabled)
        self._changing_items = False

        self.tableWidget.resizeColumnToContents(0)
        self.tableWidget.setColumnWidth(0, self.tableWidget.columnWidth(0) + self.row_height)
        desired_width = self.tableWidget.columnWidth(0) + self.tableWidget.columnWidth(1) + self.tableWidget.columnWidth(2) + 4
        self.tableWidget.setMinimumWidth(min(desired_width, self.tableWidget.maximumWidth()))
        if self.tableWidget.rowCount() > 4:
            desired_height = self.tableWidget.rowCount() * self.tableWidget.rowHeight(0) \
                             + self.tableWidget.horizontalHeader().height() + 4
            self.tableWidget.setMinimumHeight(min(desired_height, get_screen_height(self.tableWidget) * 0.8))
        self.adjustSize()

    @QtCore.Slot(int)
    def update_status_view(self, row):
        if self._statuses[row][0] is Status.PROGRESS:
            icon = ProgressIndicator(self)
            icon.setMaximumSize(QtCore.QSize(self.row_height * 0.75, self.row_height * 0.75))
            icon.setAnimationDelay(70)
            icon.startAnimation()
        else:
            if self._statuses[row][0] is Status.OK:
                item_name = "dialog-ok"
            elif self._statuses[row][0] is Status.ERROR:
                item_name = "edit-delete-remove"
            icon = QtWidgets.QLabel()
            icon.setPixmap(get_icon(item_name).pixmap(self.row_height * 0.75, self.row_height * 0.75))
        icon.setToolTip(self._statuses[row][1])
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(icon, alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        layout.setContentsMargins(self.row_height * 0.1, self.row_height * 0.1,
                                  self.row_height * 0.1, self.row_height * 0.1)

        wdgt = WorklogDialog.ClickWidget(self.tableWidget.item(row, 0), self.tableWidget, self)
        wdgt.setLayout(layout)
        self.tableWidget.setCellWidget(row, 0, wdgt)

    @QtCore.Slot()
    def on_resize(self):
        self.tableWidget.resizeRowsToContents()

    @QtCore.Slot()
    def disable_buttons(self):
        self.previous_button.setEnabled(False)
        self.next_button.setEnabled(False)
        self.upload_button.setEnabled(False)
        self.ok_button.setEnabled(False)

    @QtCore.Slot()
    def enable_buttons(self):
        self.ok_button.setEnabled(True)
        self.update_prev_next()

    def update_prev_next(self):
        prev, next_ = self._worklog.prev_next_avail()
        self.previous_button.setEnabled(prev)
        self.next_button.setEnabled(next_)

    @QtCore.Slot()
    def previous(self):
        self.save()
        self._worklog.previous()
        self._focussed = False
        self.update_all()
        self.upload_button.setEnabled(False)

    @QtCore.Slot()
    def next(self):
        self.save()
        self._worklog.next()
        self._focussed = False
        self.update_all()
        self.upload_button.setEnabled(False)

    @QtCore.Slot()
    def upload(self):
        issues = list(map(lambda x: (x[0].split()[0], x[1], x[2]), self._worklog_data[:-1]))
        self.rest.upload(issues, self._worklog.date)
        self.update_statuses()
        self.update_timer.start()

    @QtCore.Slot()
    def cell_changed(self, row, _):
        if self._changing_items:
            return
        self._worklog_data[row][0] = self.tableWidget.item(row, 0).text()
        self.save()
        self.update_all()
        self.upload_button.setEnabled(False)

    @QtCore.Slot()
    def text_edit_changed(self, text, row):
        self._worklog_data[row][1] = text

    @QtCore.Slot()
    def _accept(self):
        self.save()
        self.accept()
