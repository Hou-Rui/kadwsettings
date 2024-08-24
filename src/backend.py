from pathlib import Path
from typing import Any, override

from PySide6.QtCore import Property, QObject, QStandardPaths, Signal, Slot
from PySide6.QtGui import QColor
from PySide6.QtQml import QmlElement, QmlSingleton
from tinycss2.color3 import RGBA, parse_color

from color import BackendBase, ColorRule

QML_IMPORT_NAME = "backend.kadwsettings"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
@QmlSingleton
class Backend(BackendBase, QObject):
    customChanged: Any = Signal()
    defineColorPrefix = '@define-color'
    internalPrefix = f'/* KAdwSettings:'

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._rules, self._custom = self.load()

    def load(self) -> tuple[dict[str, ColorRule], str]:
        result, custom = {}, ''
        with open(self.getCssPath(), 'r') as config:
            for raw in config:
                line = raw.strip()
                if line.startswith(self.internalPrefix):
                    continue
                if not line.startswith(self.defineColorPrefix):
                    custom += raw
                    continue
                tokens = (line.removeprefix(self.defineColorPrefix)
                              .removesuffix(';')
                              .strip().split())
                name, rule = tokens[0], ' '.join(tokens[1:])
                result[name] = ColorRule(name, rule, self)
        return result, custom

    @Slot()
    def save(self) -> None:
        with open(self.getCssPath(), 'w') as config:
            config.write(f'{self.internalPrefix} Named Colors */\n')
            for rule in self._rules.values():
                line = f'{self.defineColorPrefix} {rule.name} {rule.code};\n'
                config.write(line)
            config.write(f'{self.internalPrefix} Custom Styles */\n')
            config.write(f'{self.custom}\n')

    def getCssPath(self) -> Path:
        loc = QStandardPaths.StandardLocation.ConfigLocation
        path = QStandardPaths.writableLocation(loc)
        return Path(path) / 'gtk-4.0' / 'gtk.css'

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

    @Property(str, notify=customChanged)
    def custom(self) -> str:
        return self._custom

    @custom.setter
    def custom(self, custom: str) -> None:
        self._custom = custom
