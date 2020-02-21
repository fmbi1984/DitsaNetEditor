# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from newlabel import Ui_NewLabel
from newcircuit import Ui_NewCircuit

class Ui_MainWindow(object):
	def __init__(self,MainWindow, parent=None):
		#super(Ui_MainWindow, self).__init__(parent)
		object.__init__(parent)

		#self.setupUi()
		
	#def setupUi(self):
		#object.__init__(parent)
		#self.lineTable = lineTable
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(510, 507)
		self.centralWidget = QtWidgets.QWidget(MainWindow)
		self.centralWidget.setObjectName("centralWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
		self.verticalLayout.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout.setSpacing(6)
		self.verticalLayout.setObjectName("verticalLayout")
		self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
		self.tabWidget.setObjectName("tabWidget")
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
		self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_2.setSpacing(6)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.tableWidget = QtWidgets.QTableWidget(self.tab)
		self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
		self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget.setLineWidth(1)
		self.tableWidget.setShowGrid(True)
		self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget.setWordWrap(True)
		self.tableWidget.setRowCount(6)
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.horizontalHeader().setVisible(False)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(60)
		#self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget.verticalHeader().setVisible(False)
		self.tableWidget.verticalHeader().setDefaultSectionSize(60)
		#self.tableWidget.verticalHeader().setMinimumSectionSize(20)

		self.verticalLayout_2.addWidget(self.tableWidget)
		self.tabWidget.addTab(self.tab, "Page 1")
		
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
		self.tab_3 = QtWidgets.QWidget()
		self.tab_3.setObjectName("tab_3")
		self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
		self.tab_4 = QtWidgets.QWidget()
		self.tab_4.setObjectName("tab_4")
		self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
		self.tab_5 = QtWidgets.QWidget()
		self.tab_5.setObjectName("tab_5")
		self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_5)
		self.tab_6 = QtWidgets.QWidget()
		self.tab_6.setObjectName("tab_6")
		self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_6)
		self.tab_7 = QtWidgets.QWidget()
		self.tab_7.setObjectName("tab_7")
		self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_7)
		self.tab_8 = QtWidgets.QWidget()
		self.tab_8.setObjectName("tab_8")
		self.tableWidget_8 = QtWidgets.QTableWidget(self.tab_8)
		self.tab_9 = QtWidgets.QWidget()
		self.tab_9.setObjectName("tab_9")
		self.tableWidget_9 = QtWidgets.QTableWidget(self.tab_9)
		self.tab_10 = QtWidgets.QWidget()
		self.tab_10.setObjectName("tab_10")
		self.tableWidget_10 = QtWidgets.QTableWidget(self.tab_10)
		'''
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
		self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_3.setSpacing(6)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
		self.tableWidget_2.setBaseSize(QtCore.QSize(0, 0))
		self.tableWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget_2.setLineWidth(1)
		self.tableWidget_2.setShowGrid(True)
		self.tableWidget_2.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget_2.setWordWrap(True)
		self.tableWidget_2.setRowCount(6)
		self.tableWidget_2.setColumnCount(6)
		self.tableWidget_2.setObjectName("tableWidget_2")
		self.tableWidget_2.horizontalHeader().setVisible(False)
		self.tableWidget_2.horizontalHeader().setDefaultSectionSize(60)
		self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget_2.verticalHeader().setVisible(False)
		self.tableWidget_2.verticalHeader().setDefaultSectionSize(60)
		self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
		self.verticalLayout_3.addWidget(self.tableWidget_2)
		self.tabWidget.addTab(self.tab_2, "")
		'''

		self.verticalLayout.addWidget(self.tabWidget)
		MainWindow.setCentralWidget(self.centralWidget)
		self.menuBar = QtWidgets.QMenuBar(MainWindow)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 510, 22))
		self.menuBar.setObjectName("menuBar")
		MainWindow.setMenuBar(self.menuBar)
		#self.mainToolBar = QtWidgets.QToolBar(MainWindow)
		#self.mainToolBar.setObjectName("mainToolBar")
		#MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
		self.statusBar = QtWidgets.QStatusBar(MainWindow)
		self.statusBar.setObjectName("statusBar")
		MainWindow.setStatusBar(self.statusBar)

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		MainWindow.showEvent = self.showEvent
		MainWindow.closeEvent = self.closeEvent
		#self.tableWidget.mousePressEvent = self.mousePressEvent
		self.tableWidget.contextMenuEvent = self.contextMenuEvent
		self.tableWidget.keyPressEvent = self.keyPressEvent

		self.tableWidget_2.contextMenuEvent = self.contextMenuEvent
		self.tableWidget_2.keyPressEvent = self.keyPressEvent
		self.tableWidget_3.contextMenuEvent = self.contextMenuEvent
		self.tableWidget_3.keyPressEvent = self.keyPressEvent
		self.tableWidget_4.contextMenuEvent = self.contextMenuEvent
		self.tableWidget_4.keyPressEvent = self.keyPressEvent
		self.tableWidget_5.contextMenuEvent = self.contextMenuEvent
		self.tableWidget_5.keyPressEvent = self.keyPressEvent
		self.tableWidget_6.contextMenuEvent = self.contextMenuEvent
		self.tableWidget_6.keyPressEvent = self.keyPressEvent
		self.tableWidget_7.contextMenuEvent = self.contextMenuEvent
		self.tableWidget_7.keyPressEvent = self.keyPressEvent
		self.tableWidget_8.contextMenuEvent = self.contextMenuEvent
		self.tableWidget_8.keyPressEvent = self.keyPressEvent
		self.tableWidget_9.contextMenuEvent = self.contextMenuEvent
		self.tableWidget_9.keyPressEvent = self.keyPressEvent
		self.tableWidget_10.contextMenuEvent = self.contextMenuEvent
		self.tableWidget_10.keyPressEvent = self.keyPressEvent

		self.mylist = list()
		self.mylabel = list()
		self.tempCut = list()
		self.newCut = list()
		self.newCutL = list()

		self.newtb.triggered.connect(self.newPage)
		self.savetb.triggered.connect(self.saveLayout)
		self.deletetb.triggered.connect(self.deletePage)
		self.exittb.triggered.connect(self.exitLayout)
		self.tabWidget.tabBarClicked.connect(self.tabSelected)

		self.tableWidget.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget_2.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget_3.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget_4.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget_5.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget_6.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget_7.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget_8.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget_9.cellDoubleClicked.connect(self.on_doubleClickedTableW)
		self.tableWidget_10.cellDoubleClicked.connect(self.on_doubleClickedTableW)

		self.tableWidget.cellClicked.connect(self.on_cellClickedTableW)
		self.tableWidget_2.cellClicked.connect(self.on_cellClickedTableW)
		self.tableWidget_3.cellClicked.connect(self.on_cellClickedTableW)
		self.tableWidget_4.cellClicked.connect(self.on_cellClickedTableW)
		self.tableWidget_5.cellClicked.connect(self.on_cellClickedTableW)
		self.tableWidget_6.cellClicked.connect(self.on_cellClickedTableW)
		self.tableWidget_7.cellClicked.connect(self.on_cellClickedTableW)
		self.tableWidget_8.cellClicked.connect(self.on_cellClickedTableW)
		self.tableWidget_9.cellClicked.connect(self.on_cellClickedTableW)
		self.tableWidget_10.cellClicked.connect(self.on_cellClickedTableW)

		self.tableWidget.itemClicked.connect(self.prueba)
		
		self.MainWindow = MainWindow

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Layout Editor"))
		#self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
		#self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

		self.newtb = QtWidgets.QAction(QtGui.QIcon('image/nuevo.png'),'New',MainWindow)
		self.savetb = QtWidgets.QAction(QtGui.QIcon('image/guardar.png'),'Save',MainWindow)
		self.deletetb = QtWidgets.QAction(QtGui.QIcon('image/borrar.png'),'Delete',MainWindow)
		self.exittb = QtWidgets.QAction(QtGui.QIcon('image/salir.png'),'Exit',MainWindow)

		self.toolB = MainWindow.addToolBar('ToolBar')
		
		self.rbCM = QtWidgets.QRadioButton('Circuit Mode')
		self.rbLM = QtWidgets.QRadioButton('Label Mode')
		self.rbCM.setChecked(True)
		self.rbLM.setChecked(False)

		self.toolB.addWidget(self.rbCM)
		self.toolB.addWidget(self.rbLM)
		self.toolB.addAction(self.newtb)
		self.toolB.addAction(self.savetb)
		self.toolB.addAction(self.deletetb)
		self.toolB.addAction(self.exittb)

		#self.popMenu = QtGui.QMenu(self) 
	
		#self.popMenu.addSeparator() 
		#self.popMenu.addAction(QtGui.QAction('test2', self)) 

	def showEvent(self,event):
		print("ShowEvent")

	def closeEvent(self,event):
		print("CloseEvent")

	#def mousePressEvent(self,event):
	#	if event.button() == QtCore.Qt.RightButton:
	#		print("Click Right")
			

	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Enter: # mac fn + enter
			self.on_doubleClickedTableW()

	def prueba(self):
		print("prueba")
		#x = self.tableWidget.font()
		#print("x:",x)

	valCut = False
	def contextMenuEvent(self,event):
		self.popMenu = QtWidgets.QMenu(MainWindow)
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
	
	i = 0
	def items_cut(self):
		print("cut")
		for item in self.tableWidget.selectedItems():
			self.valCut = True
			self.i = self.i + 1
			txt = item.text()
			coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

			self.tempCut.append(coord2+txt)
			item.setBackground(QtGui.QColor('white'))
			item.setText('')
		
		print("tempCut",self.tempCut)

	def items_paste(self):
		print("paste")
		#item = QtWidgets.QTableWidgetItem()
		copy = self.tempCut[0] #1

		x = copy.split("/")
		vx = self.tableWidget.currentRow()
		vy = self.tableWidget.currentColumn()

		#item.setText(x[1])
		#self.tableWidget.setItem(vx,vy,item)

		self.newCut.append("X="+str(vx)+" Y="+str(vy))
		self.newCut.append(x[1])

		for i in range(len(self.tempCut)-1):
			copy2 = self.tempCut[i+1]  #i+2
			new = u"X=%i Y=%i/" % (vx,vy)
			#print("new:",new)
			#print("copy:",copy)
			y = copy2.split("/") 
			#print("y:",y)
			for i in range(2,7,4): 	#(1,4,2):  
				if copy[i] == copy2[i]:	#1,3
					if i == 2:
						row = int(new[2]) #1
					else:
						column = int(new[6]) #3
				else:
					if i == 2:
						if copy[2] > copy2[2]: #1
							row = int(copy[2]) - int(copy2[2])
						else:
							row = int(copy2[2]) - int(copy[2])
						row = int(new[2]) + row
					else:
						if copy[6] > copy2[6]:  #3
							column = int(copy[6]) - int(copy2[6])
						else:
							column = int(copy2[6]) - int(copy[6])
						column = int(new[6]) + column
			
			#item = QtWidgets.QTableWidgetItem()
			#item.setText(y[1])
			#self.tableWidget.setItem(row,column,item)
			self.newCut.append("X="+str(row)+" Y="+str(column))
			self.newCut.append(y[1])

		print("NEWCUT:",self.newCut)
		self.cleanMylist()
		self.newMylist()
		self.tempCut.clear()
		self.newCut.clear()
		self.i = 0
		print("temCutClean:",self.tempCut)
		print("newCut:",self.newCut)

	def cleanMylist(self): #clean mylist and mylabel
		for i in range(len(self.tempCut)):
			value = self.tempCut[i].split("/")
			print("VALUE:",value)
			for i in range(len(value)):
				for j in range(len(self.mylist)):
					if value[i] == self.mylist[j]:
						self.mylist.pop(j+2)
						self.mylist.pop(j+1)
						self.mylist.pop(j) #se recorre un lugar a la izquierda
						break

				for k in range(len(self.mylabel)):
					if value[i] == self.mylabel[k]:
						self.mylabel.pop(k+1)
						self.mylabel.pop(k) #se recorre un lugar a la izquierda
						break
				
	
	def newMylist(self):
		for j in range(len(self.newCut)):
			x = self.newCut[j].split("\n")
			if len(x) == 2:
				t = self.newCut[j-1]
				#self.newCutL.remove(t)
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(self.newCut[j])
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget.setItem(int(t[2]),int(t[6]),item)

				self.mylist.append(self.newCut[j-1])
				for i in range(2):
					nw = x[i].replace('[]','')
					self.mylist.append(nw)
			else:
				nw = x[0].replace('[]','')
				w = str(nw)

				if w[0] != 'X':
					t = self.newCut[j-1]
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Black)
					item = QtWidgets.QTableWidgetItem(self.newCut[j])
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightyellow'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget.setItem(int(t[2]),int(t[6]),item)

					self.mylabel.append(self.newCut[j-1])
					self.mylabel.append(nw)
					print("M:",self.mylabel)

				#w  = nw[0].split('')
				
				#item = QtWidgets.QTableWidgetItem(self.newCut[j])
				#lblt = QtGui.QFont("Arial",int(sizeW), QtGui.QFont.Black)
				#item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

				#nw = x[0].replace('[]','')
				#print("nw:",nw)
				#self.mylabel.append(nw)

	editDelete = False
	secondEdit = False
	flagEdit = False
	def items_clear(self):
		msgClear = QtWidgets.QMessageBox()
		for item in self.tableWidget.selectedItems():
			self.editDelete = True 

		if self.editDelete == True:
			returnValue = msgClear.warning(self.MainWindow,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
			self.editDelete = False

			if returnValue == msgClear.Yes:
				for item in self.tableWidget.selectedItems(): 
					vy = item.column()
					vx = item.row()
					value = "X="+str(vx)+" Y="+str(vy)

					item.setBackground(QtGui.QColor('white'))
					item.setText('')

					for i in range(len(self.mylist)): 
						if self.mylist[i] == value:
							self.x = i
							self.secondEdit = True

					for i in range(len(self.mylabel)):
						if self.mylabel[i] == value:
							self.y = i
							self.flagEdit = True

					if self.flagEdit == True:
						self.mylabel.pop(self.y+1)
						self.mylabel.pop(self.y)
						self.flagEdit = False

					if self.secondEdit == True: 
						self.mylist.pop(self.x+2)
						self.mylist.pop(self.x+1)
						self.mylist.pop(self.x) #se recorre un lugar a la izquierda
						self.secondEdit = False

	def tabSelected(self):
		print("tabSelect")

	def bttnCancel(self):
		print("Cancel")  ##verificar 
		item = QtWidgets.QTableWidgetItem()
		item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		if self.tableWidget.isVisible()==True:
			vx = self.tableWidget.currentRow()
			vy = self.tableWidget.currentColumn()
			self.tableWidget.setItem(vx,vy,item)

		if self.tableWidget_2.isVisible()==True:
			vx = self.tableWidget_2.currentRow()
			vy = self.tableWidget_2.currentColumn()
			self.tableWidget_2.setItem(vx,vy,item)

		if self.tableWidget_3.isVisible()==True:
			vx = self.tableWidget_3.currentRow()
			vy = self.tableWidget_3.currentColumn()
			self.tableWidget_3.setItem(vx,vy,item)

		if self.tableWidget_4.isVisible()==True:
			vx = self.tableWidget_4.currentRow()
			vy = self.tableWidget_4.currentColumn()
			self.tableWidget_4.setItem(vx,vy,item)

		if self.tableWidget_5.isVisible()==True:
			vx = self.tableWidget_5.currentRow()
			vy = self.tableWidget_5.currentColumn()
			self.tableWidget_5.setItem(vx,vy,item)

		if self.tableWidget_6.isVisible()==True:
			vx = self.tableWidget_6.currentRow()
			vy = self.tableWidget_6.currentColumn()
			self.tableWidget_6.setItem(vx,vy,item)

		if self.tableWidget_7.isVisible()==True:
			vx = self.tableWidget_7.currentRow()
			vy = self.tableWidget_7.currentColumn()
			self.tableWidget_7.setItem(vx,vy,item)

		if self.tableWidget_8.isVisible()==True:
			vx = self.tableWidget_8.currentRow()
			vy = self.tableWidget_8.currentColumn()
			self.tableWidget_8.setItem(vx,vy,item)

		if self.tableWidget_9.isVisible()==True:
			vx = self.tableWidget_9.currentRow()
			vy = self.tableWidget_9.currentColumn()
			self.tableWidget_9.setItem(vx,vy,item)

		if self.tableWidget_10.isVisible()==True:
			vx = self.tableWidget_10.currentRow()
			vy = self.tableWidget_10.currentColumn()
			self.tableWidget_10.setItem(vx,vy,item)

	def tableLabel(self,sizeW,text,textAlign):
		item = QtWidgets.QTableWidgetItem(text)
		lblt = QtGui.QFont("Arial",int(sizeW), QtGui.QFont.Black)
		item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		if textAlign == 'AlignTop':
			item.setTextAlignment(QtCore.Qt.AlignTop)
			item.setFont(lblt)
			item.setBackground(QtGui.QColor('lightyellow'))
			
		else:
			item.setTextAlignment(QtCore.Qt.AlignBottom)
			item.setFont(lblt)
			item.setBackground(QtGui.QColor('lightyellow'))
		
		if self.tableWidget.isVisible()==True:
			vx = self.tableWidget.currentRow()
			vy = self.tableWidget.currentColumn()
			self.tableWidget.setItem(vx,vy,item)
			self.mylabel.append("X="+str(vx)+" Y="+str(vy))

		if self.tableWidget_2.isVisible()==True:
			vx = self.tableWidget_2.currentRow()
			vy = self.tableWidget_2.currentColumn()
			self.tableWidget_2.setItem(vx,vy,item)

		if self.tableWidget_3.isVisible()==True:
			vx = self.tableWidget_3.currentRow()
			vy = self.tableWidget_3.currentColumn()
			self.tableWidget_3.setItem(vx,vy,item)

		if self.tableWidget_4.isVisible()==True:
			vx = self.tableWidget_4.currentRow()
			vy = self.tableWidget_4.currentColumn()
			self.tableWidget_4.setItem(vx,vy,item)

		if self.tableWidget_5.isVisible()==True:
			vx = self.tableWidget_5.currentRow()
			vy = self.tableWidget_5.currentColumn()
			self.tableWidget_5.setItem(vx,vy,item)

		if self.tableWidget_6.isVisible()==True:
			vx = self.tableWidget_6.currentRow()
			vy = self.tableWidget_6.currentColumn()
			self.tableWidget_6.setItem(vx,vy,item)

		if self.tableWidget_7.isVisible()==True:
			vx = self.tableWidget_7.currentRow()
			vy = self.tableWidget_7.currentColumn()
			self.tableWidget_7.setItem(vx,vy,item)

		if self.tableWidget_8.isVisible()==True:
			vx = self.tableWidget_8.currentRow()
			vy = self.tableWidget_8.currentColumn()
			self.tableWidget_8.setItem(vx,vy,item)

		if self.tableWidget_9.isVisible()==True:
			vx = self.tableWidget_9.currentRow()
			vy = self.tableWidget_9.currentColumn()
			self.tableWidget_9.setItem(vx,vy,item)

		if self.tableWidget_10.isVisible()==True:
			vx = self.tableWidget_10.currentRow()
			vy = self.tableWidget_10.currentColumn()
			self.tableWidget_10.setItem(vx,vy,item)

		self.mylabel.append(text)

	def on_cellClickedTableW(self):
		print("mylist",self.mylist)
		print("mylabel",self.mylabel)
		if self.tableWidget.isVisible()==True:
			print("Tabla1")
			#self.tableWidget.setItem(3,3,QtWidgets.QTableWidgetItem("Hola"))
			y = self.tableWidget.columnCount()
			x = self.tableWidget.rowCount()
			if self.tableWidget.currentRow() == x-1:
				self.tableWidget.setRowCount(x+1)

			if self.tableWidget.currentColumn()== y-1:
				self.tableWidget.setColumnCount(y+1)

		if self.tableWidget_2.isVisible() == True:
			print("Tabla2")
			y = self.tableWidget_2.columnCount()
			x = self.tableWidget_2.rowCount()
			if self.tableWidget_2.currentRow() == x-1:
				self.tableWidget_2.setRowCount(x+1)

			if self.tableWidget_2.currentColumn()== y-1:
				self.tableWidget_2.setColumnCount(y+1)

		if self.tableWidget_3.isVisible()==True:
			print("Tabla3")
			y = self.tableWidget_3.columnCount()
			x = self.tableWidget_3.rowCount()
			if self.tableWidget_3.currentRow() == x-1:
				self.tableWidget_3.setRowCount(x+1)

			if self.tableWidget_3.currentColumn()== y-1:
				self.tableWidget_3.setColumnCount(y+1)

		if self.tableWidget_4.isVisible() == True:
			print("Tabla4")
			y = self.tableWidget_4.columnCount()
			x = self.tableWidget_4.rowCount()
			if self.tableWidget_4.currentRow() == x-1:
				self.tableWidget_4.setRowCount(x+1)

			if self.tableWidget_4.currentColumn()== y-1:
				self.tableWidget_4.setColumnCount(y+1)

		if self.tableWidget_5.isVisible()==True:
			print("Tabla5")
			y = self.tableWidget_5.columnCount()
			x = self.tableWidget_5.rowCount()
			if self.tableWidget_5.currentRow() == x-1:
				self.tableWidget_5.setRowCount(x+1)

			if self.tableWidget_5.currentColumn()== y-1:
				self.tableWidget_5.setColumnCount(y+1)

		if self.tableWidget_6.isVisible() == True:
			print("Tabla6")
			y = self.tableWidget_6.columnCount()
			x = self.tableWidget_6.rowCount()
			if self.tableWidget_6.currentRow() == x-1:
				self.tableWidget_6.setRowCount(x+1)

			if self.tableWidget_6.currentColumn()== y-1:
				self.tableWidget_6.setColumnCount(y+1)

		if self.tableWidget_7.isVisible()==True:
			print("Tabla7")
			y = self.tableWidget_7.columnCount()
			x = self.tableWidget_7.rowCount()
			if self.tableWidget_7.currentRow() == x-1:
				self.tableWidget_7.setRowCount(x+1)

			if self.tableWidget_7.currentColumn()== y-1:
				self.tableWidget_7.setColumnCount(y+1)

		if self.tableWidget_8.isVisible() == True:
			print("Tabla8")
			y = self.tableWidget_8.columnCount()
			x = self.tableWidget_8.rowCount()
			if self.tableWidget_8.currentRow() == x-1:
				self.tableWidget_8.setRowCount(x+1)

			if self.tableWidget_8.currentColumn()== y-1:
				self.tableWidget_8.setColumnCount(y+1)

		if self.tableWidget_9.isVisible()==True:
			print("Tabla9")
			y = self.tableWidget_9.columnCount()
			x = self.tableWidget_9.rowCount()
			if self.tableWidget_9.currentRow() == x-1:
				self.tableWidget_9.setRowCount(x+1)

			if self.tableWidget_9.currentColumn()== y-1:
				self.tableWidget_9.setColumnCount(y+1)

		if self.tableWidget_10.isVisible() == True:
			print("Tabla10")
			y = self.tableWidget_10.columnCount()
			x = self.tableWidget_10.rowCount()
			if self.tableWidget_10.currentRow() == x-1:
				self.tableWidget_10.setRowCount(x+1)

			if self.tableWidget_10.currentColumn()== y-1:
				self.tableWidget_10.setColumnCount(y+1)

	def on_doubleClickedTableW(self):
		if self.rbCM.text()=='Circuit Mode':
			if self.rbCM.isChecked()==True:
				Ui_NewCircuit(self).exec_()
			else:
				Ui_NewLabel(self).exec_()

	count = 1
	def newPage(self):
		print("newPage")
		self.count = self.count + 1

		if self.count == 2:
			self.countPage2()
		if self.count == 3:
			self.countPage3()
		if self.count == 4:
			self.countPage4()
		if self.count == 5:
			self.countPage5()
		if self.count == 6:
			self.countPage6()
		if self.count == 7:
			self.countPage7()
		if self.count == 8:
			self.countPage8()
		if self.count == 9:
			self.countPage9()
		if self.count == 10:
			self.countPage10()

	def saveLayout(self):
		print("Save")

	def deletePage(self):
		print("Delete")

	def exitLayout(self):
		print("Exit")
		MainWindow.close()

	def countPage2(self):
		#self.tab_2 = QtWidgets.QWidget()
		#self.tab_2.setObjectName("tab_2")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
		self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_3.setSpacing(6)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		#self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
		self.tableWidget_2.setBaseSize(QtCore.QSize(0, 0))
		self.tableWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget_2.setLineWidth(1)
		self.tableWidget_2.setShowGrid(True)
		self.tableWidget_2.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget_2.setWordWrap(True)
		self.tableWidget_2.setRowCount(6)
		self.tableWidget_2.setColumnCount(6)
		self.tableWidget_2.setObjectName("tableWidget_2")
		self.tableWidget_2.horizontalHeader().setVisible(False)
		self.tableWidget_2.horizontalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget_2.verticalHeader().setVisible(False)
		self.tableWidget_2.verticalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
		self.verticalLayout_3.addWidget(self.tableWidget_2)
		self.tabWidget.addTab(self.tab_2, "Page 2")

	def countPage3(self):
		#self.tab_3 = QtWidgets.QWidget()
		#self.tab_3.setObjectName("tab_3")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
		self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_4.setSpacing(6)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		#self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
		self.tableWidget_3.setBaseSize(QtCore.QSize(0, 0))
		self.tableWidget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.tableWidget_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget_3.setLineWidth(1)
		self.tableWidget_3.setShowGrid(True)
		self.tableWidget_3.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget_3.setWordWrap(True)
		self.tableWidget_3.setRowCount(6)
		self.tableWidget_3.setColumnCount(6)
		self.tableWidget_3.setObjectName("tableWidget_3")
		self.tableWidget_3.horizontalHeader().setVisible(False)
		self.tableWidget_3.horizontalHeader().setDefaultSectionSize(60)
		#self.tableWidget_3.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget_3.verticalHeader().setVisible(False)
		self.tableWidget_3.verticalHeader().setDefaultSectionSize(60)
		#self.tableWidget_3.verticalHeader().setMinimumSectionSize(20)
		self.verticalLayout_4.addWidget(self.tableWidget_3)
		self.tabWidget.addTab(self.tab_3, "Page 3")

	def countPage4(self):
		#self.tab_4 = QtWidgets.QWidget()
		#self.tab_4.setObjectName("tab_4")
		self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_4)
		self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_5.setSpacing(6)
		self.verticalLayout_5.setObjectName("verticalLayout_5")
		#self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
		self.tableWidget_4.setBaseSize(QtCore.QSize(0, 0))
		self.tableWidget_4.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.tableWidget_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget_4.setLineWidth(1)
		self.tableWidget_4.setShowGrid(True)
		self.tableWidget_4.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget_4.setWordWrap(True)
		self.tableWidget_4.setRowCount(6)
		self.tableWidget_4.setColumnCount(6)
		self.tableWidget_4.setObjectName("tableWidget_4")
		self.tableWidget_4.horizontalHeader().setVisible(False)
		self.tableWidget_4.horizontalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget_4.verticalHeader().setVisible(False)
		self.tableWidget_4.verticalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
		self.verticalLayout_5.addWidget(self.tableWidget_4)
		self.tabWidget.addTab(self.tab_4, "Page 4")

	def countPage5(self):
		#self.tab_5 = QtWidgets.QWidget()
		#self.tab_5.setObjectName("tab_5")
		self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_5)
		self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_6.setSpacing(6)
		self.verticalLayout_6.setObjectName("verticalLayout_6")
		#self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_5)
		self.tableWidget_5.setBaseSize(QtCore.QSize(0, 0))
		self.tableWidget_5.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.tableWidget_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget_5.setLineWidth(1)
		self.tableWidget_5.setShowGrid(True)
		self.tableWidget_5.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget_5.setWordWrap(True)
		self.tableWidget_5.setRowCount(6)
		self.tableWidget_5.setColumnCount(6)
		self.tableWidget_5.setObjectName("tableWidget_5")
		self.tableWidget_5.horizontalHeader().setVisible(False)
		self.tableWidget_5.horizontalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget_5.verticalHeader().setVisible(False)
		self.tableWidget_5.verticalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
		self.verticalLayout_6.addWidget(self.tableWidget_5)
		self.tabWidget.addTab(self.tab_5, "Page 5")

	def countPage6(self):
		#self.tab_6 = QtWidgets.QWidget()
		#self.tab_6.setObjectName("tab_6")
		self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_6)
		self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_7.setSpacing(6)
		self.verticalLayout_7.setObjectName("verticalLayout_7")
		#self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_6)
		self.tableWidget_6.setBaseSize(QtCore.QSize(0, 0))
		self.tableWidget_6.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.tableWidget_6.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget_6.setLineWidth(1)
		self.tableWidget_6.setShowGrid(True)
		self.tableWidget_6.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget_6.setWordWrap(True)
		self.tableWidget_6.setRowCount(6)
		self.tableWidget_6.setColumnCount(6)
		self.tableWidget_6.setObjectName("tableWidget_6")
		self.tableWidget_6.horizontalHeader().setVisible(False)
		self.tableWidget_6.horizontalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget_6.verticalHeader().setVisible(False)
		self.tableWidget_6.verticalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
		self.verticalLayout_7.addWidget(self.tableWidget_6)
		self.tabWidget.addTab(self.tab_6, "Page 6")

	def countPage7(self):
		#self.tab_7 = QtWidgets.QWidget()
		#self.tab_7.setObjectName("tab_7")
		self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_7)
		self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_8.setSpacing(6)
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		#self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_7)
		self.tableWidget_7.setBaseSize(QtCore.QSize(0, 0))
		self.tableWidget_7.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.tableWidget_7.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget_7.setLineWidth(1)
		self.tableWidget_7.setShowGrid(True)
		self.tableWidget_7.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget_7.setWordWrap(True)
		self.tableWidget_7.setRowCount(6)
		self.tableWidget_7.setColumnCount(6)
		self.tableWidget_7.setObjectName("tableWidget_7")
		self.tableWidget_7.horizontalHeader().setVisible(False)
		self.tableWidget_7.horizontalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget_7.verticalHeader().setVisible(False)
		self.tableWidget_7.verticalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
		self.verticalLayout_8.addWidget(self.tableWidget_7)
		self.tabWidget.addTab(self.tab_7, "Page 7")

	def countPage8(self):
		#self.tab_8 = QtWidgets.QWidget()
		#self.tab_8.setObjectName("tab_8")
		self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_8)
		self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_9.setSpacing(6)
		self.verticalLayout_9.setObjectName("verticalLayout_9")
		#self.tableWidget_8 = QtWidgets.QTableWidget(self.tab_8)
		self.tableWidget_8.setBaseSize(QtCore.QSize(0, 0))
		self.tableWidget_8.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.tableWidget_8.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget_8.setLineWidth(1)
		self.tableWidget_8.setShowGrid(True)
		self.tableWidget_8.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget_8.setWordWrap(True)
		self.tableWidget_8.setRowCount(6)
		self.tableWidget_8.setColumnCount(6)
		self.tableWidget_8.setObjectName("tableWidget_8")
		self.tableWidget_8.horizontalHeader().setVisible(False)
		self.tableWidget_8.horizontalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget_8.verticalHeader().setVisible(False)
		self.tableWidget_8.verticalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
		self.verticalLayout_9.addWidget(self.tableWidget_8)
		self.tabWidget.addTab(self.tab_8, "Page 8")

	def countPage9(self):
		#self.tab_9 = QtWidgets.QWidget()
		#self.tab_9.setObjectName("tab_9")
		self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_9)
		self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_10.setSpacing(6)
		self.verticalLayout_10.setObjectName("verticalLayout_10")
		#self.tableWidget_9 = QtWidgets.QTableWidget(self.tab_9)
		self.tableWidget_9.setBaseSize(QtCore.QSize(0, 0))
		self.tableWidget_9.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.tableWidget_9.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget_9.setLineWidth(1)
		self.tableWidget_9.setShowGrid(True)
		self.tableWidget_9.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget_9.setWordWrap(True)
		self.tableWidget_9.setRowCount(6)
		self.tableWidget_9.setColumnCount(6)
		self.tableWidget_9.setObjectName("tableWidget_9")
		self.tableWidget_9.horizontalHeader().setVisible(False)
		self.tableWidget_9.horizontalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget_9.verticalHeader().setVisible(False)
		self.tableWidget_9.verticalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
		self.verticalLayout_10.addWidget(self.tableWidget_9)
		self.tabWidget.addTab(self.tab_9, "Page 9")

	def countPage10(self):
		#self.tab_10 = QtWidgets.QWidget()
		#self.tab_10.setObjectName("tab_10")
		self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_10)
		self.verticalLayout_11.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_11.setSpacing(6)
		self.verticalLayout_11.setObjectName("verticalLayout_11")
		#self.tableWidget_10 = QtWidgets.QTableWidget(self.tab_10)
		self.tableWidget_10.setBaseSize(QtCore.QSize(0, 0))
		self.tableWidget_10.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.tableWidget_10.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget_10.setLineWidth(1)
		self.tableWidget_10.setShowGrid(True)
		self.tableWidget_10.setGridStyle(QtCore.Qt.DotLine)
		self.tableWidget_10.setWordWrap(True)
		self.tableWidget_10.setRowCount(6)
		self.tableWidget_10.setColumnCount(6)
		self.tableWidget_10.setObjectName("tableWidget_10")
		self.tableWidget_10.horizontalHeader().setVisible(False)
		self.tableWidget_10.horizontalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
		self.tableWidget_10.verticalHeader().setVisible(False)
		self.tableWidget_10.verticalHeader().setDefaultSectionSize(60)
		#self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
		self.verticalLayout_11.addWidget(self.tableWidget_10)
		self.tabWidget.addTab(self.tab_10, "Page 10")


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	#ui = Ui_MainWindow()
	#ui.setupUi(MainWindow)
	#MainWindow.show()
	ui = Ui_MainWindow(MainWindow)
	#ui.__init__(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
