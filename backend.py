from pathlib import Path
from typing import Any, override

from PySide6.QtCore import Property, QObject, QStandardPaths, Signal, Slot
from PySide6.QtGui import QColor
from PySide6.QtQml import QmlElement, QmlSingleton
from tinycss2.color3 import RGBA, parse_color

from color import BackendBase, ColorRule

QML_IMPORT_NAME = "backend.kgradience"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
@QmlSingleton
class Backend(BackendBase, QObject):
    customChanged: Any = Signal()

    def __init__(self, parent=None) -> None:
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
                    custom += raw
                    continue
                tokens = (line.removeprefix(prefix)
                              .removesuffix(';')
                              .strip().split())
                name, rule = tokens[0], ' '.join(tokens[1:])
                result[name] = ColorRule(name, rule, self)
        return result, custom

    @override
    def resolveColor(self, code: str) -> QColor:
        code = code.strip()
        if not code.startswith('@'):
            if isinstance(c := parse_color(code), RGBA):
                return QColor.fromRgbF(c.red, c.green, c.blue, c.alpha)
            return QColor()
        if next := self._rules.get(code.removeprefix('@')):
            return self.resolveColor(next._code)
        return QColor()

    @Slot(str, result=ColorRule)
    def getColorRule(self, name: str) -> ColorRule | None:
        return self._rules.get(name)

    def setCustom(self, custom: str) -> None:
        self._custom = custom

    @Property(str, fset=setCustom, notify=customChanged)
    def custom(self) -> str:
        return self._custom
