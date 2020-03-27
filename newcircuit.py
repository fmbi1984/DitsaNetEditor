# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newcircuit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import re
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewCircuit(QtWidgets.QDialog):
	def __init__(self,currentTab,parent=None):
		super(Ui_NewCircuit, self).__init__()
		self.parent = parent
		self.currentTab = currentTab
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
		self.lineName.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("^[-A-Za-z\\d]*$"),self))
		self.horizontalLayout.addWidget(self.lineName)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.lblAddrs = QtWidgets.QLabel(self.widget)
		self.lblAddrs.setObjectName("lblAddrs")
		self.horizontalLayout_2.addWidget(self.lblAddrs)
		self.lineAddrs = QtWidgets.QLineEdit(self.widget)
		self.lineAddrs.setObjectName("lineAddrs")
		#self.lineAddrs.setValidator(QtGui.QIntValidator(1,999))
		self.lineAddrs.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9]\\d{0,2}"),self)) #1-999
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
		QtCore.QMetaObject.connectSlotsByName(self) #NEw

		self.keyPressEvent = self.keyPressEventE

		self.abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		self.lineName.textChanged.connect(self.changeNameUpper)

	def retranslateUi(self, NewCircuit):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("NewCircuit", "New Circuit"))
		self.lblName.setText(_translate("NewCircuit", "Name	"))
		self.lblAddrs.setText(_translate("NewCircuit", "Address"))

	flagD = False
	flagD2 = False
	def showEvent(self,event):
		print("showCircuit")
		vx = self.parent.tableWidget.currentRow()
		vy = self.parent.tableWidget.currentColumn()
		value = "X="+str(vx)+" Y="+str(vy)

		self.parent.totalMylist()
		for i in range(len(self.parent.Auxmylist)): 
			if self.parent.Auxmylist[i] == value and self.parent.Auxmylist[i-1] == self.currentTab:
				valueName = self.parent.Auxmylist[i+1]
				valueAddr = self.parent.Auxmylist[i+2]
				valueName = valueName.replace('N=','')
				valueAddr = valueAddr.replace('A=','')
				self.x = i
				self.passEdit = True 
		
		if self.passEdit == True:
			self.numberTab = self.parent.Auxmylist[self.x-1]
			self.coord = self.parent.Auxmylist[self.x]
			self.CircuitName = self.parent.Auxmylist[self.x+1]
			self.CircuitAddrs = self.parent.Auxmylist[self.x+2]

			self.parent.deleteMylist(self.x+2)
			self.parent.deleteMylist(self.x+1)
			self.parent.deleteMylist(self.x)
			self.parent.deleteMylist(self.x-1)
			self.lineName.setText(valueName)
			self.lineAddrs.setText(valueAddr)

		else:
			#print(len(self.parent.Auxmylist))
			if len(self.parent.Auxmylist) != 0:
				i = len(self.parent.Auxmylist)
				#print("Tab:",self.parent.Auxmylist[i-4])
				valueName = self.parent.Auxmylist[i-2]
				valueAddr = self.parent.Auxmylist[i-1]
				valueName = valueName.replace('N=','')
				valueAddr = valueAddr.replace('A=','')
				#print("VName:",valueName)
				#print("VAddr:",valueAddr)

				self.nextVName(valueName)
				self.nextVAddr(valueAddr)
			else:
				#print("vacio ===")
				self.lineName.setText('1')
				self.lineAddrs.setText('1')


	def keyPressEventE(self,event):
		if event.key() == QtCore.Qt.Key_Enter: # mac fn + enter
			self.bttnDone()

		if event.key() == QtCore.Qt.Key_Escape:
			self.bttnCancel()

	def nextVName(self,VName):
		print("nextVName")
		#y = '-' in VName 
		if '-' in VName != False:
			x = VName.rpartition('-')
			v = VName.rindex('-')
			if VName[v] == '-':
				cmb = x[2]
				digT = len(cmb)
				midig = digT - 2 
				tmp1 = cmb[0:midig]
				tmp = cmb[midig:digT]

				if tmp.isdigit():
					print("dos digitos numeros")
					self.flagD = True
					num = tmp
					#print("NUM:",num)
					numT = int(num) + 1
					#print("numT:",numT)
					if num[0] == '0' and len(str(numT)) != len(num): ##agregar la cantidad de ceros
						#print("digito 0")
						if len(num) > len(str(numT)):
							dif = len(num) - len(str(numT))
							#print("dif:",dif)
						dp = ''
						for n in range(dif):
							dp = dp + '0'

						numT = dp + str(numT) 
					VNameF = str(x[0])+str(x[1])+str(tmp1)+str(numT)
					self.valueMylistName(VNameF)

				if tmp.isalpha():
					print("dos digitos letra")
					self.flagD = True
					dig = tmp[0]
					
					for a in range(len(self.abc)):
						if dig == self.abc[a]:
							if dig == 'Z':
								digF = '-'
								break
							digF = self.abc[a+1]
					dig2 = '0'
					VNameF = str(x[0])+str(x[1])+str(tmp1)+str(digF)+str(dig2)
					self.valueMylistName(VNameF)

				if tmp.isalnum():
					if self.flagD != True:
						print("dos digitos letra-numero")
						dig = tmp[0]
						dig2 = tmp[1]

						if dig.isalpha():
							digF = dig  #dig letra
						else:
							digF = int(dig) + 1  #dig numero

						if dig2.isalpha():
							dig2F = '0'  #dig2 letra
						else:
							dig2F = int(dig2) + 1	#dig2 numero

						VNameF = str(x[0])+str(x[1])+str(tmp1)+str(digF)+str(dig2F)
						self.valueMylistName(VNameF)

		else:
			lenAct = len(VName)
			midAct = lenAct - 2 

			valI = VName[0:midAct]
			valS = VName[midAct:lenAct]

			if valS.isdigit():
				print("dos digitos numeros")
				self.flagD = True
				num = VName
				numT = int(num) + 1
				if num[0] == '0' and len(str(numT)) != len(num): ##agregar la cantidad de ceros
					if len(num) > len(str(numT)):
						dif = len(num) - len(str(numT))
					dp = ''
					for n in range(dif):
						dp = dp + '0'
					numT = dp + str(numT) 

				VNameF = numT
				self.valueMylistName(VNameF)

			if valS.isalpha():
				print("dos digitos letra")
				self.flagD = True
				dig = valS[0]

				for a in range(len(self.abc)):
					if dig == self.abc[a]:
						if dig == 'Z':
							digF = '-'
							break
						digF = self.abc[a+1]
				dig2 = '0'
				VNameF = str(valI)+str(digF)+str(dig2)
				self.valueMylistName(VNameF)

			if valS.isalnum():
				if self.flagD != True:
					print("dos digitos letra-numero")
					dig = valS[0]
					dig2 = valS[1]

					if dig.isalpha():
						digF = dig	#dig letra
					else:
						digF = int(dig) + 1  #dig numero

					if dig2.isalpha():
						dig2F = '0'  #dig2 letra
					else:
						dig2F = int(dig2) + 1	#dig2 numero

					VNameF = str(valI)+str(digF)+str(dig2F)
					self.valueMylistName(VNameF)

	flagName = False
	def valueMylistName(self,VNameF): 
		t = 0
		while t<len(self.parent.Auxmylist)/4:
			t += 1
			self.flagName = False
			for i in range(2,len(self.parent.Auxmylist),4):
				if self.parent.Auxmylist[i] == 'N='+str(VNameF):
					VNameF = self.nextVNameW(str(VNameF))
					self.flagName = True
			
			if self.flagName !=True:
				self.flagName = False
				break

		self.lineName.setText(str(VNameF))


	def nextVNameW(self,VNameF):
		print("neW")
		if '-' in VNameF != False:
			x = VNameF.rpartition('-')
			v = VNameF.rindex('-')
			if VNameF[v] == '-':
				cmb = x[2]
				digT = len(cmb)
				midig = digT - 2 
				tmp1 = cmb[0:midig]
				tmp = cmb[midig:digT]

				if tmp.isdigit():
					print("dos digitos numeros")
					self.flagD2 = True
					num = tmp
					#print("NUM:",num)
					numT = int(num) + 1
					#print("numT:",numT)
					if num[0] == '0' and len(str(numT)) != len(num): ##agregar la cantidad de ceros
						#print("digito 0")
						if len(num) > len(str(numT)):
							dif = len(num) - len(str(numT))
							#print("dif:",dif)
						dp = ''
						for n in range(dif):
							dp = dp + '0'
						#print(dp)
						numT = dp + str(numT) 
					VNameF2 = str(x[0])+str(x[1])+str(tmp1)+str(numT)
				#	self.valueMylistName(VNameF)
					print("FN:",VNameF2)
					return VNameF2
				#	self.lineName.setText(VNameF)

				if tmp.isalpha():
					print("dos digitos letra")
					self.flagD2 = True
					dig = tmp[0]
					
					for a in range(len(self.abc)):
						if dig == self.abc[a]:
							if dig == 'Z':
								digF = '-'
								break
							digF = self.abc[a+1]
					dig2 = '0'
					VNameF2 = str(x[0])+str(x[1])+str(tmp1)+str(digF)+str(dig2)
				#	self.valueMylistName(VNameF)
					print("FN",VNameF2)
					return VNameF2
				#	self.lineName.setText(VNameF)

				if tmp.isalnum():
					if self.flagD2 != True:
						print("dos digitos letra-numero")
						dig = tmp[0]
						dig2 = tmp[1]

						if dig.isalpha():
							digF = dig  #dig letra
						else:
							digF = int(dig) + 1  #dig numero

						if dig2.isalpha():
							dig2F = '0'  #dig2 letra
						else:
							dig2F = int(dig2) + 1	#dig2 numero

						VNameF2 = str(x[0])+str(x[1])+str(tmp1)+str(digF)+str(dig2F)
					#	self.valueMylistName(VNameF)
						print("FN",VNameF2)
						return VNameF2
					#	self.lineName.setText(VNameF)

		else:
			lenAct = len(VNameF)
			midAct = lenAct - 2 

			valI = VNameF[0:midAct]
			valS = VNameF[midAct:lenAct]

			if valS.isdigit():
				print("dos digitos numeros")
				self.flagD2 = True
				num = VNameF
				numT = int(num) + 1
				if num[0] == '0' and len(str(numT)) != len(num): ##agregar la cantidad de ceros
					if len(num) > len(str(numT)):
						dif = len(num) - len(str(numT))
					dp = ''
					for n in range(dif):
						dp = dp + '0'
					numT = dp + str(numT) 

				VNameF2 = numT
			#	self.valueMylistName(VNameF)
				print("FN:",VNameF2)
				return VNameF2
			#	self.lineName.setText(VNameF)

			if valS.isalpha():
				print("dos digitos letra")
				self.flagD2 = True
				dig = valS[0]

				for a in range(len(self.abc)):
					if dig == self.abc[a]:
						#print("abc:",abc[a+1])
						if dig == 'Z':
							digF = '-'
							break
						digF = self.abc[a+1]
				dig2 = '0'
				VNameF2 = str(valI)+str(digF)+str(dig2)
			#	self.valueMylistName(VNameF)
				print("FN:",VNameF2)
				return VNameF2
			#	self.lineName.setText(VNameF)

			if valS.isalnum():
				if self.flagD2 != True:
					print("dos digitos letra-numero")
					dig = valS[0]
					dig2 = valS[1]

					if dig.isalpha():
						digF = dig	#dig letra
					else:
						digF = int(dig) + 1  #dig numero

					if dig2.isalpha():
						dig2F = '0'  #dig2 letra
					else:
						dig2F = int(dig2) + 1	#dig2 numero

					VNameF2 = str(valI)+str(digF)+str(dig2F)
				#	self.valueMylistName(VNameF)
					print("FN:",VNameF2)
					return VNameF2
				#	self.lineName.setText(VNameF)


	def nextVAddr(self,VAddr):
		print("nextVAddr")
		VAddrF = int(VAddr) + 1
		self.valueMylistAddr(VAddrF)
	
	flagNext = False
	def valueMylistAddr(self,VAddrF):
		#print("valores de mylist")
		t = 0
		while t<len(self.parent.Auxmylist)/4:
			t += 1
			self.flagNext = False
			for i in range(3,len(self.parent.Auxmylist),4):
				if self.parent.Auxmylist[i] == 'A='+str(VAddrF):
					VAddrF = int(VAddrF) + 1
					self.flagNext = True
			
			if self.flagNext !=True:
				self.flagNext = False
				break

		self.lineAddrs.setText(str(VAddrF))

		
	def bttnCancel(self): 
		self.parent.totalMylist()
		if len(self.parent.Auxmylist) != 0:
			if self.passEdit != False:
				self.parent.saveMylist(self.numberTab)
				self.parent.saveMylist(self.coord)
				self.parent.saveMylist(self.CircuitName)
				self.parent.saveMylist(self.CircuitAddrs)
				#self.parent.mylist.append(self.coord)
				#self.parent.mylist.append(self.CircuitName)
				#self.parent.mylist.append(self.CircuitAddrs)

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
				self.parent.totalMylist()
				if len(self.parent.Auxmylist) == 0:
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem("N="+name+'\n'+"A="+addr)
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

					vz = self.currentTab
					vx = self.parent.tableWidget.currentRow()
					vy = self.parent.tableWidget.currentColumn()
					self.parent.tableWidget.setItem(vx,vy,item)
					
					self.parent.saveMylist(vz)
					self.parent.saveMylist("X="+str(vx)+" Y="+str(vy))
					self.parent.saveMylist("N="+name)
					self.parent.saveMylist("A="+addr)
					#self.parent.mylist.append(vz)
					#self.parent.mylist.append("X="+str(vx)+" Y="+str(vy))

					#self.parent.mylist.append("N="+name)
					#self.parent.mylist.append("A="+addr)

					self.parent.flagSaveF(False)
					self.close()
				else:
					for i in range(len(self.parent.Auxmylist)):
						if self.parent.Auxmylist[i] =="N="+name:
							self.validatorName = True

					for i in range(len(self.parent.Auxmylist)):
						if self.parent.Auxmylist[i] =="A="+addr:
							self.validatorAddr = True

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

							vz = self.currentTab
							vx = self.parent.tableWidget.currentRow()
							vy = self.parent.tableWidget.currentColumn()
							self.parent.tableWidget.setItem(vx,vy,item)

							self.parent.saveMylist(vz)
							self.parent.saveMylist("X="+str(vx)+" Y="+str(vy))
							self.parent.saveMylist("N="+name)
							self.parent.saveMylist("A="+addr)
							#self.parent.mylist.append(vz)
							#self.parent.mylist.append("X="+str(vx)+" Y="+str(vy))

							#self.parent.mylist.append("N="+name)
							#self.parent.mylist.append("A="+addr)
							self.parent.flagSaveF(False)
							self.close()

	def changeNameUpper(self):
		#print("Upper")
		tmpTxt = self.lineName.text()
		sendTxt = tmpTxt.upper()
		self.lineName.setText(sendTxt)

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