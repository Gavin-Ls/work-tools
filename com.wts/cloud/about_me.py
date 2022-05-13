# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_me.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(400, 200)
        Dialog.setMinimumSize(QSize(400, 200))
        Dialog.setMaximumSize(QSize(400, 200))
        font = QFont()
        font.setFamilies([u"Heiti SC"])
        font.setBold(True)
        Dialog.setFont(font)
        Dialog.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/root/resources/image/title_main.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(61, 71))
        self.label.setPixmap(QPixmap(u":/root/resources/image/title_main.png"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Heiti SC"])
        font1.setBold(False)
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_6)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_about_me = QPushButton(Dialog)
        self.pushButton_about_me.setObjectName(u"pushButton_about_me")
        self.pushButton_about_me.setMinimumSize(QSize(45, 45))
        self.pushButton_about_me.setMaximumSize(QSize(45, 45))
        self.pushButton_about_me.setFont(font1)
        self.pushButton_about_me.setStyleSheet(u"border-image: url(:/root/resources/image/close_3.svg);")

        self.horizontalLayout_2.addWidget(self.pushButton_about_me)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5173\u4e8e\u6211\u4eec", None))
#if QT_CONFIG(statustip)
        Dialog.setStatusTip(QCoreApplication.translate("Dialog", u"\u5173\u4e8e\u6211\u4eec", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Dialog.setWhatsThis(QCoreApplication.translate("Dialog", u"\u5173\u4e8e\u6211\u4eec", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u4e91\u4f01\u670d\u52a1\u7ba1\u7406\u7cfb\u7edf</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u4f5c\u8005\uff1a</span><span style=\" color:#575757;\">\u65e0\u540d</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u7248\u672c\uff1a</span><span style=\" color:#575757;\">V1.0</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u5f00\u53d1\u65f6\u95f4\uff1a</span><span style=\" color:#575757;\">2022/5/10</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u7248\u6743\uff1a</span><span style=\" color:#575757;\">\u53ef\u514d\u8d39\u8bd5\u7528\uff0c\u5982\u9700\u957f\u671f\u4f7f\u7528\uff0c\u8bf7\u8054\u7cfb\u4f5c\u8005</span></p></body></html>", None))
        self.pushButton_about_me.setText("")
    # retranslateUi

