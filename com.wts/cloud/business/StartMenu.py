from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QDialog, QMainWindow, QStyleFactory

from ..ui.about_me import Ui_Dialog as About_me_Ui_Dialog
from ..ui.contact_us import Ui_Dialog as Contact_us_Ui_Dialog
from ..ui.Operate_ShouCe import Ui_Dialog as Operate_ShouCe_Ui_Dialog
from ..ui.register import Ui_Dialog as Register_Ui_Dialog
from ..ui.YunQi_MainWindow import Ui_MainWindow


class StartMainMenu(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.ui_main_window = Ui_MainWindow()
        self.ui_main_window.setupUi(self)

        self.app = app

        # 退出系统
        self.ui_main_window.action_exit.triggered.connect(self.app.exit)

        # 切换到MacOS风格
        self.ui_main_window.actionMacOS.triggered.connect(self.change_to_windows_vista)
        # 切换到Windows风格
        self.ui_main_window.actionWindows.triggered.connect(self.change_to_window)
        # 切换到Fusion风格
        self.ui_main_window.actionFusion.triggered.connect(self.change_to_fusion)

        # 操作手册
        self.ui_main_window.action_7.triggered.connect(self.about_me)
        # 注册
        self.ui_main_window.action_5.triggered.connect(self.register_page)
        # 联系我们
        self.ui_main_window.action_6.triggered.connect(self.contact_us)
        # 关于我们
        self.ui_main_window.action_4.triggered.connect(self.operate_shou_ce)

    @Slot()
    def change_to_windows_vista(self):
        self.app.setStyle(QStyleFactory.create("WindowsVista"))

    @Slot()
    def change_to_window(self):
        self.app.setStyle(QStyleFactory.create("Windows"))

    @Slot()
    def change_to_fusion(self):
        self.app.setStyle(QStyleFactory.create("Fusion"))

    @Slot()
    def register_page(self):
        """
        打开注册页
        :return:
        """
        dialog = QDialog()
        register = Register_Ui_Dialog()
        register.setupUi(dialog)
        # 关于我们窗口关闭(以下2中槽传参样例)
        # about.pushButton_about_me.clicked.connect(functools.partial(self.about_me_close, dialog_about))
        register.pushButton.clicked.connect(self.register_close)
        register.pushButton_2.clicked.connect(lambda: self.register_save(dialog=dialog))
        # 直接隐藏界面整个头部内容
        # dialog.setWindowFlags(Qt.FramelessWindowHint)
        dialog.setWindowFlags(Qt.WindowCloseButtonHint)
        dialog.exec()

    @Slot()
    def register_close(self):
        """
        todo 关闭注册页和主窗口(如果已经注册过，并且注册码有效，则只关闭dialog窗口，不退出程序)
        :return:
        """
        self.app.exit()

    @Slot()
    def register_save(self, dialog):
        """
        todo 注册码保存注册，并关闭注册页(注册程序。如果注册码不合规，则提示，不关闭dialog。如果合规则，注册成功，并关闭dialog)
        :param dialog:
        :return:
        """
        dialog.close()

    @Slot()
    def contact_us(self):
        """
        打开联系我们
        :return:
        """
        dialog = QDialog()
        contact_us = Contact_us_Ui_Dialog()
        contact_us.setupUi(dialog)
        # 关于我们窗口关闭(以下2中槽传参样例)
        # about.pushButton_about_me.clicked.connect(functools.partial(self.about_me_close, dialog_about))
        contact_us.pushButton.clicked.connect(dialog.close)
        # 直接隐藏界面整个头部内容
        dialog.setWindowFlags(Qt.WindowCloseButtonHint)
        dialog.exec()

    @Slot()
    def operate_shou_ce(self):
        """
        打开操作手册
        :return:
        """
        dialog = QDialog()
        operate_shou_ce = Operate_ShouCe_Ui_Dialog()
        operate_shou_ce.setupUi(dialog)
        # 关于我们窗口关闭(以下2中槽传参样例)
        # about.pushButton_about_me.clicked.connect(functools.partial(self.about_me_close, dialog_about))
        operate_shou_ce.pushButton.clicked.connect(dialog.close)
        # 直接隐藏界面整个头部内容
        dialog.setWindowFlags(Qt.WindowCloseButtonHint)
        dialog.exec()

    @Slot()
    def about_me(self):
        """
        打开关于我们
        :return:
        """
        dialog_about = QDialog()
        about = About_me_Ui_Dialog()
        about.setupUi(dialog_about)
        # 关于我们窗口关闭(以下2中槽传参样例)
        # about.pushButton_about_me.clicked.connect(functools.partial(self.about_me_close, dialog_about))
        about.pushButton_about_me.clicked.connect(dialog_about.close)
        # 直接隐藏界面整个头部内容
        dialog_about.setWindowFlags(Qt.WindowCloseButtonHint)
        dialog_about.exec()
