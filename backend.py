from pathlib import Path

from PySide6.QtCore import QObject, QStandardPaths, Slot
from PySide6.QtGui import QColor
from PySide6.QtQml import QmlElement
from tinycss2.color3 import RGBA, parse_color

QML_IMPORT_NAME = "backend.kgradience"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class Backend(QObject):
    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._rules = self.load()

    def load(self) -> dict[str, str | QColor]:
        loc = QStandardPaths.StandardLocation.ConfigLocation
        path = QStandardPaths.writableLocation(loc)
        gtkPath = Path(path) / 'gtk-4.0' / 'gtk.css'
        prefix = '@define-color'
        result = {}
        with open(gtkPath, 'r') as config:
            for line in config:
                line: str
                line = line.strip()
                if not line.startswith(prefix):
                    continue
                tokens = (line.removeprefix(prefix)
                              .removesuffix(';')
                              .strip().split())
                name, rule = tokens[0], ' '.join(tokens[1:])
                if not rule.startswith('@'):
                    rule = self._stringToColor(rule)
                result[name] = rule
        return result

    def _stringToColor(self, data: str) -> QColor:
        c = parse_color(data)
        if isinstance(c, RGBA):
            return QColor.fromRgbF(c.red, c.green, c.blue, c.alpha)
        return QColor()

    @Slot(str, result=str)
    def getRuleText(self, name: str) -> str:
        rule = self._rules[name]
        if isinstance(rule, QColor):
            return rule.name(QColor.NameFormat.HexArgb)
        return rule

    @Slot(str, result=QColor)
    def getColor(self, color: str) -> QColor:
        if isinstance(color, QColor):
            return color
        rule = self._rules.get(color.removeprefix('@'))
        assert rule is not None
        return self.getColor(rule)
