import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication

from preset import Preset

if __name__ == "__main__":
    app = QApplication()
    app.setApplicationName("KAdwSettings")
    app.setDesktopFileName("KAdwSettings")
    app.setApplicationDisplayName("KDE Adwaita Settings")

    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).parent / 'main.qml'
    engine.load(QUrl.fromLocalFile(qml_file))
    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code)
