from fime.util import get_icon

try:
    from PySide6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets

from fime.config import Config


class Settings(QtWidgets.QDialog):
    def __init__(self, config: Config, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowTitle("Settings")

        self.config = config

        caption_label = QtWidgets.QLabel()
        caption_label.setText("Settings")
        caption_label.setAlignment(QtCore.Qt.AlignHCenter)

        settings_layout = QtWidgets.QGridLayout()

        jira_url_label = QtWidgets.QLabel()
        jira_url_label.setText("Jira URL")
        settings_layout.addWidget(jira_url_label, 0, 0)
        self.jira_url_edit = QtWidgets.QLineEdit()
        settings_layout.addWidget(self.jira_url_edit, 0, 1)

        jira_token_label = QtWidgets.QLabel()
        jira_token_label.setText("Jira Personal Access Token<br/> see <a href='https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html#UsingPersonalAccessTokens-CreatingPATsinapplication'>here</a> for how to get one")
        jira_token_label.setTextFormat(QtCore.Qt.RichText)
        jira_token_label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        jira_token_label.setOpenExternalLinks(True)
        settings_layout.addWidget(jira_token_label, 1, 0)
        self.jira_token_edit = QtWidgets.QLineEdit()
        settings_layout.addWidget(self.jira_token_edit, 1, 1)

        tray_theme_label = QtWidgets.QLabel()
        tray_theme_label.setText("Tray theme")
        settings_layout.addWidget(tray_theme_label, 2, 0)
        self.tray_theme_combo_box = QtWidgets.QComboBox()
        self.tray_theme_combo_box.addItem("Light")
        self.tray_theme_combo_box.addItem("Dark")
        settings_layout.addWidget(self.tray_theme_combo_box, 2, 1, QtCore.Qt.AlignRight)

        flip_menu_label = QtWidgets.QLabel()
        flip_menu_label.setText("Flip menu")
        settings_layout.addWidget(flip_menu_label, 3, 0)
        self.flip_menu_check_box = QtWidgets.QCheckBox()
        settings_layout.addWidget(self.flip_menu_check_box, 3, 1, QtCore.Qt.AlignRight)

        import_auto_change_task_label = QtWidgets.QLabel()
        import_auto_change_task_label.setText("Automatically select task as active task\nafter task import")
        settings_layout.addWidget(import_auto_change_task_label, 4, 0)
        self.import_auto_change_task_check_box = QtWidgets.QCheckBox()
        settings_layout.addWidget(self.import_auto_change_task_check_box, 4, 1, QtCore.Qt.AlignRight)

        self.ok_button = QtWidgets.QPushButton()
        self.ok_button.setText("OK")
        self.ok_button.setIcon(get_icon("dialog-ok"))
        self.ok_button.pressed.connect(self.accept)
        self.ok_button.setAutoDefault(True)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch(66)
        button_layout.addWidget(self.ok_button, 33)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(caption_label)
        layout.addLayout(settings_layout)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.resize(500, 0)
        self.accepted.connect(self._accepted)

    def showEvent(self, _):
        self.jira_url_edit.setText(self.config.jira_url)
        self.jira_token_edit.setText(self.config.jira_token)
        self.tray_theme_combo_box.setCurrentText(self.config.tray_theme.capitalize())
        self.flip_menu_check_box.setChecked(self.config.flip_menu)
        self.import_auto_change_task_check_box.setChecked(self.config.import_auto_change_task)

    def _accepted(self):
        self.config.jira_url = self.jira_url_edit.text()
        self.config.jira_token = self.jira_token_edit.text()
        self.config.tray_theme = self.tray_theme_combo_box.currentText()
        self.config.flip_menu = self.flip_menu_check_box.isChecked()
        self.config.import_auto_change_task = self.import_auto_change_task_check_box.isChecked()
        self.config.save()


# only for dev/debug
if __name__ == "__main__":
    QtCore.QCoreApplication.setApplicationName("fime")
    app = QtWidgets.QApplication()
    cfg = Config()
    settings = Settings(cfg, None)
    settings.show()
    app.exec()
