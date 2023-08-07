import enum

from loguru import logger

try:
    from PySide6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets

# noinspection PyUnresolvedReferences
import fime.icons


def get_screen_height(qobject):
    if hasattr(qobject, "screen"):
        return qobject.screen().size().height()
    else:
        logger.info("unable to detect screen height falling back to default value of 1080")
        return 1080


def get_screen_width(qobject):
    if hasattr(qobject, "screen"):
        return qobject.screen().size().width()
    else:
        logger.info("unable to detect screen width falling back to default value of 1920")
        return 1920


def get_icon(icon_name):
    theme_name = icon_name.replace("-light", "")  # respect system theme
    fallback = QtGui.QIcon(f":/icons/{icon_name}").pixmap(256, 256)
    return QtGui.QIcon.fromTheme(theme_name, fallback)


class EditStartedDetector(QtWidgets.QStyledItemDelegate):
    editStarted = QtCore.Signal()
    editFinished = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)
        editor.editingFinished.connect(self.editFinished)
        self.editStarted.emit()
        return editor


class Status(enum.Enum):
    PROGRESS = enum.auto()
    OK = enum.auto()
    ERROR = enum.auto()
