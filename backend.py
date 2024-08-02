from pathlib import Path
from typing import Any

from PySide6.QtCore import QObject, QStandardPaths, Slot
from PySide6.QtGui import QColor
from PySide6.QtQml import QmlElement, QmlSingleton
from tinycss2.color3 import RGBA, parse_color

QML_IMPORT_NAME = "backend.kgradience"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
@QmlSingleton
class Backend(QObject):
    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._rules, self._custom = self.load()

    def load(self) -> tuple[dict[str, str], str]:
        loc = QStandardPaths.StandardLocation.ConfigLocation
        path = QStandardPaths.writableLocation(loc)
        gtkPath = Path(path) / 'gtk-4.0' / 'gtk.css'
        prefix = '@define-color'
        result, custom = {}, ''
        with open(gtkPath, 'r') as config:
            for raw in config:
                line = raw.strip()
                if not line.startswith(prefix):
                    custom += raw + '\n'
                    continue
                tokens = (line.removeprefix(prefix)
                              .removesuffix(';')
                              .strip().split())
                name, rule = tokens[0], ' '.join(tokens[1:])
                result[name] = rule
        return result, custom

    @Slot(str, result=QColor)
    def colorFromCode(self, code: str) -> QColor:
        if isinstance(c := parse_color(code), RGBA):
            return QColor.fromRgbF(c.red, c.green, c.blue, c.alpha)
        return QColor()

    @Slot(result=str)
    def getCustomStyle(self) -> str:
        return self._custom

    @Slot(str, result=str)
    def getCode(self, name: str) -> str:
        if rule := self._rules.get(name):
            return rule
        return ''

    @Slot(str, str)
    def setCode(self, name: str, code: str) -> None:
        self._rules[name] = code

    @Slot(str, result=QColor)
    def getColor(self, name: str) -> QColor:
        code: str = self.getCode(name)
        if not code.startswith('@'):
            return self.colorFromCode(code)
        return self.getColor(code.removeprefix('@'))
