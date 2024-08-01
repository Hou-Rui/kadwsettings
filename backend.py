from dataclasses import dataclass
from pathlib import Path

from PySide6.QtCore import QObject, QStandardPaths, Slot
from PySide6.QtGui import QColor
from PySide6.QtQml import QmlElement
from tinycss2.color3 import RGBA, parse_color

QML_IMPORT_NAME = "backend.kgradience"
QML_IMPORT_MAJOR_VERSION = 1


@dataclass
class ColorRule:
    name: str
    code: str


@QmlElement
class Backend(QObject):
    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._rules, self._custom = self.load()

    def load(self) -> tuple[dict[str, ColorRule], str]:
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
                result[name] = ColorRule(name, rule)
        return result, custom

    def _colorFromCode(self, data: str) -> QColor:
        if isinstance(c := parse_color(data), RGBA):
            return QColor.fromRgbF(c.red, c.green, c.blue, c.alpha)
        return QColor()

    @Slot(str, result=str)
    def getCode(self, name: str) -> str:
        if rule := self._rules[name]:
            return rule.code
        return ''

    @Slot(str, result=QColor)
    def getColor(self, name: str) -> QColor:
        code: str = self.getCode(name)
        if not code.startswith('@'):
            return self._colorFromCode(code)
        if rule := self._rules.get(code.removeprefix('@')):
            return self.getColor(rule)
        return QColor()
