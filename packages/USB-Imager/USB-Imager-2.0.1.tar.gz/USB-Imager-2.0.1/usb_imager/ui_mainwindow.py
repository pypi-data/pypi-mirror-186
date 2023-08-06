# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 175)
        MainWindow.setMinimumSize(QSize(500, 0))
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_open = QPushButton(self.centralwidget)
        self.pushButton_open.setObjectName(u"pushButton_open")

        self.horizontalLayout.addWidget(self.pushButton_open)

        self.comboBox_devices = QComboBox(self.centralwidget)
        self.comboBox_devices.setObjectName(u"comboBox_devices")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_devices.sizePolicy().hasHeightForWidth())
        self.comboBox_devices.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.comboBox_devices)

        self.comboBox_buffers = QComboBox(self.centralwidget)
        self.comboBox_buffers.setObjectName(u"comboBox_buffers")

        self.horizontalLayout.addWidget(self.comboBox_buffers)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_source = QLabel(self.centralwidget)
        self.label_source.setObjectName(u"label_source")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_source.sizePolicy().hasHeightForWidth())
        self.label_source.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.label_source)

        self.label_srcpath = QLabel(self.centralwidget)
        self.label_srcpath.setObjectName(u"label_srcpath")
        sizePolicy1.setHeightForWidth(self.label_srcpath.sizePolicy().hasHeightForWidth())
        self.label_srcpath.setSizePolicy(sizePolicy1)
        self.label_srcpath.setScaledContents(False)
        self.label_srcpath.setWordWrap(True)
        self.label_srcpath.setMargin(6)

        self.horizontalLayout_2.addWidget(self.label_srcpath)

        self.pushButton_cancel = QPushButton(self.centralwidget)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)

        self.pushButton_write = QPushButton(self.centralwidget)
        self.pushButton_write.setObjectName(u"pushButton_write")

        self.horizontalLayout_2.addWidget(self.pushButton_write)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 30))
        self.menubar.setLayoutDirection(Qt.RightToLeft)
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuInfo.addAction(self.actionAbout)
        self.menuInfo.addAction(self.actionAboutQt)

        self.retranslateUi(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"AboutQt", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"Select Image", None))
        self.label_source.setText(QCoreApplication.translate("MainWindow", u"Image files:", None))
        self.label_srcpath.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_write.setText(QCoreApplication.translate("MainWindow", u"Write", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

