from PySide6.QtCore import Property, QObject, Slot
from PySide6.QtQml import QmlElement


@QmlElement
class Backend(QObject):
    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)