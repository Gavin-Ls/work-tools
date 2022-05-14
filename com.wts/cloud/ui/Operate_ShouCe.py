# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Operate_ShouCe.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(380, 400)
        Dialog.setMinimumSize(QSize(380, 400))
        Dialog.setMaximumSize(QSize(380, 400))
        font = QFont()
        font.setFamilies([u"Heiti SC"])
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/root/DiVTAnFBWTZFfRV.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser_Operate_ShouCe = QTextBrowser(Dialog)
        self.textBrowser_Operate_ShouCe.setObjectName(u"textBrowser_Operate_ShouCe")
        self.textBrowser_Operate_ShouCe.setStyleSheet(u"#textBrowser_Operate_ShouCe{\n"
"	background-color: rgb(236, 240, 240);\n"
"}")
        self.textBrowser_Operate_ShouCe.setReadOnly(True)
        self.textBrowser_Operate_ShouCe.setOverwriteMode(False)

        self.verticalLayout.addWidget(self.textBrowser_Operate_ShouCe)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(60, 30))
        self.pushButton.setMaximumSize(QSize(60, 30))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(237, 208, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.267045 rgba(239, 206, 55, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:1 rgba(235, 213, 26, 255));")
        icon1 = QIcon()
        icon1.addFile(u":/close/resources/image/close_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u64cd\u4f5c\u624b\u518c", None))
        self.textBrowser_Operate_ShouCe.setDocumentTitle(QCoreApplication.translate("Dialog", u"\u64cd\u4f5c\u624b\u518c", None))
        self.textBrowser_Operate_ShouCe.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><title>\u64cd\u4f5c\u624b\u518c</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Heiti SC'; font-size:18pt; font-weight:700;\">\u529f\u80fd\u4ecb\u7ecd\uff1a</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Heiti SC'; font-size:18pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Heiti S"
                        "C'; font-size:13pt; font-weight:700;\">1\u3001</span><span style=\" font-family:'Heiti SC'; font-size:13pt;\">\u8bbe\u7f6e-&gt;\u98ce\u683c\u8bbe\u7f6e</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Heiti SC'; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Heiti SC'; font-size:13pt; font-weight:700;\">2\u3001</span><span style=\" font-family:'Heiti SC'; font-size:13pt;\">\u8bbe\u7f6e-&gt;\u4e91\u4f01\u5207\u6362</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Heiti SC'; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style="
                        "\" font-family:'Heiti SC'; font-size:13pt; font-weight:700;\">3\u3001</span><span style=\" font-family:'Heiti SC'; font-size:13pt;\">\u5e2e\u52a9-&gt;\u64cd\u4f5c\u624b\u518c</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Heiti SC'; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Heiti SC'; font-size:13pt; font-weight:700;\">4\u3001</span><span style=\" font-family:'Heiti SC'; font-size:13pt;\">\u5e2e\u52a9-&gt;\u6ce8\u518c</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Heiti SC'; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" font-family:'Heiti SC'; font-size:13pt; font-weight:700;\">5\u3001</span><span style=\" font-family:'Heiti SC'; font-size:13pt;\">\u5e2e\u52a9-&gt;\u8054\u7cfb\u6211\u4eec</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Heiti SC'; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Heiti SC'; font-size:13pt; font-weight:700;\">6\u3001</span><span style=\" font-family:'Heiti SC'; font-size:13pt;\">\u5e2e\u52a9-&gt;\u5173\u4e8e\u6211\u4eec</span></p></body></html>", None))
        self.textBrowser_Operate_ShouCe.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u529f\u80fd\u4ecb\u7ecd", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u5173\u95ed", None))
    # retranslateUi

