# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from newlabel import Ui_NewLabel
from newcircuit import Ui_NewCircuit


class Ui_Form(QtWidgets.QWidget):
	def __init__(self,parent=None):
		super(Ui_Form, self).__init__()
		self.parent = parent
	#def setupUi(self, Form):

		self.setObjectName("Form")
		self.resize(450, 399) #450 399
		self.horizontalLayout = QtWidgets.QHBoxLayout(self)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.tableWidget = QtWidgets.QTableWidget(self)
		self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget.setWordWrap(True)
		self.tableWidget.setRowCount(6)
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.horizontalHeader().setVisible(False)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(60)
		#self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
		self.tableWidget.verticalHeader().setVisible(False)
		self.tableWidget.verticalHeader().setDefaultSectionSize(60)
		#self.tableWidget.verticalHeader().setMinimumSectionSize(20)
		self.horizontalLayout.addWidget(self.tableWidget)

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)


		self.Auxmylist = list() #list de newcircuit
		#self.mylabel = list() #list de label

		self.tableWidget.contextMenuEvent = self.contextMenuEvent
		self.tableWidget.keyPressEvent = self.keyPressEvent

		self.tableWidget.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget.cellClicked.connect(self.on_cellClickedTableW)


		#self.Form = Form

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))


	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Enter: # mac fn + enter
			self.on_doubleClickedTableW()

	valCut = False
	def contextMenuEvent(self,event):
		self.popMenu = QtWidgets.QMenu(self)
		cutAct = self.popMenu.addAction('Cut')
		pasAct = self.popMenu.addAction('Paste')
		delAct = self.popMenu.addAction('Delete')
	
		if self.valCut == False:
			pasAct.setDisabled(True)
		else:
			pasAct.setDisabled(False)

		action = self.popMenu.exec_(self.tableWidget.mapToGlobal(event.pos()))

		if action == delAct:
			self.items_clear()

		if action == pasAct:
			self.valCut = False   
			self.items_paste()

		if action == cutAct:
			self.items_cut()

	def on_cellClickedTableW(self):
		print("mylist",self.parent.mylist)
		print("mylabel",self.parent.mylabel)
		y = self.tableWidget.columnCount()
		x = self.tableWidget.rowCount()
		if self.tableWidget.currentRow() == x-1:
			self.tableWidget.setRowCount(x+1)

		if self.tableWidget.currentColumn()== y-1:
			self.tableWidget.setColumnCount(y+1)
	
	def on_doubleClickedTableW(self):
		vz = self.parent.tabWidget.currentIndex() + 1 

		if self.parent.rbCM.text()=='Circuit Mode':
			if self.parent.rbCM.isChecked()==True:
				Ui_NewCircuit(str(vz)+"%",self).exec_()
			else:
				Ui_NewLabel(self).exec_()

	def saveMylist(self,saveText):
		self.parent.mylist.append(saveText)
		print("saveList:",self.parent.mylist)

	def deleteMylist(self,deleteText):
		print("Deletemylist")
		
	def totalMylist(self):
		self.Auxmylist = self.parent.mylist[:]
		print("selfAux:",self.Auxmylist)

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
'''