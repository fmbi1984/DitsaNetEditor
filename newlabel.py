# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newlabel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewLabel(QtWidgets.QDialog):
	#def setupUi(self, NewLabel,parent=None):
	def __init__(self,parent=None):
		super(Ui_NewLabel, self).__init__()
		self.parent = parent
		#self.setupUi()

	#def setupUi(self):
		#NewLabel.setObjectName("NewLabel")
		#NewLabel.resize(340, 228)

		self.setObjectName("NewLabel")
		self.setFixedSize(354, 200)
		#self.resize(354,200) #340 228
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
		#self.lblLabel.editingFinished.connect(self.lbltexto)
		#self.lineFont.editingFinished.connect(self.sizeTexto)


	def retranslateUi(self, NewLabel):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("NewLabel", "New Label")) ##New
		self.lblFont.setText(_translate("NewLabel", "Font Size"))


	def lbltexto(self):
		if self.lblLabel.text()=="" or self.lblLabel.text() == " ":
			print("vacio")
			
		else:
			x = self.lblLabel.text()
			print("x:",x)
		
	def sizeTexto(self):
		sizeW = self.lineFont.text()
		print("sizeW:",sizeW)
	
	def bttnOK(self):
		x = self.lblLabel.text()
		sizeW = self.lineFont.text()

		if self.cbFont.currentIndex() == 0:
			align = 'AlignTop'
		if self.cbFont.currentIndex() == 1:
			align = 'AlignBottom'
		self.parent.tableLabel(sizeW,x,align)
		
		self.close()
		

	def bttnCancel(self):
		self.close()

	#def buttons(self):
	#	print("bttn")
	#	y = self.buttonBox.Ok()
	#	print(y)
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