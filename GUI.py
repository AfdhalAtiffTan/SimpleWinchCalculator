# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(798, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 10, 781, 151))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_1 = QtGui.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_1)
        self.lineEdit_2 = QtGui.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.formLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 240, 781, 311))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_5 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_12 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_11 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_11)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_5 = QtGui.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtGui.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        self.lineEdit_7 = QtGui.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_7)
        self.lineEdit_8 = QtGui.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_8)
        self.lineEdit_9 = QtGui.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_9)
        self.lineEdit_10 = QtGui.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_10)
        self.lineEdit_11 = QtGui.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_11)
        self.lineEdit_12 = QtGui.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEdit_12)
        self.lineEdit_13 = QtGui.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEdit_13)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 169, 781, 61))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        MainWindow.setTabOrder(self.lineEdit_8, self.lineEdit_9)
        MainWindow.setTabOrder(self.lineEdit_9, self.lineEdit_10)
        MainWindow.setTabOrder(self.lineEdit_10, self.lineEdit_11)
        MainWindow.setTabOrder(self.lineEdit_11, self.lineEdit_12)
        MainWindow.setTabOrder(self.lineEdit_12, self.lineEdit_13)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Winch Calculator", None))
        self.label.setText(_translate("MainWindow", "Maximum Final Motor Output Torque (Nm)", None))
        self.label_2.setText(_translate("MainWindow", "Motor RPM (rev/min)", None))
        self.label_3.setText(_translate("MainWindow", "Minimum Drum Diameter (full unwound) (m)", None))
        self.label_4.setText(_translate("MainWindow", "Maximum Drum Diameter (full wound) (m)", None))
        self.lineEdit_1.setText(_translate("MainWindow", "100", None))
        self.lineEdit_2.setText(_translate("MainWindow", "100", None))
        self.lineEdit_3.setText(_translate("MainWindow", "0.075", None))
        self.lineEdit_4.setText(_translate("MainWindow", "0.15", None))
        self.label_5.setText(_translate("MainWindow", "Minimum Cable Tension (N)", None))
        self.label_6.setText(_translate("MainWindow", "Maximum Cable Tension (N)", None))
        self.label_12.setText(_translate("MainWindow", "Minimum Cable Tension (kg)", None))
        self.label_13.setText(_translate("MainWindow", "Minimum Cable Tension (kg)", None))
        self.label_7.setText(_translate("MainWindow", "Power Output (W)", None))
        self.label_8.setText(_translate("MainWindow", "Minimum Radius (m)", None))
        self.label_9.setText(_translate("MainWindow", "Maximum Radius (m)", None))
        self.label_11.setText(_translate("MainWindow", "Minimum Cable Travel Speed (km/h)", None))
        self.label_10.setText(_translate("MainWindow", "Maximum Cable Travel Speed (km/h)", None))
        self.pushButton.setText(_translate("MainWindow", "Calculate", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

