from typing import Any

from PySide6.QtCore import Property, QObject, Signal
from PySide6.QtGui import QColor


class BackendBase(QObject):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def resolveColor(self, _: str) -> QColor:
        return NotImplemented


class ColorRule(QObject):
    nameChanged: Any = Signal()
    colorChanged: Any = Signal()

    def __init__(self, name: str, code: str, parent: BackendBase) -> None:
        super().__init__(parent)
        self._name = name
        self._code = code
        self._parent = parent

    def setCode(self, newCode: str) -> None:
        if newCode != self._code:
            self._code = newCode
            self.colorChanged.emit()

    @Property(str, notify=nameChanged)
    def name(self) -> str:
        return self._name

    @Property(str, notify=colorChanged, fset=setCode)
    def code(self) -> str:
        return self._code

    @Property(QColor, notify=colorChanged)
    def color(self) -> QColor:
        return self._parent.resolveColor(self._code)
