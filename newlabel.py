# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newlabel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewLabel(QtWidgets.QDialog):
	#def setupUi(self, NewLabel,parent=None):
	def __init__(self,currentTabL,parent=None):
		super(Ui_NewLabel, self).__init__()
		self.parent = parent
		self.currentTabL = currentTabL
		#self.setupUi()

	#def setupUi(self):
		#NewLabel.setObjectName("NewLabel")
		#NewLabel.resize(340, 228)

		self.setObjectName("NewLabel")
		self.setFixedSize(354, 200)
		#self.resize(354,200) #340 228
		self.setWindowFlags(QtCore.Qt.CustomizeWindowHint|QtCore.Qt.WindowTitleHint)
		self.widget = QtWidgets.QWidget(self) #NEw
		self.widget.setGeometry(QtCore.QRect(20, 20, 321, 151)) #20,40,306,160
		self.widget.setObjectName("widget")
		self.gridLayout = QtWidgets.QGridLayout(self.widget)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")
		self.lblLabel = QtWidgets.QLineEdit(self.widget)
		self.lblLabel.setObjectName("lblLabel")
		self.gridLayout.addWidget(self.lblLabel, 0, 0, 1, 4)
		self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.gridLayout.addWidget(self.buttonBox, 6, 3, 1, 1)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem)
		self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)
		spacerItem1 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem1, 1, 0, 1, 2)
		spacerItem2 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
		self.lineFont = QtWidgets.QLineEdit(self.widget)
		self.lineFont.setEnabled(True)
		self.lineFont.setObjectName("lineFont")
		self.lineFont.setText("8")
		self.gridLayout.addWidget(self.lineFont, 3, 1, 1, 1)
		self.cbFont = QtWidgets.QComboBox(self.widget)
		self.cbFont.setEnabled(True)
		self.cbFont.setObjectName("cbFont")
		self.gridLayout.addWidget(self.cbFont, 3, 3, 1, 1)
		self.lblFont = QtWidgets.QLabel(self.widget)
		self.lblFont.setObjectName("lblFont")
		self.gridLayout.addWidget(self.lblFont, 3, 0, 1, 1)
		spacerItem3 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)

		self.retranslateUi(self) ##New
		self.buttonBox.accepted.connect(self.bttnOK)	#NewLabel.accept
		self.buttonBox.rejected.connect(self.bttnCancel)
		QtCore.QMetaObject.connectSlotsByName(self)  ##NEw

		self.cbFont.addItems(['Align Top','Align Bottom'])

	def retranslateUi(self, NewLabel):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("NewLabel", "New Label")) ##New
		self.lblFont.setText(_translate("NewLabel", "Font Size"))
	
	validatorLabel = False
	def bttnOK(self):
		text = self.lblLabel.text()
		sizeW = self.lineFont.text()
		txtA = None

		if not self.lblLabel.text():
			msgN = QtWidgets.QMessageBox()
			msgN.critical(self,'Error','Enter a label')
		else:
			self.parent.totalMylabel()
			if len(self.parent.Auxmylabel) == 0:
				item = QtWidgets.QTableWidgetItem(text)
				lblt = QtGui.QFont("Arial",int(sizeW), QtGui.QFont.Black)
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

				if self.cbFont.currentIndex() == 0:
					item.setTextAlignment(QtCore.Qt.AlignTop)
					item.setFont(lblt)
					txtA = 'AT'

				if self.cbFont.currentIndex() == 1:
					item.setTextAlignment(QtCore.Qt.AlignBottom)
					item.setFont(lblt)
					txtA = 'AB'
				
				item.setBackground(QtGui.QColor('lightyellow'))

				#vz = self.parent.tabWidget.currentIndex()
				vz = self.currentTabL
				vx = self.parent.tableWidget.currentRow()
				vy = self.parent.tableWidget.currentColumn()
				self.parent.tableWidget.setItem(vx,vy,item)
				
				self.parent.saveMylabel(vz)
				self.parent.saveMylabel("X="+str(vx)+" Y="+str(vy))
				self.parent.saveMylabel(text+"#"+sizeW+"$"+txtA)

				self.parent.flagSaveF(False)
				self.close()
			
			else:
				for i in range(len(self.parent.Auxmylabel)):
					x = self.parent.Auxmylabel[i].split('#')
					#if self.parent.mylabel[i] ==text:
					if x[0] == text:
						self.validatorLabel = True

				if self.validatorLabel != False:
					msg = QtWidgets.QMessageBox()
					msg.about(self,'Error','Label already exist')
					self.validatorLabel = False

				else:
					item = QtWidgets.QTableWidgetItem(text)
					lblt = QtGui.QFont("Arial",int(sizeW), QtGui.QFont.Black)
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

					if self.cbFont.currentIndex() == 0:
						item.setTextAlignment(QtCore.Qt.AlignTop)
						item.setFont(lblt)
						txtA = 'AT'

					if self.cbFont.currentIndex() == 1:
						item.setTextAlignment(QtCore.Qt.AlignBottom)
						item.setFont(lblt)
						txtA = 'AB'
					
					item.setBackground(QtGui.QColor('lightyellow'))

					vz = self.currentTabL
					vx = self.parent.tableWidget.currentRow()
					vy = self.parent.tableWidget.currentColumn()
					self.parent.tableWidget.setItem(vx,vy,item)

					self.parent.saveMylabel(vz)
					self.parent.saveMylabel("X="+str(vx)+" Y="+str(vy))
					self.parent.saveMylabel(text+"#"+sizeW+"$"+txtA)
					#self.parent.mylabel.append("0"+str(vz+1)+"%")
					#self.parent.mylabel.append("X="+str(vx)+" Y="+str(vy))

					#self.parent.mylabel.append(text)
					#self.parent.mylabel.append(text+"#"+sizeW+"$"+txtA)
					self.parent.flagSaveF(False)
					self.close()
		
	def bttnCancel(self):
		self.parent.bttnCancel()
		self.close()

'''
if __name__ == "__main__":

	import sys
	app = QtWidgets.QApplication(sys.argv)
	NewLabel = QtWidgets.QDialog()
	ui = Ui_NewLabel()
	#ui.setupUi(NewLabel)
	ui.__init__(NewLabel)
	NewLabel.show()
	sys.exit(app.exec_())
'''