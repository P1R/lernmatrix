import sys
from PyQt4 import QtGui, QtCore

rows = "ABCD"
choices = ['apple', 'orange', 'banana']

class Model(QtCore.QAbstractTableModel):
    def __init__(self):
        super(Model, self).__init__()
        self.table = [[row, choices[0]] for row in rows]
    def rowCount(self, index=QtCore.QModelIndex()):
        return len(self.table)
    def columnCount(self, index=QtCore.QModelIndex()):
        return 2
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.table[index.row()][index.column()]
    def setData(self, index, role, value):
        if role == QtCore.Qt.DisplayRole:
            self.table[index.row()][index.column()] = value

class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.model = Model()
        self.table = QtGui.QTableView()
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)
        self.setWindowTitle('Delegate Test')
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    app.exec_()
