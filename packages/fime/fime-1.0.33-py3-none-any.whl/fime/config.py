from configparser import ConfigParser
from io import StringIO
from pathlib import Path

from loguru import logger

try:
    from PySide6 import QtCore
except ImportError:
    from PySide2 import QtCore


def dequotify(string):
    if string.startswith(('"', "'")) and string.endswith(('"', "'")):
        return string[1:-1]
    else:
        return string


class Config:
    def __init__(self):
        self._configparser = ConfigParser()
        config_dir_path = Path(QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.AppConfigLocation))
        self.config_path = config_dir_path / "fime.conf"
        if self.config_path.exists():
            logger.info(f'reading config file "{self.config_path}"')
            with self.config_path.open(encoding="utf-8") as f:
                config_text = f.read()
            config_text = "[DEFAULT]\n" + config_text
            self._configparser.read_string(config_text)

    def save(self):
        logger.info(f'writing config file "{self.config_path}"')
        config_str = StringIO()
        self._configparser.write(config_str)
        # do not conform to configparser's stupid section requirement
        config_str = "\n".join(config_str.getvalue().splitlines()[1:])
        with self.config_path.open("w", encoding="utf-8") as f:
            f.write(config_str)

    @property
    def jira_url(self):
        return dequotify(self._configparser.get("DEFAULT", "jira_url", fallback=""))

    @jira_url.setter
    def jira_url(self, value):
        self._configparser["DEFAULT"]["jira_url"] = f'"{value}"'

    @property
    def jira_token(self):
        return dequotify(self._configparser.get("DEFAULT", "jira_token", fallback=""))

    @jira_token.setter
    def jira_token(self, value):
        self._configparser["DEFAULT"]["jira_token"] = f'"{value}"'

    @property
    def tray_theme(self):
        val = dequotify(self._configparser.get("DEFAULT", "tray_theme", fallback="dark")).lower()
        return val if val in ["light", "dark"] else "dark"

    @tray_theme.setter
    def tray_theme(self, value):
        value = value.lower()
        if value not in ["light", "dark"]:
            raise RuntimeError('config key "tray_theme" can only be set to "light" or "dark"')
        self._configparser["DEFAULT"]["tray_theme"] = f'"{value}"'

    @property
    def flip_menu(self):
        val = dequotify(self._configparser.get("DEFAULT", "flip_menu", fallback="no")).lower()
        return val in ["yes", "true", "1"]

    @flip_menu.setter
    def flip_menu(self, value):
        if type(value) is not bool:
            raise RuntimeError('config key "flip_menu" must be a bool')
        self._configparser["DEFAULT"]["flip_menu"] = f'"{value}"'

    @property
    def import_auto_change_task(self):
        val = dequotify(self._configparser.get("DEFAULT", "import_auto_change_task", fallback="no")).lower()
        return val in ["yes", "true", "1"]

    @import_auto_change_task.setter
    def import_auto_change_task(self, value):
        if type(value) is not bool:
            raise RuntimeError('config key "import_auto_change_task" must be a bool')
        self._configparser["DEFAULT"]["import_auto_change_task"] = f'"{value}"'
