import sys

from PyQt6.QtWidgets import QApplication

from domain.app import App
from ui.main_window import MainWindow

if __name__ == "__main__":
    app = App()

    qt_app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    sys.exit(qt_app.exec())

