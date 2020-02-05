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
		self.resize(340,228)
		self.widget = QtWidgets.QWidget(self) #NEw
		self.widget.setGeometry(QtCore.QRect(20, 40, 306, 160))
		self.widget.setObjectName("widget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.lblLabel = QtWidgets.QLineEdit(self.widget)
		self.lblLabel.setObjectName("lblLabel")
		self.verticalLayout.addWidget(self.lblLabel)
		spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.lblFont = QtWidgets.QLabel(self.widget)
		self.lblFont.setObjectName("lblFont")
		self.horizontalLayout.addWidget(self.lblFont)
		self.lineFont = QtWidgets.QLineEdit(self.widget)
		self.lineFont.setEnabled(True)
		self.lineFont.setObjectName("lineFont")
		self.horizontalLayout.addWidget(self.lineFont)
		self.cbFont = QtWidgets.QComboBox(self.widget)
		self.cbFont.setObjectName("cbFont")
		self.horizontalLayout.addWidget(self.cbFont)
		self.verticalLayout.addLayout(self.horizontalLayout)
		spacerItem1 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem1)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem2)
		self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.horizontalLayout_2.addWidget(self.buttonBox)
		self.verticalLayout.addLayout(self.horizontalLayout_2)

		self.retranslateUi(self) ##New
		self.buttonBox.accepted.connect(self.bttnOK)	#NewLabel.accept
		self.buttonBox.rejected.connect(self.bttnCancel)
		QtCore.QMetaObject.connectSlotsByName(self)  ##NEw


		self.lblLabel.editingFinished.connect(self.lbltexto)



	def retranslateUi(self, NewLabel):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("NewLabel", "New Label")) ##New
		self.lblFont.setText(_translate("NewLabel", "Font Size"))


	def lbltexto(self):
		if self.lblLabel.text()=="" or self.lblLabel.text() == " ":
			print("vacio")
		else:
			x = self.lblLabel.text()
			self.parent.tableValue(3,3,x)
			#self.parent.tableWidget.setItem(3,3,QtWidgets.QTableWidgetItem("hola"))
			#tableWidget.setItem(3,3,QtWidgets.QTableWidgetItem(x))
			print("x:",x)

	
	def bttnOK(self):
		print("BttnOK")
		

	def bttnCancel(self):
		print("BttnCancel")

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