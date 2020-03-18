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
		self.Auxmylabel = list() #list de label

		self.tableWidget.contextMenuEvent = self.contextMenuEvent
		self.tableWidget.keyPressEvent = self.keyPressEvent

		self.tableWidget.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget.cellClicked.connect(self.on_cellClickedTableW)


	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))

	
	def showEvent(self,event):
		#print("showE")
		self.populateCircuit()
		self.populateLabel()

	def populateCircuit(self): 
		print("PopulateCircuit")
		for i in range(0,len(self.parent.mylist),4):
			numberTab = self.parent.mylist[i]
			coordCell = self.parent.mylist[i+1] 
			nameCell = self.parent.mylist[i+2]
			addrCell = self.parent.mylist[i+3]

			z = self.parent.tabWidget.currentIndex() + 1 
			k = numberTab[0].replace('%','')

			if z == 0:
				z = 1

			#print("z",z)
			#print("k",k)
			if k == str(z):
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget.setItem(int(coordCell[2]),int(coordCell[6]),item)

	def populateLabel(self):
		print("PopulateLabel")
		for i in range(0,len(self.parent.mylabel),3):
			numberTabL = self.parent.mylabel[i]
			coordCellL = self.parent.mylabel[i+1]  #2 - x  6- y
			nameCellL = self.parent.mylabel[i+2]

			z = self.parent.tabWidget.currentIndex() + 1 
			k = numberTabL[0].replace('%','')

			if z == 0:
				z = 1

			#print("z2",z)
			#print("k2",k)
			label = nameCellL.split('#')
			number = label[1].split('$')
			lblt = QtGui.QFont("Arial",int(number[0]), QtGui.QFont.Black)
			item = QtWidgets.QTableWidgetItem(label[0])

			if number[1] == 'AT':
				item.setTextAlignment(QtCore.Qt.AlignTop)
			else:
				item.setTextAlignment(QtCore.Qt.AlignBottom)

			item.setFont(lblt)
			item.setBackground(QtGui.QColor('lightyellow'))

			if k == str(z):
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget.setItem(int(coordCellL[2]),int(coordCellL[6]),item)

	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Enter: # mac fn + enter
			self.on_doubleClickedTableW()

	def contextMenuEvent(self,event):
		self.popMenu = QtWidgets.QMenu(self)
		cutAct = self.popMenu.addAction('Cut')
		pasAct = self.popMenu.addAction('Paste')
		delAct = self.popMenu.addAction('Delete')
	
		if self.parent.valCut == False:
			pasAct.setDisabled(True)
		else:
			pasAct.setDisabled(False)

		action = self.popMenu.exec_(self.tableWidget.mapToGlobal(event.pos()))

		if action == delAct:
			self.items_clear()

		if action == pasAct:
			self.parent.valCut = False   
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
				Ui_NewLabel(str(vz)+"%",self).exec_()

	def items_cut(self):
		print("CUT")
		if self.parent.i == 0:
			vz = self.parent.tabWidget.currentIndex() + 1 
			for item in self.tableWidget.selectedItems():
				if item.text()!='':
					self.parent.flagLabel = False
					self.parent.valCut = True
					self.parent.i = self.parent.i + 1
					txt = item.text()
					coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

					for i in range(len(self.parent.mylabel)):
						x = coord2.replace('/','')
						if self.parent.mylabel[i] == x and self.parent.mylabel[i-1]==str(vz)+"%":
							self.parent.flagLabel = True
							self.parent.tempCut.append(str(vz)+"%"+coord2+self.parent.mylabel[i+1])

					if self.parent.flagLabel != True:
						self.parent.tempCut.append(str(vz)+"%"+coord2+txt)
						
					item.setBackground(QtGui.QColor('white'))
					item.setText('')

			print("tempCut1",self.parent.tempCut)
			self.parent.cleanMylist()
		else:
			msgCut = QtWidgets.QMessageBox()
			returnCut = msgCut.warning(self,'Warning','You alredy have circuit copied to memory. If you continue those circuit will be deleted. Are you sure you want to continue?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
			if returnCut == msgCut.Yes:
				#print("YES-MEMORY")
				#print("tempCutElse",self.tempCut)

				#self.cleanMylist()
				self.parent.tempCut.clear()

				vz = self.parent.tabWidget.currentIndex() + 1 
				for item in self.tableWidget.selectedItems():
					if item.text()!='':
						self.parent.flagLabel = False
						self.parent.i = self.parent.i + 1
						txt = item.text()
						coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

						for i in range(len(self.parent.mylabel)):
							x = coord2.replace('/','')
							if self.parent.mylabel[i] == x and self.parent.mylabel[i-1]==str(vz)+"%":
								self.parent.flagLabel = True
								self.parent.tempCut.append(str(vz)+"%"+coord2+self.parent.mylabel[i+1])

						if self.parent.flagLabel != True:
							self.parent.tempCut.append(str(vz)+"%"+coord2+txt)

						item.setBackground(QtGui.QColor('white'))
						item.setText('')
			
				self.parent.cleanMylist()
				print("tempCutElSE",self.parent.tempCut)

	def items_paste(self):
		#print("PASTE") 
		self.flagEmpty = False
		self.parent.tmplist.clear()
		#print("tc:",self.tempCut)
		for i in range(len(self.parent.tempCut)):
			tmp = self.parent.tempCut[i].split("/")
			tmp2 = tmp[0].split("%")
			#print("tmp:",tmp[0])
			#print("tmp2:",tmp2)
			self.parent.tmplist.append(tmp2[0])
			self.parent.tmplist.append(tmp2[1]) 

		for i in range(1,len(self.parent.tmplist),2):
			new = self.parent.tmplist[i]
			#print("NEW:",new)
			for j in range(2,7,4):
				if j == 2:
					self.parent.comp1.append(new[j])
					
				if j == 6:
					self.parent.comp2.append(new[j])

		compT = "X="+min(self.parent.comp1)+" Y="+min(self.parent.comp2)

		#print("Comp1:",self.parent.comp1)
		#print("Comp2:",self.parent.comp2)
		#print("compT1:",compT)
		#print("tmplist1:",self.parent.tmplist)
		for i in range(len(self.parent.tmplist)):
			if compT == self.parent.tmplist[i]:
				#print("No hay espacio Vacio")
				
				self.parent.flagEmpty = True
				self.parent.comp1.clear()
				self.parent.comp2.clear()

		if self.parent.flagEmpty != True:
			self.parent.tempCut.insert(0,tmp2[0]+"%"+"X="+min(self.parent.comp1)+" Y="+min(self.parent.comp2)+"/empty")
			self.parent.comp1.clear()
			self.parent.comp2.clear()

		#print("tempC:",self.tempCut)
		#print("tempC:",self.tempCut[0])
		copy = self.parent.tempCut[0] #1
		x = copy.split("/")
		#///////////////////////////////////////////////////////////////////////////
		vz = self.parent.tabWidget.currentIndex() + 1
		vx = self.tableWidget.currentRow()
		vy = self.tableWidget.currentColumn()

		self.parent.newCut.append(str(vz)+"%")
		self.parent.newCut.append("X="+str(vx)+" Y="+str(vy))
		self.parent.newCut.append(x[1])
		#print("Nuevo:",self.newCut)
		#print("TE:",self.tempCut)

		for i in range(len(self.parent.tempCut)-1):
			copy2 = self.parent.tempCut[i+1]  #i+2
			new = u"X=%i Y=%i/" % (vx,vy)
			#print("new:",new)
			#print("copy:",copy2)
			y = copy2.split("/") 
			#print("y:",y)
			for i in range(4,10,4): #2,7,4	#(1,4,2): #es solo hasta 9 para dos o mas digitos cambia OJO!
				#print("CoPY:",copy)
				#print("COPY2:",copy2)
				#print("C2:",copy2[i])
				#print("C1:",copy[i])
				if copy[i] == copy2[i]:	#1,3
					#print("same")
					if i == 4:
						row = int(new[2]) #1
					else:
						column = int(new[6]) #3
				else:
					if i == 4:
						if copy[4] > copy2[4]: #1
							#print("primerDigitoM")
							row = int(copy[4]) - int(copy2[4])
							row = int(new[2]) - row 
						else:
							#print("primerDigitom")
							row = int(copy2[4]) - int(copy[4])
							row = int(new[2]) + row
						#print("row:",row)
					else:
						if copy[8] > copy2[8]:  #3
							#print("SegundoDigitoM")
							column = int(copy[8]) - int(copy2[8])
							column = int(new[6]) - column
						else:
							#print("SegundoDigitom")
							column = int(copy2[8]) - int(copy[8])
							column = int(new[6]) + column
						#print("column:",column)
			
			self.parent.newCut.append(str(vz)+"%")
			self.parent.newCut.append("X="+str(row)+" Y="+str(column))
			self.parent.newCut.append(y[1])
			#print("Nuevo2:",self.newCut)
			#print("my:",self.parent.mylist)

			for i in range(len(self.parent.mylist)):  #Mylist
				for j in range(1,len(self.parent.newCut),3):
					if self.parent.newCut[j] == self.parent.mylist[i] and self.parent.mylist[i-1] == str(vz)+"%":
						#print("Entro list")
						#print("mylist:",self.mylist[i])
						#print(self.mylist[i-1])
						#print("table:",table)
						#print("newCut:",self.parent.newCut[j])
						self.parent.flagOverList = True

			for i in range(len(self.parent.mylabel)): 
				for j in range(1,len(self.parent.newCut),3):
					if self.parent.newCut[j] == self.parent.mylabel[i] and self.parent.mylabel[i-1] == str(vz)+"%":
						#print("Entro label")
						#print("mylabel:",self.mylabel[i])
						#print(self.mylabel[i-1])
						#print("table:",table)
						#print("newCut:",self.parent.newCut[j])
						self.parent.flagOverLabel = True

		if self.parent.flagOverLabel != False or self.parent.flagOverList != False:
			self.parent.flagOverList = False
			self.parent.flagOverLabel = False
			msgPasteNot = QtWidgets.QMessageBox()
			msgPasteNot.critical(self,'Error','The location is taken')
			self.parent.valCut = True
			self.parent.newCut.clear()
		else:
			print("NEWCUT:",self.parent.newCut)
			#self.cleanMylist()
			self.newMylist()
			self.parent.tempCut.clear()
			self.parent.newCut.clear()
			self.parent.i = 0

		#print("temCutClean:",self.tempCut)
		#print("newCutFinal:",self.parent.newCut)

	def items_clear(self):
		print("clearTable")
		msgClear = QtWidgets.QMessageBox()
		for item in self.tableWidget.selectedItems():
			if item.text()!='':
				self.parent.editDelete = True 

		if self.parent.editDelete == True:
			returnValue = msgClear.warning(self,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
			self.parent.editDelete = False

			if returnValue == msgClear.Yes:
				for item in self.tableWidget.selectedItems(): 
					vy = item.column()
					vx = item.row()
					vz = self.parent.tabWidget.currentIndex() + 1
					value = "X="+str(vx)+" Y="+str(vy)

					item.setBackground(QtGui.QColor('white'))
					item.setText('')

					for i in range(len(self.parent.mylist)): 
						if self.parent.mylist[i] == value and self.parent.mylist[i-1]==str(vz)+"%":
							self.x = i
							self.parent.secondEdit = True

					for i in range(len(self.parent.mylabel)):
						if self.parent.mylabel[i] == value and self.parent.mylabel[i-1]==str(vz)+"%":
							self.y = i
							self.parent.flagEdit = True

					if self.parent.flagEdit == True:
						self.parent.mylabel.pop(self.y+1)
						self.parent.mylabel.pop(self.y)
						self.parent.mylabel.pop(self.y-1)
						self.parent.flagEdit = False

					if self.parent.secondEdit == True: 
						self.parent.mylist.pop(self.x+2)
						self.parent.mylist.pop(self.x+1)
						self.parent.mylist.pop(self.x) #se recorre un lugar a la izquierda
						self.parent.mylist.pop(self.x-1)
						self.parent.secondEdit = False

	def newMylist(self):
		for j in range(len(self.parent.newCut)):
			x = self.parent.newCut[j].split("\n")
			if len(x) == 2:
				t = self.parent.newCut[j-1]
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(self.parent.newCut[j])
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget.setItem(int(t[2]),int(t[6]),item)

				self.parent.mylist.append(self.parent.newCut[j-2])
				self.parent.mylist.append(self.parent.newCut[j-1])
				for i in range(2):
					nw = x[i].replace('[]','')
					self.parent.mylist.append(nw)
			else:
				nw = x[0].replace('[]','')
				w = str(nw)
				#print("w:",w)

				if w[0] != 'X' and w[1] != '%':
					t = self.parent.newCut[j-1]
					if self.parent.newCut[j] == 'empty':
						item = QtWidgets.QTableWidgetItem()
						item.setBackground(QtGui.QColor('white'))
					else:
						label = self.parent.newCut[j].split('#')
						number = label[1].split('$')
						lblt = QtGui.QFont("Arial",int(number[0]), QtGui.QFont.Black)
						item = QtWidgets.QTableWidgetItem(label[0])

						if number[1] == 'AT':
							item.setTextAlignment(QtCore.Qt.AlignTop)
						else:
							item.setTextAlignment(QtCore.Qt.AlignBottom)

						item.setFont(lblt)
						item.setBackground(QtGui.QColor('lightyellow'))

						self.parent.mylabel.append(self.parent.newCut[j-2])
						self.parent.mylabel.append(self.parent.newCut[j-1])
						self.parent.mylabel.append(nw)

					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget.setItem(int(t[2]),int(t[6]),item)

	flagCancel = False
	def bttnCancel(self):
		self.flagCancel = False
		print("Cancel")  
		for item in self.tableWidget.selectedItems():
			self.flagCancel = True
			c = item.text()
			#print("c:",c)
			if item.text():
				print("Con text-Cancel")
			#else:
			#	self.continuesCancel()

		if self.flagCancel != True:
			item = QtWidgets.QTableWidgetItem()
			item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

			vx = self.tableWidget.currentRow()
			vy = self.tableWidget.currentColumn()
			self.tableWidget.setItem(vx,vy,item)

	################ FlagSave ##################
	def flagSaveF(self,textS):
		self.parent.flagSave = textS

	################ MyLabel ###################

	def saveMylabel(self,saveLabel):
		self.parent.mylabel.append(saveLabel)
	
	def deleteMylabel(self,indexLabel):
		self.parent.mylabel.pop(indexLabel)

	def totalMylabel(self):
		self.Auxmylabel = self.parent.mylabel[:]

	############### MyList #####################
	def saveMylist(self,saveText):
		self.parent.mylist.append(saveText)
		#print("saveList:",self.parent.mylist)

	def deleteMylist(self,deleteIndex):
		#print("Deletemylist")
		self.parent.mylist.pop(deleteIndex)
		#print(deleteIndex)
		
	def totalMylist(self):
		self.Auxmylist = self.parent.mylist[:]
		#print("selfAux:",self.Auxmylist)

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