# coding=utf-8
import sys

from PySide6.QtWidgets import QApplication

sys.path.append('')
sys.path.append('business')
sys.path.append('ui')
sys.path.append('utils')


class MainStart:
    def __init__(self):
        from business.StartMenu import StartMainMenu
        self.start_main_menu = StartMainMenu(app)
        self.start_main_menu.show()
        self.start_main_menu.change_to_windows_vista()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_start = MainStart()
    app.exit(app.exec())
