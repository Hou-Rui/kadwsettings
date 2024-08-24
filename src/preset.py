import json
from pathlib import Path
from typing import Iterator, override

from PySide6.QtCore import (Property, QObject, QStandardPaths, QUrl, Signal,
                            Slot)
from PySide6.QtGui import QColor
from PySide6.QtQml import QmlElement, QmlSingleton
from tinycss2.color3 import RGBA, parse_color

from color import Resolver, Rule
from schema import Schema

QML_IMPORT_NAME = "kadwsettings.backend"
QML_IMPORT_MAJOR_VERSION = 1

PREFIX_DEFINE_COLOR = '@define-color'
PREFIX_INTERNAL = '/* KAdwSettings:'


@QmlElement
@QmlSingleton
class Preset(Resolver, QObject):
    customChanged = Signal()
    schemaChanged = Signal()
    errorHappened = Signal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._schema = Schema(self)
        self._rules: dict[str, Rule] = {}
        self._custom: str = ''
        self._initRules()
        self.loadCss()

    def _initRules(self) -> None:
        def _genNames(data: dict[str, list]) -> Iterator[str]:
            for group in data['groups']:
                for variable in group['variables']:
                    yield variable['name']
            for palette in data['palette']:
                for n in range(1, palette['n_shades'] + 1):
                    yield f"{palette['prefix']}{n}"
        for name in _genNames(self._schema.data()):
            self._rules[name] = Rule(name, 'transparent', self)

    @Slot()
    def loadCss(self) -> None:
        with open(self._cssPath(), 'r') as config:
            for raw in config:
                line = raw.strip()
                if line.startswith(PREFIX_INTERNAL):
                    continue
                if not line.startswith(PREFIX_DEFINE_COLOR):
                    self._custom += raw
                    continue
                tokens = (line.removeprefix(PREFIX_DEFINE_COLOR)
                              .strip().split())
                name, code = tokens[0], ' '.join(tokens[1:])
                if name not in self._rules:
                    print(f"Warning: unknown named color {name}")
                    continue
                self._rules[name].code = code.removesuffix(';')  # type: ignore

    @Slot()
    def saveCss(self) -> None:
        with open(self._cssPath(), 'w') as config:
            config.write(f'{PREFIX_INTERNAL} Named Colors */\n')
            for rule in self._rules.values():
                line = f'{PREFIX_DEFINE_COLOR} {rule.name} {rule.code};\n'
                config.write(line)
            config.write(f'{PREFIX_INTERNAL} Custom Styles */\n')
            config.write(f'{self._custom}\n')

    def _cssPath(self) -> Path:
        loc = QStandardPaths.StandardLocation.ConfigLocation
        path = QStandardPaths.writableLocation(loc)
        return Path(path) / 'gtk-4.0' / 'gtk.css'

    @Slot(str)
    def loadJson(self, path: str) -> None:
        def _genRules(data) -> Iterator[tuple[str, str]]:
            assert isinstance(data, dict)
            assert isinstance(vars := data['variables'], dict)
            for name, code in vars.items():
                assert isinstance(name, str) and isinstance(code, str)
                yield name, code
            assert isinstance(palette := data['palette'], dict)
            for prefix, shades in palette.items():
                assert isinstance(shades, dict)
                for n, code in shades.items():
                    assert isinstance(code, str)
                    yield f'{prefix}{n}', code
        try:
            with open(QUrl(path).path(), 'r') as input:
                for name, code in _genRules(json.load(input)):
                    self._rules[name].code = code  # type: ignore
        except (ValueError, KeyError, AssertionError) as e:
            msg = self.tr('Load preset failed: {}'.format(e))
            self.errorHappened.emit(msg)

    @Slot(str)
    def saveJson(self, path: str) -> None:
        pass

    @override
    def resolve(self, code: str) -> QColor:
        code = code.strip()
        if not code.startswith('@'):
            if isinstance(c := parse_color(code), RGBA):
                return QColor.fromRgbF(c.red, c.green, c.blue, c.alpha)
            return QColor()
        if next := self._rules.get(code.removeprefix('@')):
            return self.resolve(next._code)
        return QColor()

    @Slot(str, result=Rule)
    def rule(self, name: str) -> Rule | None:
        return self._rules.get(name)

    @Property('QVariant', notify=schemaChanged)
    def schema(self) -> dict:
        return self._schema.data()

    @Property(str, notify=customChanged)
    def custom(self) -> str:
        return self._custom

    @custom.setter
    def custom(self, custom: str) -> None:
        self._custom = custom
