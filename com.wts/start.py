# coding=utf-8
import sys

from PySide6.QtWidgets import QApplication

sys.path.append('cloud')


class MainStart:
    def __init__(self):
        from cloud.StartMenu import StartMainMenu
        self.start_main_menu = StartMainMenu(app)
        self.start_main_menu.show()
        self.start_main_menu.to_macos()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_start = MainStart()
    app.exit(app.exec())
