# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contact_us.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(287, 174)
        font = QFont()
        font.setFamilies([u"Heiti SC"])
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/root/resources/image/title_main.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Heiti SC"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Heiti SC"])
        font2.setBold(True)
        self.label.setFont(font2)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setTextFormat(Qt.AutoText)
        self.label_7.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.verticalLayout_2.addWidget(self.label_8)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(60, 30))
        self.pushButton.setMaximumSize(QSize(60, 30))
        self.pushButton.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(237, 208, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.267045 rgba(239, 206, 55, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:1 rgba(235, 213, 26, 255));")
        icon1 = QIcon()
        icon1.addFile(u":/close/resources/image/close_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8054\u7cfb\u6211\u4eec", None))
#if QT_CONFIG(tooltip)
        Dialog.setToolTip(QCoreApplication.translate("Dialog", u"\u8054\u7cfb\u6211\u4eec", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Dialog.setStatusTip(QCoreApplication.translate("Dialog", u"\u8054\u7cfb\u6211\u4eec", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Dialog.setWhatsThis(QCoreApplication.translate("Dialog", u"\u8054\u7cfb\u6211\u4eec", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u8054  \u7cfb  \u4eba\uff1a", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8054\u7cfb\u7535\u8bdd\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u8054\u7cfb\u90ae\u7bb1\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u8054\u7cfb\u5730\u5740\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u65e0\u540d", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"123456789", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"123456789@163.com", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u6d77", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u5173\u95ed", None))
    # retranslateUi

