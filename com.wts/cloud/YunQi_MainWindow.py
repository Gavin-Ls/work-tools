# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YunQi_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setFamilies([u"Heiti SC"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/root/DiVTAnFBWTZFfRV.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.actionMacOS = QAction(MainWindow)
        self.actionMacOS.setObjectName(u"actionMacOS")
        self.actionMacOS.setFont(font)
        self.actionWindows = QAction(MainWindow)
        self.actionWindows.setObjectName(u"actionWindows")
        self.actionWindows.setFont(font)
        self.actionFusion = QAction(MainWindow)
        self.actionFusion.setObjectName(u"actionFusion")
        self.actionFusion.setFont(font)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_3.setFont(font)
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_4.setFont(font)
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_5.setFont(font)
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_6.setFont(font)
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.action_7.setFont(font)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        icon1 = QIcon()
        icon1.addFile(u":/root/resources/image/exit_1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_exit.setIcon(icon1)
        self.action_exit.setFont(font)
        self.action_exit.setMenuRole(QAction.QuitRole)
        self.action_exit_warn = QAction(MainWindow)
        self.action_exit_warn.setObjectName(u"action_exit_warn")
        self.action_exit_warn.setCheckable(True)
        self.action_exit_warn.setChecked(True)
        icon2 = QIcon()
        icon2.addFile(u":/root/resources/image/bell_1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_exit_warn.setIcon(icon2)
        self.action_exit_warn.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(240, 150, 291, 261))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setFont(font)
        self.menu_2 = QMenu(self.menu)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setFont(font)
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_3.setFont(font)
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_4.setFont(font)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menu_2.addAction(self.actionMacOS)
        self.menu_2.addAction(self.actionWindows)
        self.menu_2.addAction(self.actionFusion)
        self.menu_3.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)
        self.menu_4.addAction(self.action_exit_warn)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e91\u4f01\u670d\u52a1\u7ba1\u7406\u7cfb\u7edf", None))
        self.actionMacOS.setText(QCoreApplication.translate("MainWindow", u"MacOS", None))
        self.actionWindows.setText(QCoreApplication.translate("MainWindow", u"Windows", None))
        self.actionFusion.setText(QCoreApplication.translate("MainWindow", u"Fusion", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u4f01\u5207\u6362", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u624b\u518c", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u6211\u4eec", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u6211\u4eec", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.action_exit_warn.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u65f6\u53d1\u51fa\u8b66\u544a", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Heiti SC'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'.AppleSystemUIFont';\"><br /></p></body></html>", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u98ce\u683c", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf", None))
    # retranslateUi

