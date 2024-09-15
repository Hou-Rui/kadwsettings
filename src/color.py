from PySide6.QtCore import Property, QObject, Signal
from PySide6.QtGui import QColor


class Resolver(QObject):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def resolve(self, _: str) -> QColor:
        return NotImplemented


class Rule(QObject):
    nameChanged = Signal()
    colorChanged = Signal()
    paletteChanged = Signal()

    def __init__(self, parent: Resolver, name: str,
                 code: str = 'transparent', isPalette: bool = False) -> None:
        super().__init__(parent)
        self._parent = parent
        self._name = name
        self._code = code
        self._isPalette = isPalette

    @Property(str, notify=nameChanged)
    def name(self) -> str:
        return self._name

    @Property(str, notify=colorChanged)
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, newCode: str) -> None:
        if newCode != self._code:
            self._code = newCode
            self.colorChanged.emit()

    @Property(QColor, notify=colorChanged)
    def color(self) -> QColor:
        return self._parent.resolve(self._code)

    @Property(bool, notify=paletteChanged)
    def isPalette(self) -> bool:
        return self._isPalette
