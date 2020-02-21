# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newcircuit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import re
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewCircuit(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super(Ui_NewCircuit, self).__init__()
		self.parent = parent
	#def setupUi(self, NewCircuit):
		#NewCircuit.setObjectName("NewCircuit")
		#NewCircuit.resize(268, 186)
		self.setObjectName("NewCircuit")
		self.setFixedSize(268, 186)
		#self.resize(268, 186)
		self.setWindowFlags(QtCore.Qt.CustomizeWindowHint|QtCore.Qt.WindowTitleHint)
		self.widget = QtWidgets.QWidget(self) #NEw
		self.widget.setGeometry(QtCore.QRect(18, 24, 221, 131))
		self.widget.setObjectName("widget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.lblName = QtWidgets.QLabel(self.widget)
		self.lblName.setObjectName("lblName")
		self.horizontalLayout.addWidget(self.lblName)
		self.lineName = QtWidgets.QLineEdit(self.widget)
		self.lineName.setObjectName("lineName")
		self.horizontalLayout.addWidget(self.lineName)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.lblAddrs = QtWidgets.QLabel(self.widget)
		self.lblAddrs.setObjectName("lblAddrs")
		self.horizontalLayout_2.addWidget(self.lblAddrs)
		self.lineAddrs = QtWidgets.QLineEdit(self.widget)
		self.lineAddrs.setObjectName("lineAddrs")
		self.lineAddrs.setValidator(QtGui.QIntValidator(1,999))
		self.horizontalLayout_2.addWidget(self.lineAddrs)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		self.verticalLayout_2.addLayout(self.verticalLayout)
		self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout_2.addWidget(self.buttonBox)

		self.retranslateUi(self) #New
		self.buttonBox.accepted.connect(self.bttnDone)
		self.buttonBox.rejected.connect(self.bttnCancel)
		self.passEdit = False
		#self.lineName.editingFinished.connect(self.fname)
		#NewCircuit.showEvent = self.showEvent
		QtCore.QMetaObject.connectSlotsByName(self) #NEw

	def retranslateUi(self, NewCircuit):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("NewCircuit", "New Circuit"))
		self.lblName.setText(_translate("NewCircuit", "Name	"))
		self.lblAddrs.setText(_translate("NewCircuit", "Address"))

	def showEvent(self,event):
		vx = self.parent.tableWidget.currentRow()
		vy = self.parent.tableWidget.currentColumn()
		value = "X="+str(vx)+" Y="+str(vy)
		#print(value)
		#print(len(self.parent.mylist))

		for i in range(len(self.parent.mylist)): 
			if self.parent.mylist[i] == value:
				valueName = self.parent.mylist[i+1]
				valueAddr = self.parent.mylist[i+2]
				valueName = valueName.replace('N=','')
				valueAddr = valueAddr.replace('A=','')
				#print(self.parent.mylist)
				self.x = i
				self.passEdit = True 

		if self.passEdit == True:
			self.parent.mylist.pop(self.x+2)
			self.parent.mylist.pop(self.x+1)
			self.parent.mylist.pop(self.x) #se recorre un lugar a la izquierda
			#print(self.parent.mylist)
			self.lineName.setText(valueName)
			self.lineAddrs.setText(valueAddr)

	def bttnCancel(self):
		self.parent.bttnCancel()
		self.close()

	validatorName = False
	validatorAddr = False
	def bttnDone(self):
		name = self.lineName.text()
		addr = self.lineAddrs.text()

		if not self.lineName.text():
			msgN = QtWidgets.QMessageBox()
			msgN.critical(self,'Error','Enter a name')

		else:
			if not self.lineAddrs.text():
				msgA = QtWidgets.QMessageBox()
				msgA.critical(self,'Error','Invalid address data')
			else:
				if len(self.parent.mylist) == 0:
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem("N="+name+'\n'+"A="+addr)
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

					if self.parent.tableWidget.isVisible()==True:
						vx = self.parent.tableWidget.currentRow()
						vy = self.parent.tableWidget.currentColumn()
						self.parent.tableWidget.setItem(vx,vy,item)
						self.parent.mylist.append("X="+str(vx)+" Y="+str(vy))

					if self.parent.tableWidget_2.isVisible()==True:
						vx = self.parent.tableWidget_2.currentRow()
						vy = self.parent.tableWidget_2.currentColumn()
						self.parent.tableWidget_2.setItem(vx,vy,item)

					if self.parent.tableWidget_3.isVisible()==True:
						vx = self.parent.tableWidget_3.currentRow()
						vy = self.parent.tableWidget_3.currentColumn()
						self.parent.tableWidget_3.setItem(vx,vy,item)
					
					if self.parent.tableWidget_4.isVisible()==True:
						vx = self.parent.tableWidget_4.currentRow()
						vy = self.parent.tableWidget_4.currentColumn()
						self.parent.tableWidget_4.setItem(vx,vy,item)
					
					if self.parent.tableWidget_5.isVisible()==True:
						vx = self.parent.tableWidget_5.currentRow()
						vy = self.parent.tableWidget_5.currentColumn()
						self.parent.tableWidget_5.setItem(vx,vy,item)

					if self.parent.tableWidget_6.isVisible()==True:
						vx = self.parent.tableWidget_6.currentRow()
						vy = self.parent.tableWidget_6.currentColumn()
						self.parent.tableWidget_6.setItem(vx,vy,item)

					if self.parent.tableWidget_7.isVisible()==True:
						vx = self.parent.tableWidget_7.currentRow()
						vy = self.parent.tableWidget_7.currentColumn()
						self.parent.tableWidget_7.setItem(vx,vy,item)

					if self.parent.tableWidget_8.isVisible()==True:
						vx = self.parent.tableWidget_8.currentRow()
						vy = self.parent.tableWidget_8.currentColumn()
						self.parent.tableWidget_8.setItem(vx,vy,item)

					if self.parent.tableWidget_9.isVisible()==True:
						vx = self.parent.tableWidget_9.currentRow()
						vy = self.parent.tableWidget_9.currentColumn()
						self.parent.tableWidget_9.setItem(vx,vy,item)

					if self.parent.tableWidget_10.isVisible()==True:
						vx = self.parent.tableWidget_10.currentRow()
						vy = self.parent.tableWidget_10.currentColumn()
						self.parent.tableWidget_10.setItem(vx,vy,item)

					self.parent.mylist.append("N="+name)
					self.parent.mylist.append("A="+addr)

					self.close()
				else:
					#mylistString = ','.join(self.parent.mylist)
					#print("mylistS:",mylistString)

					#validatorName = re.search("N="+name,mylistString)
					#validatorAddr = re.search("A="+addr,mylistString)
					for i in range(len(self.parent.mylist)):
						if self.parent.mylist[i] =="N="+name:
							self.validatorName = True

					for i in range(len(self.parent.mylist)):
						if self.parent.mylist[i] =="A="+addr:
							self.validatorAddr = True

					#print("vaN:",self.validatorName)
					#print("vaAd:",self.validatorAddr)

					if self.validatorName != False:
						msg = QtWidgets.QMessageBox()
						msg.about(self,'Error','Name already exist')
						self.validatorName = False
					else:
						if self.validatorAddr != False:
							msg = QtWidgets.QMessageBox()
							msg.about(self,'Error','Address already exist')
							self.validatorAddr = False
						else:
							lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
							item = QtWidgets.QTableWidgetItem("N="+name+'\n'+"A="+addr)
							item.setFont(lblt)
							item.setBackground(QtGui.QColor('lightblue'))
							item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

							if self.parent.tableWidget.isVisible()==True:
								vx = self.parent.tableWidget.currentRow()
								vy = self.parent.tableWidget.currentColumn()
								self.parent.tableWidget.setItem(vx,vy,item)
								self.parent.mylist.append("X="+str(vx)+" Y="+str(vy))

							if self.parent.tableWidget_2.isVisible()==True:
								vx = self.parent.tableWidget_2.currentRow()
								vy = self.parent.tableWidget_2.currentColumn()
								self.parent.tableWidget_2.setItem(vx,vy,item)

							if self.parent.tableWidget_3.isVisible()==True:
								vx = self.parent.tableWidget_3.currentRow()
								vy = self.parent.tableWidget_3.currentColumn()
								self.parent.tableWidget_3.setItem(vx,vy,item)
							
							if self.parent.tableWidget_4.isVisible()==True:
								vx = self.parent.tableWidget_4.currentRow()
								vy = self.parent.tableWidget_4.currentColumn()
								self.parent.tableWidget_4.setItem(vx,vy,item)
							
							if self.parent.tableWidget_5.isVisible()==True:
								vx = self.parent.tableWidget_5.currentRow()
								vy = self.parent.tableWidget_5.currentColumn()
								self.parent.tableWidget_5.setItem(vx,vy,item)

							if self.parent.tableWidget_6.isVisible()==True:
								vx = self.parent.tableWidget_6.currentRow()
								vy = self.parent.tableWidget_6.currentColumn()
								self.parent.tableWidget_6.setItem(vx,vy,item)

							if self.parent.tableWidget_7.isVisible()==True:
								vx = self.parent.tableWidget_7.currentRow()
								vy = self.parent.tableWidget_7.currentColumn()
								self.parent.tableWidget_7.setItem(vx,vy,item)

							if self.parent.tableWidget_8.isVisible()==True:
								vx = self.parent.tableWidget_8.currentRow()
								vy = self.parent.tableWidget_8.currentColumn()
								self.parent.tableWidget_8.setItem(vx,vy,item)

							if self.parent.tableWidget_9.isVisible()==True:
								vx = self.parent.tableWidget_9.currentRow()
								vy = self.parent.tableWidget_9.currentColumn()
								self.parent.tableWidget_9.setItem(vx,vy,item)

							if self.parent.tableWidget_10.isVisible()==True:
								vx = self.parent.tableWidget_10.currentRow()
								vy = self.parent.tableWidget_10.currentColumn()
								self.parent.tableWidget_10.setItem(vx,vy,item)

							self.parent.mylist.append("N="+name)
							self.parent.mylist.append("A="+addr)
							self.close()

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	NewCircuit = QtWidgets.QDialog()
	ui = Ui_NewCircuit()
	ui.setupUi(NewCircuit)
	NewCircuit.show()
	sys.exit(app.exec_())
'''