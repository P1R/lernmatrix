# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LernMatrix.ui'
#
# Created: Thu Feb 27 21:45:11 2014
#      by: PyQt4 UI code generator 4.10.3
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

#Here is the matrix i want to show
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

rows = "ABCD"
choices = ['apple', 'orange', 'banana']

class Model(QtCore.QAbstractTableModel):
    def __init__(self):
        super(Model, self).__init__()
        self.table = [[row, choices[0],choices[1], choices[2]] for row in rows]
    def rowCount(self, index=QtCore.QModelIndex()):
        return len(self.table)
    def columnCount(self, index=QtCore.QModelIndex()):
        return 4
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.table[index.row()][index.column()]
    def setData(self, index, role, value):
        if role == QtCore.Qt.DisplayRole:
            self.table[index.row()][index.column()] = value

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(708, 557)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(440, 20, 258, 227))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 361, 229))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableView = QtGui.QTableView(self.layoutWidget1)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_2.addWidget(self.tableView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 320, 175, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.model = Model()

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.MostrarMem)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tableView.reset)
        #QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.slot2)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textBrowser.clear)
        #QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.slot3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_3.setText(_translate("Form", "PushButton", None))
        self.pushButton.setText(_translate("Form", "Mostrar Memoria", None))
        self.pushButton_4.setText(_translate("Form", "Generar Memoria", None))
        self.pushButton_2.setText(_translate("Form", "Limpiar", None))
    def MostrarMem(self):
        self.tableView.setModel(self.model)
        print "hola"
if __name__ == "__main__":
    import sys;
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
