import json
from pathlib import Path
from typing import Iterator, TextIO, override

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
    nameChanged = Signal()
    customChanged = Signal()
    schemaChanged = Signal()
    errorHappened = Signal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._schema = Schema(self)
        self._name = self.tr("Unnamed Preset")
        self._rules: dict[str, Rule] = {}
        self._custom: str = ''
        self._palette: list[str] = []
        self._shades: int = 0
        self._initRules()
        self.loadCss()

    def _initRules(self) -> None:
        data = self._schema.data()
        for group in data['groups']:
            for variable in group['variables']:
                name = variable['name']
                self._rules[name] = Rule(self, name)
        for palette in data['palette']:
            prefix: str = palette['prefix']
            shades: int = palette['n_shades']
            self._palette.append(prefix)
            self._shades = max(self._shades, shades)
            for n in range(1, shades + 1):
                name = f"{prefix}{n}"
                self._rules[name] = Rule(self, name, isPalette=True)

    @Slot()
    def loadCss(self) -> None:
        with open(self._cssPath(), 'r') as config:
            for raw in config:
                line = raw.strip()
                if line.startswith(PREFIX_INTERNAL):
                    presetPrefix = f'{PREFIX_INTERNAL} Preset:'
                    if line.startswith(presetPrefix):
                        self._name = (line.removeprefix(presetPrefix)
                                          .removesuffix('*/')
                                          .strip())
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

    def _writeInternal(self, output: TextIO, text: str) -> None:
        output.write(f'{PREFIX_INTERNAL} {text} */\n')

    @Slot()
    def saveCss(self) -> None:
        with open(self._cssPath(), 'w') as config:
            # preset info
            self._writeInternal(config, f'Preset: {self.name}')
            # named colors / palette
            self._writeInternal(config, 'Named Colors')
            for rule in self._rules.values():
                line = f'{PREFIX_DEFINE_COLOR} {rule.name} {rule.code};\n'
                config.write(line)
            # custom styles
            self._writeInternal(config, 'Custom Styles')
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
                data = json.load(input)
                for name, code in _genRules(data):
                    self._rules[name].code = code  # type: ignore
                if custom := data.get('custom_css'):
                    if customGtk4 := custom.get('gtk4'):
                        self._custom = customGtk4
        except (ValueError, KeyError, AssertionError) as e:
            msg = self.tr('Load preset failed: {}'.format(e))
            self.errorHappened.emit(msg)

    @Slot(str)
    def saveJson(self, path: str) -> None:
        result = {
            "name": self._name,
            "variables": {
                name: rule._code
                for name, rule in self._rules.items() if not rule._isPalette
            },
            "palette": {
                prefix: {
                    str(n): self._rules[f'{prefix}{n}']._code
                    for n in range(1, self._shades + 1)
                }
                for prefix in self._palette
            },
            "custom_css": {
                "gtk4": self._custom
            },
        }
        try:
            with open(QUrl(path).path(), 'w') as output:
                json.dump(result, output, indent=2)
        except (ValueError, KeyError) as e:
            msg = self.tr('Save preset failed: {}'.format(e))
            self.errorHappened.emit(msg)

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

    @Property(str, notify=nameChanged)
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, newName: str) -> None:
        self._name = newName

    @Property('QVariant', notify=schemaChanged)
    def schema(self) -> dict:
        return self._schema.data()

    @Property(str, notify=customChanged)
    def custom(self) -> str:
        return self._custom

    @custom.setter
    def custom(self, newCustom: str) -> None:
        self._custom = newCustom
