# coding=utf-8
import sys

from PySide6.QtWidgets import QApplication

sys.path.append('cloud')
sys.path.append('cloud/business')
sys.path.append('cloud/ui')
sys.path.append('cloud/utils')


class MainStart:
    def __init__(self):
        from cloud.business.StartMenu import StartMainMenu
        self.start_main_menu = StartMainMenu(app)
        self.start_main_menu.show()
        self.start_main_menu.change_to_windows_vista()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_start = MainStart()
    app.exit(app.exec())
