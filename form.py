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
		self.tableWidget.setRowCount(10)
		self.tableWidget.setColumnCount(10)
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
		self.tableWidget.keyPressEvent = self.keyPressEvent ##checar en !!

		self.tableWidget.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget.cellClicked.connect(self.on_cellClickedTableW)


	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
	
	def showEvent(self,event):
		print("showE")
		self.populateColumnRow()
		self.populateCircuit()
		self.populateLabel()
	
	def populateColumnRow(self):
		print("populateColumnRow")
		#print("RC0:",self.parent.rowCol)
		z = self.parent.tabWidget.currentIndex() + 1
		if z == 0:
			z = 1

		for i in range(len(self.parent.rowCol)):
			if self.parent.rowCol[i] == str(z)+'%':
				j = self.parent.rowCol

				tmp = j[i+1].split()
				for i in range(2):
					if i == 0:
						y = tmp[0].partition('R=')
						self.tableWidget.setRowCount(int(y[2]))
					else:
						y = tmp[1].partition('C=')
						self.tableWidget.setColumnCount(int(y[2]))

		#print("TT:",self.parent.rowCol)

	def populateCircuit(self): 
		print("PopulateCircuit")
		for i in range(0,len(self.parent.mylist),4):
			numberTab = self.parent.mylist[i]
			coordCell = self.parent.mylist #i+1 
			nameCell = self.parent.mylist[i+2]
			addrCell = self.parent.mylist[i+3]

			z = self.parent.tabWidget.currentIndex() + 1 
			k = numberTab.replace('%','')

			if z == 0:
				z = 1

			#print("z",z)
			#print("k",k)
			if k == str(z):
				tmp = coordCell[i+1].split()
				for i in range(2):
					if i == 0:
						y = tmp[0].partition('X=')
						coordx = y[2]
					else:
						y = tmp[1].partition('Y=')
						coordy = y[2]

				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget.setItem(int(coordx),int(coordy),item)

	def populateLabel(self):
		print("PopulateLabel")
		for i in range(0,len(self.parent.mylabel),3):
			numberTabL = self.parent.mylabel[i]
			coordCellL = self.parent.mylabel #[i+1]
			nameCellL = self.parent.mylabel[i+2]

			z = self.parent.tabWidget.currentIndex() + 1 
			k = numberTabL.replace('%','')

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
				tmpL = coordCellL[i+1].split()
				for i in range(2):
					if i == 0:
						y = tmpL[0].partition('X=')
						coordx = y[2]
					else:
						y = tmpL[1].partition('Y=')
						coordy = y[2]
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget.setItem(int(coordx),int(coordy),item)

	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Enter: # mac fn + enter
			self.on_doubleClickedTableW()

	def contextMenuEvent(self,event):
		self.on_cellClickedTableW()
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

	flagClickedTableCol = False
	flagClickedTableRow = False
	def on_cellClickedTableW(self):
		print("UNCLICK")
		print("mylist",self.parent.mylist)
		print("mylabel",self.parent.mylabel)
		print("RowCol:",self.parent.rowCol)

		y = self.tableWidget.columnCount()
		x = self.tableWidget.rowCount()
		z = self.parent.tabWidget.currentIndex() + 1

		if self.tableWidget.currentRow() == x-1:
			self.tableWidget.setRowCount(x+1)
			self.flagClickedTableRow = True

		if self.tableWidget.currentColumn()== y-1:
			self.tableWidget.setColumnCount(y+1)
			self.flagClickedTableCol = True
	
		if self.flagClickedTableCol != False or self.flagClickedTableRow != False:
			self.flagClickedTableRow = False
			self.flagClickedTableCol = False

			for i in range(len(self.parent.rowCol)-1):
				if self.parent.rowCol[i] == str(z)+'%':
					#print("entra:",self.parent.rowCol[i])
					self.parent.rowCol.pop(i+1)
					self.parent.rowCol.pop(i)
					break

			self.parent.rowCol.append(str(z)+'%')
			self.parent.rowCol.append('R='+str(self.tableWidget.rowCount())+' C='+str(self.tableWidget.columnCount()))

	def on_doubleClickedTableW(self):
		self.verifyCell()
		vz = self.parent.tabWidget.currentIndex() + 1 
		if self.flagEmpty2 != False:
			self.flagEmpty2 = False
			#print("CELL FULL")
			if self.flagCell != False:
				Ui_NewCircuit(str(vz)+"%",self).exec_()
			else:
				Ui_NewLabel(str(vz)+"%",self).exec_()
		else:
			#print("CELL EMPTY")
			if self.parent.rbCM.text()=='Circuit Mode':
				if self.parent.rbCM.isChecked()==True:
					Ui_NewCircuit(str(vz)+"%",self).exec_()
				else:
					Ui_NewLabel(str(vz)+"%",self).exec_()

	flagCell = False
	flagEmpty2 = False
	def verifyCell(self):
		for item in self.tableWidget.selectedItems():
			if item.text()!='':
				self.flagEmpty2 = True
				mssg = item.text()
				if 'N=' and 'A=' in mssg != False:
					self.flagCell = True
				else:
					self.flagCell = False

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
		print("PASTE") 
		self.parent.flagEmpty = False
		self.parent.tmplist.clear()
		#print("tc:",self.parent.tempCut)
		for i in range(len(self.parent.tempCut)):
			tmp = self.parent.tempCut[i].split("/")
			tmp2 = tmp[0].split("%")
			#print("tmp:",tmp[0])
			#print("tmp2:",tmp2)
			self.parent.tmplist.append(tmp2[0])
			self.parent.tmplist.append(tmp2[1]) 

		for i in range(1,len(self.parent.tmplist),2):
			new = self.parent.tmplist[i].split()
			#print("NEW:",new)

			for i in range(2):
				if i == 0:
					x1 = new[0].partition('X=')
					self.parent.comp1.append(int(x1[2]))
				else:
					y1 = new[1].partition('Y=')
					self.parent.comp2.append(int(y1[2]))

		compT = "X="+str(min(self.parent.comp1))+" Y="+str(min(self.parent.comp2))

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
			#print("flagEmpty")
			self.parent.tempCut.insert(0,tmp2[0]+"%"+"X="+str(min(self.parent.comp1))+" Y="+str(min(self.parent.comp2))+"/empty")
			self.parent.comp1.clear()
			self.parent.comp2.clear()

		#print("tempC:",self.parent.tempCut)
		#print("tempC:",self.parent.tempCut[0])
		copy = self.parent.tempCut[0] #1
		x = copy.split("/")
		#print("x:",x)
		#///////////////////////////////////////////////////////////////////////////
		vz = self.parent.tabWidget.currentIndex() + 1
		vx = self.tableWidget.currentRow()
		vy = self.tableWidget.currentColumn()

		self.parent.newCut.append(str(vz)+"%")
		self.parent.newCut.append("X="+str(vx)+" Y="+str(vy))
		self.parent.newCut.append(x[1])
		#print("Nuevo:",self.parent.newCut)
		#print("TE:",self.parent.tempCut)

		for i in range(len(self.parent.tempCut)-1):
			copy2 = self.parent.tempCut[i+1]  #i+2
			#new = u"X=%i Y=%i/" % (vx,vy)
			#print("new:",new)
			#print("copy:",copy2)
			y = copy2.split("/") 
			#print("y:",y)

			x1 = x[0].split('%')
			y1 = y[0].split('%')
			#print("1x1:",x1)
			#print("1y1:",y1)#teniendo esos datos verif cuatos dig son y de ahi clasificar
			#print("xx",len(x1))
			#print("yy",len(y1))
			tmp1 = x1[1].split()
			#print(tmp1)
			tmp2 = y1[1].split()
			#print(tmp2)
			for i in range(2):
				if i == 0:
					temp1 = tmp1[0].partition('X=')
					#print("X1:",temp1[2])
					coord1x = temp1[2]
	
				else:
					temp1 = tmp1[1].partition('Y=')
					#print("Y1:",temp1[2])
					coord1y = temp1[2]

			for j in range(2):
				if j == 0:
					temp2 = tmp2[0].partition('X=')
					#print("X2:",temp2[2])
					coord2x = temp2[2]
	
				else:
					temp2 = tmp2[1].partition('Y=')
					#print("Y2:",temp2[2])
					coord2y = temp2[2]

			#print("vx:",vx)
			#print("vy:",vy)
			if coord1x == coord2x:
				#print("row")
				row = vx #1
			else:
				if int(coord1x) > int(coord2x): #4
					#print("primerDigitoM")
					row = int(coord1x) - int(coord2x)
					row = vx - row 
				else:
					#print("primerDigitom")
					row = int(coord2x) - int(coord1x)
					row = vx + row
				#print("rowR:",row)
		
			if coord1y == coord2y:
				#print("column")
				column = vy
			else:
				if int(coord1y) > int(coord2y):  #3
					#print("SegundoDigitoM")
					column = int(coord1y) - int(coord2y)
					column = vy - column
				else:
					#print("SegundoDigitom")
					column = int(coord2y) - int(coord1y)
					column = vy + column
				#print("columnR:",column)

			#print("RowT:",row)
			#print("columnT:",column)

			self.parent.newCut.append(str(vz)+"%")
			self.parent.newCut.append("X="+str(row)+" Y="+str(column))
			self.parent.newCut.append(y[1])
			#print("Nuevo2:",self.parent.newCut)
			#print("my:",self.parent.mylist)
			self.verifyColumnRow()

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
			#print("NEWCUT:",self.parent.newCut)
			#self.cleanMylist()
			self.newMylist()
			self.parent.tempCut.clear()
			self.parent.newCut.clear()
			self.parent.i = 0

		#print("temCutClean:",self.tempCut)
		#print("newCutFinal:",self.parent.newCut)

	def verifyColumnRow(self):
		print("verifyColumnRow")
		y = self.tableWidget.columnCount()
		x = self.tableWidget.rowCount()
		z = self.parent.tabWidget.currentIndex() + 1
		#print("z:",z)

		for k in range(1,len(self.parent.newCut),3):
			cell = self.parent.newCut

			tmp = cell[k].split()
			for i in range(2):
				if i == 0:
					num = tmp[0].partition('X=')
					coordx = num[2]
				else:
					num = tmp[1].partition('Y=')
					coordy = num[2]

			if int(coordx) >= x-1:
			#	self.flagVerifyRow = True
				self.tableWidget.setRowCount(x+1)

			if int(coordy) >= y-1:
			#	self.flagVerifyCol = True
				self.tableWidget.setColumnCount(y+1)

			#if self.flagVerifyCol != False or self.flagVerifyRow != False:
			#	self.flagVerifyRow = False
			#	self.flagVerifyCol = False
			for i in range(len(self.parent.rowCol)-1):
				if self.parent.rowCol[i] == str(z)+'%':
					#print("entroF")
					self.parent.rowCol.pop(i+1)
					self.parent.rowCol.pop(i)
					break
			
			self.parent.rowCol.append(str(z)+'%')
			self.parent.rowCol.append('R='+str(self.tableWidget.rowCount())+' C='+str(self.tableWidget.columnCount()))
		#print("CT:",self.parent.rowCol)

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
		print("newMylist")
		for j in range(len(self.parent.newCut)):
			x = self.parent.newCut[j].split("\n")
			if len(x) == 2:
				t = self.parent.newCut[j-1].split()
				for i in range(2):
					if i == 0:
						row = t[0].partition('X=')
						coordx = row[2]
					else:
						col = t[1].partition('Y=')
						coordy = col[2]
				
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(self.parent.newCut[j])
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget.setItem(int(coordx),int(coordy),item)

				self.parent.mylist.append(self.parent.newCut[j-2])
				self.parent.mylist.append(self.parent.newCut[j-1])
				for i in range(2):
					nw = x[i].replace('[]','')
					self.parent.mylist.append(nw)
			else:
				nw = x[0].replace('[]','')
				w = str(nw)
				#print("w:",w)
				#print(len(w))
				if 'X=' in w or '%' in w:
					pass
				else:
				#if w[0] != 'X' and w[1] != '%':
					t = self.parent.newCut[j-1].split()
					for i in range(2):
						if i == 0:
							row = t[0].partition('X=')
							coordx = row[2]
						else:
							col = t[1].partition('Y=')
							coordy = col[2]

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
					self.tableWidget.setItem(int(coordx),int(coordy),item)

	flagCancel = False
	def bttnCancel(self):
		self.flagCancel = False
		print("Cancel")  
		for item in self.tableWidget.selectedItems():
			self.flagCancel = True
			c = item.text()
			#print("c:",c)
			#if item.text():
				#pass
				#print("Con text-Cancel")
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