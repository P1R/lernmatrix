# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LernMatrix.ui'
#
# Created: Fri Feb 28 01:20:19 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy as np 
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
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

Y=[0]*7
for i in range(7):
	Y[i]=[0]*15

entradat = open("db.data", "r")
dbanimales = np.array([ map( int, linea.split() ) for linea in entradat ])
z = len(dbanimales) 
print z
entrada1 = open("xy1.data", "r")
xy1 = np.array([ map( int, linea.split() ) for linea in entrada1 ])

entrada2 = open("xy2.data", "r")
xy2 = np.array([ map( int, linea.split() ) for linea in entrada2 ])

entrada3 = open("xy3.data", "r")
xy3 = np.array([ map( int, linea.split() ) for linea in entrada3 ])

entrada4 = open("xy4.data", "r")
xy4 = np.array([ map( int, linea.split() ) for linea in entrada4 ])

entrada5 = open("xy5.data", "r")
xy5 = np.array([ map( int, linea.split() ) for linea in entrada5 ])

entrada6 = open("xy6.data", "r")
xy6 = np.array([ map( int, linea.split() ) for linea in entrada6 ])

entrada7 = open("xy7.data", "r")
xy7 = np.array([ map( int, linea.split() ) for linea in entrada7 ])

y1 = np.r_[1, 0, 0, 0, 0, 0, 0]
y2 = np.r_[0, 1, 0, 0, 0, 0, 0]
y3 = np.r_[0, 0, 1, 0, 0, 0, 0]
y4 = np.r_[0, 0, 0, 1, 0, 0, 0]
y5 = np.r_[0, 0, 0, 0, 1, 0, 0]
y6 = np.r_[0, 0, 0, 0, 0, 1, 0]
y7 = np.r_[0, 0, 0, 0, 0, 0, 1]

#~ entradam = open("memoria.data", "r")
#~ memoria = np.array([ map( int, linea.split() ) for linea in entradam ]) 

class Model(QtCore.QAbstractTableModel):
    def __init__(self):
        super(Model, self).__init__()
        #self.table = [[row, choices] for row in rows]
        self.table = Y
    def rowCount(self, index=QtCore.QModelIndex()):
        return 7
    def columnCount(self, index=QtCore.QModelIndex()):
        return 15
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
        Form.resize(712, 494)
        Form.setMinimumSize(QtCore.QSize(712, 494))
        Form.setMaximumSize(QtCore.QSize(712, 494))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 370, 301, 111))
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
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 671, 341))
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
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        
        self.retranslateUi(Form)
        Form.setWindowTitle(_translate("Form", "QtLernMatrix 0.2", None))
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.MostrarMem)
        #~ QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.GenMem)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.GenMem)
        #~ QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.GenMem)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_3.setText(_translate("Form", "Calcular Porcentaje", None))
        self.pushButton_4.setText(_translate("Form", "Buscar Clase", None))
        self.pushButton.setText(_translate("Form", "Mostrar Memoria", None))
        self.pushButton_2.setText(_translate("Form", "Generar Memoria", None))
    def GenMem(self):
		entradam = open("memoria.data", "r")
		memoria = np.array([ map( int, linea.split() ) for linea in entradam ])
		for i in xrange(0, 41):
		 for j in xrange(0, 15): 
		  if xy1[i][j] == 1: 
		   memoria [0][j] = 1 + memoria [0][j]
		  elif  xy1[i][j] == 0:
		   memoria [0][j] = -1 + memoria [0][j]   
		for i in xrange(0, 20):
		 for j in xrange(0, 15): 
		  if xy2[i][j] == 1: 
		   memoria [1][j] = 1 + memoria [1][j]
		  elif  xy2[i][j] == 0:
		   memoria [1][j] = -1 + memoria [1][j]
		for i in xrange(0, 5):
		 for j in xrange(0, 15): 
		  if xy3[i][j] == 1: 
		   memoria [2][j] = 1 + memoria [2][j]
		  elif  xy3[i][j] == 0:
		   memoria [2][j] = -1 + memoria [2][j]
		for i in xrange(0, 13):
		 for j in xrange(0, 15): 
		  if xy4[i][j] == 1: 
		   memoria [3][j] = 1 + memoria [3][j]
		  elif  xy4[i][j] == 0:
		   memoria [3][j] = -1 + memoria [3][j]
		for i in xrange(0, 4):
		 for j in xrange(0, 15): 
		  if xy5[i][j] == 1: 
		   memoria [4][j] = 1 + memoria [4][j]
		  elif  xy5[i][j] == 0:
		   memoria [4][j] = -1 + memoria [4][j]
		for i in xrange(0, 8):
		 for j in xrange(0, 15): 
		  if xy6[i][j] == 1: 
		   memoria [5][j] = 1 + memoria [5][j]
		  elif  xy6[i][j] == 0:
		   memoria [5][j] = -1 + memoria [5][j]
		for i in xrange(0, 10):
		 for j in xrange(0, 15): 
		  if xy7[i][j] == 1: 
		   memoria [6][j] = 1 + memoria [6][j]
		  elif  xy7[i][j] == 0:
		   memoria [6][j] = -1 + memoria [6][j]

		for i in range(7):
			for j in range(15):
				Y[i][j]=int(memoria[i][j])
		print Y
		self.model = Model()
		self.tableView.setModel(self.model)
    def MostrarMem(self):
		entradam = open("memoria.data", "r")
		memoria = np.array([ map( int, linea.split() ) for linea in entradam ])
		for i in range(7):
			for j in range(15):
				Y[i][j]=int(memoria[i][j])
		print Y
		self.model = Model()
		self.tableView.setModel(self.model)
		       
if __name__ == "__main__":
    import sys;
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
