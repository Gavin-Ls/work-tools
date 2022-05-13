# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(374, 334)
        Dialog.setMinimumSize(QSize(374, 334))
        Dialog.setMaximumSize(QSize(374, 334))
        font = QFont()
        font.setFamilies([u"Heiti SC"])
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/root/resources/image/title_main.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(False)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(237, 239, 239);")
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(45, 45))
        self.pushButton_2.setMaximumSize(QSize(45, 45))
        self.pushButton_2.setStyleSheet(u"border-image: url(:/root/resources/image/correct_3.svg);")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(45, 45))
        self.pushButton.setMaximumSize(QSize(45, 45))
        self.pushButton.setStyleSheet(u"border-image: url(:/root/resources/image/exit_1.svg);")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u5728\u4e0b\u65b9\u8f93\u5165\u6ce8\u518c\u7801", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
    # retranslateUi

