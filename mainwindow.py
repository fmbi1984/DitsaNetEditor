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

		self.tmplist = list() 
		self.comp1 = list()
		self.comp2 = list()
		self.maxTabs = list()	#lista, se guarda valores de tabs 
		self.tempTabsList = list()
		self.tempTabsLabel =list()

		self.newtb.triggered.connect(self.newPage)
		self.savetb.triggered.connect(self.saveLayout)
		self.deletetb.triggered.connect(self.deletePage)
		self.exittb.triggered.connect(self.exitLayout)

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

		#self.tabWidget.tabBarClicked.connect(self.prueba)
		
		
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
		settings = QtCore.QSettings('Settings/archivo.ini', QtCore.QSettings.NativeFormat)
		if settings.value('Settings/archivo.ini')!='':
			self.settingsList = settings.value("mylist")
			self.settingsLabel = settings.value("mylabel")

			if self.settingsList != None:
				self.populateTabs()
				self.mylist = self.settingsList[:] #para que no se corresponden con el mismo objeto
				self.populateCircuit()

			if self.settingsLabel != None:
				self.mylabel = self.settingsLabel[:] #para que no se corresponden con el mismo objeto
				self.populateLabel()

	def closeEvent(self,event): 
		print("CloseEvent")
		if (len(self.mylist) != 0 or len(self.mylabel) != 0) and self.flagSave != True: 
			if self.settingsList != self.mylist or self.settingsLabel != self.mylabel:
				print("se han hecho cambios y no se ha guardado")
				msgExit = QtWidgets.QMessageBox()
				returnExit = msgExit.warning(self.MainWindow,'Warning','Do you want to save changes?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Cancel)
				if returnExit == msgExit.Yes:
					self.saveLayout()
					MainWindow.close()
				if returnExit == msgExit.No:
					MainWindow.close()
			else:
				MainWindow.close()
		else:
			MainWindow.close()
			

	#def mousePressEvent(self,event):
	#	if event.button() == QtCore.Qt.RightButton:
	#		print("Click Right")
			

	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Enter: # mac fn + enter
			self.on_doubleClickedTableW()

	valCut = False
	def contextMenuEvent(self,event):
		if self.tableWidget.isVisible()==True:
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

		if self.tableWidget_2.isVisible()==True:
			self.popMenu = QtWidgets.QMenu(MainWindow)
			cutAct = self.popMenu.addAction('Cut')
			pasAct = self.popMenu.addAction('Paste')
			delAct = self.popMenu.addAction('Delete')
		
			if self.valCut == False:
				pasAct.setDisabled(True)
			else:
				pasAct.setDisabled(False)

			action = self.popMenu.exec_(self.tableWidget_2.mapToGlobal(event.pos()))

			if action == delAct:
				self.items_clear()

			if action == pasAct:
				self.valCut = False
				self.items_paste()

			if action == cutAct:
				self.items_cut()

		if self.tableWidget_3.isVisible()==True:
			self.popMenu = QtWidgets.QMenu(MainWindow)
			cutAct = self.popMenu.addAction('Cut')
			pasAct = self.popMenu.addAction('Paste')
			delAct = self.popMenu.addAction('Delete')
		
			if self.valCut == False:
				pasAct.setDisabled(True)
			else:
				pasAct.setDisabled(False)

			action = self.popMenu.exec_(self.tableWidget_3.mapToGlobal(event.pos()))

			if action == delAct:
				self.items_clear()

			if action == pasAct:
				self.valCut = False
				self.items_paste()

			if action == cutAct:
				self.items_cut()

		if self.tableWidget_4.isVisible()==True:
			self.popMenu = QtWidgets.QMenu(MainWindow)
			cutAct = self.popMenu.addAction('Cut')
			pasAct = self.popMenu.addAction('Paste')
			delAct = self.popMenu.addAction('Delete')
		
			if self.valCut == False:
				pasAct.setDisabled(True)
			else:
				pasAct.setDisabled(False)

			action = self.popMenu.exec_(self.tableWidget_4.mapToGlobal(event.pos()))

			if action == delAct:
				self.items_clear()

			if action == pasAct:
				self.valCut = False
				self.items_paste()

			if action == cutAct:
				self.items_cut()

		if self.tableWidget_5.isVisible()==True:
			self.popMenu = QtWidgets.QMenu(MainWindow)
			cutAct = self.popMenu.addAction('Cut')
			pasAct = self.popMenu.addAction('Paste')
			delAct = self.popMenu.addAction('Delete')
		
			if self.valCut == False:
				pasAct.setDisabled(True)
			else:
				pasAct.setDisabled(False)

			action = self.popMenu.exec_(self.tableWidget_5.mapToGlobal(event.pos()))

			if action == delAct:
				self.items_clear()

			if action == pasAct:
				self.valCut = False
				self.items_paste()

			if action == cutAct:
				self.items_cut()

		if self.tableWidget_6.isVisible()==True:
			self.popMenu = QtWidgets.QMenu(MainWindow)
			cutAct = self.popMenu.addAction('Cut')
			pasAct = self.popMenu.addAction('Paste')
			delAct = self.popMenu.addAction('Delete')
		
			if self.valCut == False:
				pasAct.setDisabled(True)
			else:
				pasAct.setDisabled(False)

			action = self.popMenu.exec_(self.tableWidget_6.mapToGlobal(event.pos()))

			if action == delAct:
				self.items_clear()

			if action == pasAct:
				self.valCut = False
				self.items_paste()

			if action == cutAct:
				self.items_cut()

		if self.tableWidget_7.isVisible()==True:
			self.popMenu = QtWidgets.QMenu(MainWindow)
			cutAct = self.popMenu.addAction('Cut')
			pasAct = self.popMenu.addAction('Paste')
			delAct = self.popMenu.addAction('Delete')
		
			if self.valCut == False:
				pasAct.setDisabled(True)
			else:
				pasAct.setDisabled(False)

			action = self.popMenu.exec_(self.tableWidget_7.mapToGlobal(event.pos()))

			if action == delAct:
				self.items_clear()

			if action == pasAct:
				self.valCut = False
				self.items_paste()

			if action == cutAct:
				self.items_cut()

		if self.tableWidget_8.isVisible()==True:
			self.popMenu = QtWidgets.QMenu(MainWindow)
			cutAct = self.popMenu.addAction('Cut')
			pasAct = self.popMenu.addAction('Paste')
			delAct = self.popMenu.addAction('Delete')
		
			if self.valCut == False:
				pasAct.setDisabled(True)
			else:
				pasAct.setDisabled(False)

			action = self.popMenu.exec_(self.tableWidget_8.mapToGlobal(event.pos()))

			if action == delAct:
				self.items_clear()

			if action == pasAct:
				self.valCut = False
				self.items_paste()

			if action == cutAct:
				self.items_cut()
		
		if self.tableWidget_9.isVisible()==True:
			self.popMenu = QtWidgets.QMenu(MainWindow)
			cutAct = self.popMenu.addAction('Cut')
			pasAct = self.popMenu.addAction('Paste')
			delAct = self.popMenu.addAction('Delete')
		
			if self.valCut == False:
				pasAct.setDisabled(True)
			else:
				pasAct.setDisabled(False)

			action = self.popMenu.exec_(self.tableWidget_9.mapToGlobal(event.pos()))

			if action == delAct:
				self.items_clear()

			if action == pasAct:
				self.valCut = False
				self.items_paste()

			if action == cutAct:
				self.items_cut()

		if self.tableWidget_10.isVisible()==True:
			self.popMenu = QtWidgets.QMenu(MainWindow)
			cutAct = self.popMenu.addAction('Cut')
			pasAct = self.popMenu.addAction('Paste')
			delAct = self.popMenu.addAction('Delete')
		
			if self.valCut == False:
				pasAct.setDisabled(True)
			else:
				pasAct.setDisabled(False)

			action = self.popMenu.exec_(self.tableWidget_10.mapToGlobal(event.pos()))

			if action == delAct:
				self.items_clear()

			if action == pasAct:
				self.valCut = False
				self.items_paste()

			if action == cutAct:
				self.items_cut()


	def populateCircuit(self): 
		print("PopulateCircuit")
		for i in range(0,len(self.mylist),4):
			numberTab = self.mylist[i]
			coordCell = self.mylist[i+1] 
			nameCell = self.mylist[i+2]
			addrCell = self.mylist[i+3]
			if numberTab == '01%':
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget.setItem(int(coordCell[2]),int(coordCell[6]),item)
			if numberTab == '02%':
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_2.setItem(int(coordCell[2]),int(coordCell[6]),item)
			if numberTab == '03%':
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_3.setItem(int(coordCell[2]),int(coordCell[6]),item)
			if numberTab == '04%':
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_4.setItem(int(coordCell[2]),int(coordCell[6]),item)
			if numberTab == '05%':
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_5.setItem(int(coordCell[2]),int(coordCell[6]),item)
			if numberTab == '06%':
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_6.setItem(int(coordCell[2]),int(coordCell[6]),item)
			if numberTab == '07%':
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_7.setItem(int(coordCell[2]),int(coordCell[6]),item)
			if numberTab == '08%':
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_8.setItem(int(coordCell[2]),int(coordCell[6]),item)
			if numberTab == '09%':
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_9.setItem(int(coordCell[2]),int(coordCell[6]),item)
			if numberTab == '10%':
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(nameCell+'\n'+addrCell)
				item.setFont(lblt)
				item.setBackground(QtGui.QColor('lightblue'))
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_10.setItem(int(coordCell[2]),int(coordCell[6]),item)

	def populateLabel(self):
		print("PopulateLabel")
		for i in range(0,len(self.mylabel),3):
			numberTabL = self.mylabel[i]
			coordCellL = self.mylabel[i+1]  #2 - x  6- y
			nameCellL = self.mylabel[i+2]

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

			if numberTabL == '01%':
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget.setItem(int(coordCellL[2]),int(coordCellL[6]),item)

			if numberTabL == '02%':
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_2.setItem(int(coordCellL[2]),int(coordCellL[6]),item)

			if numberTabL == '03%':
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_3.setItem(int(coordCellL[2]),int(coordCellL[6]),item)
			
			if numberTabL == '04%':
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_4.setItem(int(coordCellL[2]),int(coordCellL[6]),item)

			if numberTabL == '05%':
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_5.setItem(int(coordCellL[2]),int(coordCellL[6]),item)

			if numberTabL == '06%':
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_6.setItem(int(coordCellL[2]),int(coordCellL[6]),item)

			if numberTabL == '07%':
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_7.setItem(int(coordCellL[2]),int(coordCellL[6]),item)

			if numberTabL == '08%':
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_8.setItem(int(coordCellL[2]),int(coordCellL[6]),item)
			
			if numberTabL == '09%':
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_9.setItem(int(coordCellL[2]),int(coordCellL[6]),item)

			if numberTabL == '10%':
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.tableWidget_10.setItem(int(coordCellL[2]),int(coordCellL[6]),item)


	def populateTabs(self):
		print("populateTabs")
		for i in range(0,len(self.settingsList),4):
			self.maxTabs.append(self.settingsList[i])

		for i in range(0,len(self.settingsLabel),3):
			self.maxTabs.append(self.settingsLabel[i])

		y = max(self.maxTabs)
		print(y)
		self.maxTabs.clear()

		if y == '02%':
			self.countPage2()
		if y == '03%':
			self.countPage2()
			self.countPage3()
		if y == '04%':
			self.countPage2()
			self.countPage3()
			self.countPage4()
		if y == '05%':
			self.countPage2()
			self.countPage3()
			self.countPage4()
			self.countPage5()
		if y == '06%':
			self.countPage2()
			self.countPage3()
			self.countPage4()
			self.countPage5()
			self.countPage6()
		if y == '07%':
			self.countPage2()
			self.countPage3()
			self.countPage4()
			self.countPage5()
			self.countPage6()
			self.countPage7()
		if y == '08%':
			self.countPage2()
			self.countPage3()
			self.countPage4()
			self.countPage5()
			self.countPage6()
			self.countPage7()
			self.countPage8()
		if y == '09%':
			self.countPage2()
			self.countPage3()
			self.countPage4()
			self.countPage5()
			self.countPage6()
			self.countPage7()
			self.countPage8()
			self.countPage9()
		if y == '10%':
			self.countPage2()
			self.countPage3()
			self.countPage4()
			self.countPage5()
			self.countPage6()
			self.countPage7()
			self.countPage8()
			self.countPage9()
			self.countPage10()
	
	i = 0
	flagLabel = False
	flagOverLabel = False
	flagOverList = False
	def items_cut(self):
		print("cut")
		if self.i == 0:
			if self.tableWidget.isVisible()==True:
				print("Cut-1")
				vz = self.tabWidget.currentIndex()
				for item in self.tableWidget.selectedItems():
					if item.text()!='':
						self.flagLabel = False
						self.valCut = True
						self.i = self.i + 1
						txt = item.text()
						coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

						for i in range(len(self.mylabel)):
							x = coord2.replace('/','')
							if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.flagLabel = True
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

						if self.flagLabel != True:
							self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)
							
						item.setBackground(QtGui.QColor('white'))
						item.setText('')

			if self.tableWidget_2.isVisible()==True:
				print("Cut-2")
				vz = self.tabWidget.currentIndex()
				for item in self.tableWidget_2.selectedItems():
					if item.text()!='':
						self.flagLabel = False
						self.valCut = True
						self.i = self.i + 1
						txt = item.text()
						coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

						for i in range(len(self.mylabel)):
							x = coord2.replace('/','')
							if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.flagLabel = True
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

						if self.flagLabel != True:
							self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)
							
						item.setBackground(QtGui.QColor('white'))
						item.setText('')

			if self.tableWidget_3.isVisible()==True:
				print("Cut-3")
				vz = self.tabWidget.currentIndex()
				for item in self.tableWidget_3.selectedItems():
					if item.text()!='':
						self.flagLabel = False
						self.valCut = True
						self.i = self.i + 1
						txt = item.text()
						coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

						for i in range(len(self.mylabel)):
							x = coord2.replace('/','')
							if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.flagLabel = True
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

						if self.flagLabel != True:
							self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)
							
						item.setBackground(QtGui.QColor('white'))
						item.setText('')

			if self.tableWidget_4.isVisible()==True:
				print("Cut-4")
				vz = self.tabWidget.currentIndex()
				for item in self.tableWidget_4.selectedItems():
					if item.text()!='':
						self.flagLabel = False
						self.valCut = True
						self.i = self.i + 1
						txt = item.text()
						coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

						for i in range(len(self.mylabel)):
							x = coord2.replace('/','')
							if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.flagLabel = True
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

						if self.flagLabel != True:
							self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)
							
						item.setBackground(QtGui.QColor('white'))
						item.setText('')

			if self.tableWidget_5.isVisible()==True:
				print("Cut-5")
				vz = self.tabWidget.currentIndex()
				for item in self.tableWidget_5.selectedItems():
					if item.text()!='':
						self.flagLabel = False
						self.valCut = True
						self.i = self.i + 1
						txt = item.text()
						coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

						for i in range(len(self.mylabel)):
							x = coord2.replace('/','')
							if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.flagLabel = True
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

						if self.flagLabel != True:
							self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)
							
						item.setBackground(QtGui.QColor('white'))
						item.setText('')

			if self.tableWidget_6.isVisible()==True:
				print("Cut-6")
				vz = self.tabWidget.currentIndex()
				for item in self.tableWidget_6.selectedItems():
					if item.text()!='':
						self.flagLabel = False
						self.valCut = True
						self.i = self.i + 1
						txt = item.text()
						coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

						for i in range(len(self.mylabel)):
							x = coord2.replace('/','')
							if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.flagLabel = True
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

						if self.flagLabel != True:
							self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)
							
						item.setBackground(QtGui.QColor('white'))
						item.setText('')

			if self.tableWidget_7.isVisible()==True:
				print("Cut-7")
				vz = self.tabWidget.currentIndex()
				for item in self.tableWidget_7.selectedItems():
					if item.text()!='':
						self.flagLabel = False
						self.valCut = True
						self.i = self.i + 1
						txt = item.text()
						coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

						for i in range(len(self.mylabel)):
							x = coord2.replace('/','')
							if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.flagLabel = True
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

						if self.flagLabel != True:
							self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)
							
						item.setBackground(QtGui.QColor('white'))
						item.setText('')

			if self.tableWidget_8.isVisible()==True:
				print("Cut-8")
				vz = self.tabWidget.currentIndex()
				for item in self.tableWidget_8.selectedItems():
					if item.text()!='':
						self.flagLabel = False
						self.valCut = True
						self.i = self.i + 1
						txt = item.text()
						coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

						for i in range(len(self.mylabel)):
							x = coord2.replace('/','')
							if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.flagLabel = True
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

						if self.flagLabel != True:
							self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)
							
						item.setBackground(QtGui.QColor('white'))
						item.setText('')

			if self.tableWidget_9.isVisible()==True:
				print("Cut-9")
				vz = self.tabWidget.currentIndex()
				for item in self.tableWidget_9.selectedItems():
					if item.text()!='':
						self.flagLabel = False
						self.valCut = True
						self.i = self.i + 1
						txt = item.text()
						coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

						for i in range(len(self.mylabel)):
							x = coord2.replace('/','')
							if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.flagLabel = True
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

						if self.flagLabel != True:
							self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)
							
						item.setBackground(QtGui.QColor('white'))
						item.setText('')

			if self.tableWidget_10.isVisible()==True:
				print("Cut-10")
				vz = self.tabWidget.currentIndex()
				for item in self.tableWidget_10.selectedItems():
					if item.text()!='':
						self.flagLabel = False
						self.valCut = True
						self.i = self.i + 1
						txt = item.text()
						coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

						for i in range(len(self.mylabel)):
							x = coord2.replace('/','')
							if self.mylabel[i] == x and self.mylabel[i-1]== "0"+str(vz+1)+"%":
								self.flagLabel = True
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

						if self.flagLabel != True:
							self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)
							
						item.setBackground(QtGui.QColor('white'))
						item.setText('')

			print("tempCut1",self.tempCut)
			self.cleanMylist()
		else:
			msgCut = QtWidgets.QMessageBox()
			returnCut = msgCut.warning(self.MainWindow,'Warning','You alredy have circuit copied to memory. If you continue those circuit will be deleted. Are you sure you want to continue?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
			if returnCut == msgCut.Yes:
				#print("YES-MEMORY")
				#print("tempCutElse",self.tempCut)

				#self.cleanMylist()
				self.tempCut.clear()
				
				if self.tableWidget.isVisible()==True:
					vz = self.tabWidget.currentIndex()
					for item in self.tableWidget.selectedItems():
						if item.text()!='':
							self.flagLabel = False
							self.i = self.i + 1
							txt = item.text()
							coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

							for i in range(len(self.mylabel)):
								x = coord2.replace('/','')
								if self.mylabel[i] == x and self.mylabel[i-1]== "0"+str(vz+1)+"%":
									self.flagLabel = True
									self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

							if self.flagLabel != True:
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)

							item.setBackground(QtGui.QColor('white'))
							item.setText('')
				
				if self.tableWidget_2.isVisible()==True:
					vz = self.tabWidget.currentIndex()
					for item in self.tableWidget_2.selectedItems():
						if item.text()!='':
							self.flagLabel = False
							self.i = self.i + 1
							txt = item.text()
							coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

							for i in range(len(self.mylabel)):
								x = coord2.replace('/','')
								if self.mylabel[i] == x and self.mylabel[i-1]== "0"+str(vz+1)+"%":
									self.flagLabel = True
									self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

							if self.flagLabel != True:
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)

							item.setBackground(QtGui.QColor('white'))
							item.setText('')

				if self.tableWidget_3.isVisible()==True:
					vz = self.tabWidget.currentIndex()
					for item in self.tableWidget_3.selectedItems():
						if item.text()!='':
							self.flagLabel = False
							self.i = self.i + 1
							txt = item.text()
							coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

							for i in range(len(self.mylabel)):
								x = coord2.replace('/','')
								if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
									self.flagLabel = True
									self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

							if self.flagLabel != True:
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)

							item.setBackground(QtGui.QColor('white'))
							item.setText('')

				if self.tableWidget_4.isVisible()==True:
					vz = self.tabWidget.currentIndex()
					for item in self.tableWidget_4.selectedItems():
						if item.text()!='':
							self.flagLabel = False
							self.i = self.i + 1
							txt = item.text()
							coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

							for i in range(len(self.mylabel)):
								x = coord2.replace('/','')
								if self.mylabel[i] == x and self.mylabel[i-1]== "0"+str(vz+1)+"%":
									self.flagLabel = True
									self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

							if self.flagLabel != True:
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)

							item.setBackground(QtGui.QColor('white'))
							item.setText('')

				if self.tableWidget_5.isVisible()==True:
					vz = self.tabWidget.currentIndex()
					for item in self.tableWidget_5.selectedItems():
						if item.text()!='':
							self.flagLabel = False
							self.i = self.i + 1
							txt = item.text()
							coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

							for i in range(len(self.mylabel)):
								x = coord2.replace('/','')
								if self.mylabel[i] == x and self.mylabel[i-1]== "0"+str(vz+1)+"%":
									self.flagLabel = True
									self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

							if self.flagLabel != True:
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)

							item.setBackground(QtGui.QColor('white'))
							item.setText('')

				if self.tableWidget_6.isVisible()==True:
					vz = self.tabWidget.currentIndex()
					for item in self.tableWidget_6.selectedItems():
						if item.text()!='':
							self.flagLabel = False
							self.i = self.i + 1
							txt = item.text()
							coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

							for i in range(len(self.mylabel)):
								x = coord2.replace('/','')
								if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
									self.flagLabel = True
									self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

							if self.flagLabel != True:
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)

							item.setBackground(QtGui.QColor('white'))
							item.setText('')

				if self.tableWidget_7.isVisible()==True:
					vz = self.tabWidget.currentIndex()
					for item in self.tableWidget_7.selectedItems():
						if item.text()!='':
							self.flagLabel = False
							self.i = self.i + 1
							txt = item.text()
							coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

							for i in range(len(self.mylabel)):
								x = coord2.replace('/','')
								if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
									self.flagLabel = True
									self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

							if self.flagLabel != True:
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)

							item.setBackground(QtGui.QColor('white'))
							item.setText('')

				if self.tableWidget_8.isVisible()==True:
					vz = self.tabWidget.currentIndex()
					for item in self.tableWidget_8.selectedItems():
						if item.text()!='':
							self.flagLabel = False
							self.i = self.i + 1
							txt = item.text()
							coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

							for i in range(len(self.mylabel)):
								x = coord2.replace('/','')
								if self.mylabel[i] == x and self.mylabel[i-1]== "0"+str(vz+1)+"%":
									self.flagLabel = True
									self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

							if self.flagLabel != True:
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)

							item.setBackground(QtGui.QColor('white'))
							item.setText('')

				if self.tableWidget_9.isVisible()==True:
					vz = self.tabWidget.currentIndex()
					for item in self.tableWidget_9.selectedItems():
						if item.text()!='':
							self.flagLabel = False
							self.i = self.i + 1
							txt = item.text()
							coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

							for i in range(len(self.mylabel)):
								x = coord2.replace('/','')
								if self.mylabel[i] == x and self.mylabel[i-1]== "0"+str(vz+1)+"%":
									self.flagLabel = True
									self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

							if self.flagLabel != True:
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)

							item.setBackground(QtGui.QColor('white'))
							item.setText('')

				if self.tableWidget_10.isVisible()==True:
					vz = self.tabWidget.currentIndex()
					for item in self.tableWidget_10.selectedItems():
						if item.text()!='':
							self.flagLabel = False
							self.i = self.i + 1
							txt = item.text()
							coord2 = u"X=%i Y=%i/" % (item.row(), item.column())

							for i in range(len(self.mylabel)):
								x = coord2.replace('/','')
								if self.mylabel[i] == x and self.mylabel[i-1]=="0"+str(vz+1)+"%":
									self.flagLabel = True
									self.tempCut.append("0"+str(vz+1)+"%"+coord2+self.mylabel[i+1])

							if self.flagLabel != True:
								self.tempCut.append("0"+str(vz+1)+"%"+coord2+txt)

							item.setBackground(QtGui.QColor('white'))
							item.setText('')

				self.cleanMylist()
				print("tempCutElSE",self.tempCut)

	flagEmpty = False
	def items_paste(self):
		print("paste") 
		self.flagEmpty = False
		self.tmplist.clear()
		for i in range(len(self.tempCut)):
			tmp = self.tempCut[i].split("/")
			tmp2 = tmp[0].split("%")
			#print("tmp:",tmp[0])
			#print("tmp2:",tmp2)
			self.tmplist.append(tmp2[0])
			self.tmplist.append(tmp2[1]) 

		for i in range(1,len(self.tmplist),2):
			new = self.tmplist[i]
			#print("NEW:",new)
			for j in range(2,7,4):
				if j == 2:
					self.comp1.append(new[j])
					
				if j == 6:
					self.comp2.append(new[j])

		compT = "X="+min(self.comp1)+" Y="+min(self.comp2)

		#print("Comp1:",self.comp1)
		#print("Comp2:",self.comp2)
		#print("compT1:",compT)
		#print("tmplist1:",self.tmplist)
		for i in range(len(self.tmplist)):
			if compT == self.tmplist[i]:
				#print("No hay espacio Vacio")
				
				self.flagEmpty = True
				self.comp1.clear()
				self.comp2.clear()

		if self.flagEmpty != True:
			self.tempCut.insert(0,tmp2[0]+"%"+"X="+min(self.comp1)+" Y="+min(self.comp2)+"/empty")
			self.comp1.clear()
			self.comp2.clear()

		#print("tempC:",self.tempCut)
		#print("tempC:",self.tempCut[0])
		copy = self.tempCut[0] #1
		x = copy.split("/")
		#///////////////////////////////////////////////////////////////////////////
		if self.tableWidget.isVisible()==True:
			vz = self.tabWidget.currentIndex()
			table = "0"+str(vz+1)+"%"
			vx = self.tableWidget.currentRow()
			vy = self.tableWidget.currentColumn()

		if self.tableWidget_2.isVisible()==True:
			vz = self.tabWidget.currentIndex()
			table = "0"+str(vz+1)+"%"
			vx = self.tableWidget_2.currentRow()
			vy = self.tableWidget_2.currentColumn()

		if self.tableWidget_3.isVisible()==True:
			vz = self.tabWidget.currentIndex()
			table = "0"+str(vz+1)+"%"
			vx = self.tableWidget_3.currentRow()
			vy = self.tableWidget_3.currentColumn()

		if self.tableWidget_4.isVisible()==True:
			vz = self.tabWidget.currentIndex()
			table = "0"+str(vz+1)+"%"
			vx = self.tableWidget_4.currentRow()
			vy = self.tableWidget_4.currentColumn()

		if self.tableWidget_5.isVisible()==True:
			vz = self.tabWidget.currentIndex()
			table = "0"+str(vz+1)+"%"
			vx = self.tableWidget_5.currentRow()
			vy = self.tableWidget_5.currentColumn()

		if self.tableWidget_6.isVisible()==True:
			vz = self.tabWidget.currentIndex()
			table = "0"+str(vz+1)+"%"
			vx = self.tableWidget_6.currentRow()
			vy = self.tableWidget_6.currentColumn()

		if self.tableWidget_7.isVisible()==True:
			vz = self.tabWidget.currentIndex()
			table = "0"+str(vz+1)+"%"
			vx = self.tableWidget_7.currentRow()
			vy = self.tableWidget_7.currentColumn()

		if self.tableWidget_8.isVisible()==True:
			vz = self.tabWidget.currentIndex()
			table = "0"+str(vz+1)+"%"
			vx = self.tableWidget_8.currentRow()
			vy = self.tableWidget_8.currentColumn()

		if self.tableWidget_9.isVisible()==True:
			vz = self.tabWidget.currentIndex()
			table = "0"+str(vz+1)+"%"
			vx = self.tableWidget_9.currentRow()
			vy = self.tableWidget_9.currentColumn()

		if self.tableWidget_10.isVisible()==True:
			vz = self.tabWidget.currentIndex()
			table = "0"+str(vz+1)+"%"
			vx = self.tableWidget_10.currentRow()
			vy = self.tableWidget_10.currentColumn()

		self.newCut.append(table)
		self.newCut.append("X="+str(vx)+" Y="+str(vy))
		self.newCut.append(x[1])
		#print("Nuevo:",self.newCut)
		#print("TE:",self.tempCut)

		for i in range(len(self.tempCut)-1):
			copy2 = self.tempCut[i+1]  #i+2
			new = u"X=%i Y=%i/" % (vx,vy)
			#print("new:",new)
			#print("copy:",copy)
			y = copy2.split("/") 
			#print("y:",y)
			for i in range(5,10,4): #2,7,4	#(1,4,2):  
				#print("CoPY:",copy)
				#print("COPY2:",copy2)
				#print("C2:",copy2[i])
				#print("C1:",copy[i])
				if copy[i] == copy2[i]:	#1,3
					#print("same")
					if i == 5:
						row = int(new[2]) #1
					else:
						column = int(new[6]) #3
				else:
					if i == 5:
						if copy[5] > copy2[5]: #1
							#print("primerDigitoM")
							row = int(copy[5]) - int(copy2[5])
							row = int(new[2]) - row 
						else:
							#print("primerDigitom")
							row = int(copy2[5]) - int(copy[5])
							row = int(new[2]) + row
						#print("row:",row)
					else:
						if copy[9] > copy2[9]:  #3
							#print("SegundoDigitoM")
							column = int(copy[9]) - int(copy2[9])
							column = int(new[6]) - column
						else:
							#print("SegundoDigitom")
							column = int(copy2[9]) - int(copy[9])
							column = int(new[6]) + column
						#print("column:",column)
			
			self.newCut.append(table)
			self.newCut.append("X="+str(row)+" Y="+str(column))
			self.newCut.append(y[1])
			#print("Nuevo2:",self.newCut)
			#print("my:",self.mylist)

			for i in range(len(self.mylist)):  #Mylist
				for j in range(1,len(self.newCut),3):
					if self.newCut[j] == self.mylist[i] and self.mylist[i-1] == table:
						#print("Entro list")
						#print("mylist:",self.mylist[i])
						#print(self.mylist[i-1])
						#print("table:",table)
						#print("newCut:",self.newCut[j])
						self.flagOverList = True

			for i in range(len(self.mylabel)): 
				for j in range(1,len(self.newCut),3):
					if self.newCut[j] == self.mylabel[i] and self.mylabel[i-1] == table:
						#print("Entro label")
						#print("mylabel:",self.mylabel[i])
						#print(self.mylabel[i-1])
						#print("table:",table)
						#print("newCut:",self.newCut[j])
						self.flagOverLabel = True

		if self.flagOverLabel != False or self.flagOverList != False:
			self.flagOverList = False
			self.flagOverLabel = False
			msgPasteNot = QtWidgets.QMessageBox()
			msgPasteNot.critical(self.MainWindow,'Error','The location is taken')
			self.valCut = True
			self.newCut.clear()
		else:
			print("NEWCUT:",self.newCut)
			#self.cleanMylist()
			self.newMylist()
			self.tempCut.clear()
			self.newCut.clear()
			self.i = 0

		print("temCutClean:",self.tempCut)
		print("newCutFinal:",self.newCut)

	def cleanMylist(self): #clean mylist and mylabel
		print("CleanMylist")
		print(self.tempCut)
		for i in range(len(self.tempCut)):
			value = self.tempCut[i].split("/")
			cmpValue = value[0].split("%")
			#print("VALUE:",value)
			#print("cmpValue:",cmpValue)
			#for i in range(len(value)):
			#print("MYLIST:",self.mylist)
			#print("MYLABEL:",self.mylabel)
			for j in range(len(self.mylist)-1):
				if cmpValue[0]+'%' == self.mylist[j] and cmpValue[1] == self.mylist[j+1]:
					#print("j:",j)
					#print("cmpValue2:",cmpValue[0])
					#print("MYLIST:",self.mylist)
					#print(self.mylist[j+3])
					#print(self.mylist[j+2])
					#print(self.mylist[j+1])
					#print(self.mylist[j])
					self.mylist.pop(j+3)
					self.mylist.pop(j+2)
					self.mylist.pop(j+1)
					self.mylist.pop(j) #se recorre un lugar a la izquierda
					break

			for k in range(len(self.mylabel)-1):
				if cmpValue[0]+'%' == self.mylabel[k] and cmpValue[1] == self.mylabel[k+1]:
					#self.mylabel.pop(k+3)
					#print("cmpValue[0]:",cmpValue[0])
					#print("cmpValue[1]:",cmpValue[1])
					#print("mylabel[k+2]:",self.mylabel[k+2])
					#print("mylabel[k+1]:",self.mylabel[k+1])
					#print("mylabel[k]:",self.mylabel[k])
					self.mylabel.pop(k+2)
					self.mylabel.pop(k+1)
					self.mylabel.pop(k) #se recorre un lugar a la izquierda
					break
		
		#print("List:",self.mylist)
		#print("Label:",self.mylabel)

	def newMylist(self):
		for j in range(len(self.newCut)):
			x = self.newCut[j].split("\n")
			if len(x) == 2:
				if self.tableWidget.isVisible()==True:
					t = self.newCut[j-1]
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem(self.newCut[j])
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget.setItem(int(t[2]),int(t[6]),item)

				if self.tableWidget_2.isVisible()==True:
					t = self.newCut[j-1]
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem(self.newCut[j])
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget_2.setItem(int(t[2]),int(t[6]),item)

				if self.tableWidget_3.isVisible()==True:
					t = self.newCut[j-1]
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem(self.newCut[j])
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget_3.setItem(int(t[2]),int(t[6]),item)

				if self.tableWidget_4.isVisible()==True:
					t = self.newCut[j-1]
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem(self.newCut[j])
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget_4.setItem(int(t[2]),int(t[6]),item)

				if self.tableWidget_5.isVisible()==True:
					t = self.newCut[j-1]
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem(self.newCut[j])
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget_5.setItem(int(t[2]),int(t[6]),item)

				if self.tableWidget_6.isVisible()==True:
					t = self.newCut[j-1]
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem(self.newCut[j])
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget_6.setItem(int(t[2]),int(t[6]),item)

				if self.tableWidget_7.isVisible()==True:
					t = self.newCut[j-1]
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem(self.newCut[j])
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget_7.setItem(int(t[2]),int(t[6]),item)

				if self.tableWidget_8.isVisible()==True:
					t = self.newCut[j-1]
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem(self.newCut[j])
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget_8.setItem(int(t[2]),int(t[6]),item)

				if self.tableWidget_9.isVisible()==True:
					t = self.newCut[j-1]
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem(self.newCut[j])
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget_9.setItem(int(t[2]),int(t[6]),item)

				if self.tableWidget_10.isVisible()==True:
					t = self.newCut[j-1]
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem(self.newCut[j])
					item.setFont(lblt)
					item.setBackground(QtGui.QColor('lightblue'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget_10.setItem(int(t[2]),int(t[6]),item)

				self.mylist.append(self.newCut[j-2])
				self.mylist.append(self.newCut[j-1])
				for i in range(2):
					nw = x[i].replace('[]','')
					self.mylist.append(nw)
			else:
				nw = x[0].replace('[]','')
				w = str(nw)

				if w[0] != 'X' and w[2] != '%':
					t = self.newCut[j-1]
					if self.newCut[j] == 'empty':
						item = QtWidgets.QTableWidgetItem()
						item.setBackground(QtGui.QColor('white'))
					else:
						label = self.newCut[j].split('#')
						number = label[1].split('$')
						lblt = QtGui.QFont("Arial",int(number[0]), QtGui.QFont.Black)
						item = QtWidgets.QTableWidgetItem(label[0])

						if number[1] == 'AT':
							item.setTextAlignment(QtCore.Qt.AlignTop)
						else:
							item.setTextAlignment(QtCore.Qt.AlignBottom)

						item.setFont(lblt)
						item.setBackground(QtGui.QColor('lightyellow'))

						self.mylabel.append(self.newCut[j-2])
						self.mylabel.append(self.newCut[j-1])
						self.mylabel.append(nw)
						
					if self.tableWidget.isVisible()==True:
						item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget.setItem(int(t[2]),int(t[6]),item)

					if self.tableWidget_2.isVisible()==True:
						item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget_2.setItem(int(t[2]),int(t[6]),item)

					if self.tableWidget_3.isVisible()==True:
						item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget_3.setItem(int(t[2]),int(t[6]),item)

					if self.tableWidget_4.isVisible()==True:
						item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget_4.setItem(int(t[2]),int(t[6]),item)

					if self.tableWidget_5.isVisible()==True:
						item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget_5.setItem(int(t[2]),int(t[6]),item)

					if self.tableWidget_6.isVisible()==True:
						item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget_6.setItem(int(t[2]),int(t[6]),item)

					if self.tableWidget_7.isVisible()==True:
						item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget_7.setItem(int(t[2]),int(t[6]),item)

					if self.tableWidget_8.isVisible()==True:
						item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget_8.setItem(int(t[2]),int(t[6]),item)

					if self.tableWidget_9.isVisible()==True:
						item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget_9.setItem(int(t[2]),int(t[6]),item)

					if self.tableWidget_10.isVisible()==True:
						item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget_10.setItem(int(t[2]),int(t[6]),item)
		

	editDelete = False 
	secondEdit = False
	flagEdit = False
	def items_clear(self):
		if self.tableWidget.isVisible()==True:
			print("clearTable1")
			msgClear = QtWidgets.QMessageBox()
			for item in self.tableWidget.selectedItems():
				if item.text()!='':
					self.editDelete = True 

			if self.editDelete == True:
				returnValue = msgClear.warning(self.MainWindow,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
				self.editDelete = False

				if returnValue == msgClear.Yes:
					for item in self.tableWidget.selectedItems(): 
						vy = item.column()
						vx = item.row()
						vz = self.tabWidget.currentIndex()
						value = "X="+str(vx)+" Y="+str(vy)

						item.setBackground(QtGui.QColor('white'))
						item.setText('')

						for i in range(len(self.mylist)): 
							if self.mylist[i] == value and self.mylist[i-1]=="0"+str(vz+1)+"%":
								self.x = i
								self.secondEdit = True

						for i in range(len(self.mylabel)):
							if self.mylabel[i] == value and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.y = i
								self.flagEdit = True

						if self.flagEdit == True:
							self.mylabel.pop(self.y+1)
							self.mylabel.pop(self.y)
							self.mylabel.pop(self.y-1)
							self.flagEdit = False

						if self.secondEdit == True: 
							self.mylist.pop(self.x+2)
							self.mylist.pop(self.x+1)
							self.mylist.pop(self.x) #se recorre un lugar a la izquierda
							self.mylist.pop(self.x-1)
							self.secondEdit = False

		if self.tableWidget_2.isVisible()==True:
			print("clearTable2")
			msgClear = QtWidgets.QMessageBox()
			for item in self.tableWidget_2.selectedItems():
				if item.text()!='':
					self.editDelete = True 

			if self.editDelete == True:
				returnValue = msgClear.warning(self.MainWindow,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
				self.editDelete = False

				if returnValue == msgClear.Yes:
					for item in self.tableWidget_2.selectedItems(): 
						vy = item.column()
						vx = item.row()
						vz = self.tabWidget.currentIndex()
						value = "X="+str(vx)+" Y="+str(vy)

						item.setBackground(QtGui.QColor('white'))
						item.setText('')

						for i in range(len(self.mylist)): 
							if self.mylist[i] == value and self.mylist[i-1]=="0"+str(vz+1)+"%":
								self.x = i
								self.secondEdit = True

						for i in range(len(self.mylabel)):
							if self.mylabel[i] == value and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.y = i
								self.flagEdit = True

						if self.flagEdit == True:
							self.mylabel.pop(self.y+1)
							self.mylabel.pop(self.y)
							self.mylabel.pop(self.y-1)
							self.flagEdit = False

						if self.secondEdit == True: 
							self.mylist.pop(self.x+2)
							self.mylist.pop(self.x+1)
							self.mylist.pop(self.x) #se recorre un lugar a la izquierda
							self.mylist.pop(self.x-1)
							self.secondEdit = False

		if self.tableWidget_3.isVisible()==True:
			print("clearTable3")
			msgClear = QtWidgets.QMessageBox()
			for item in self.tableWidget_3.selectedItems():
				if item.text()!='':
					self.editDelete = True 

			if self.editDelete == True:
				returnValue = msgClear.warning(self.MainWindow,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
				self.editDelete = False

				if returnValue == msgClear.Yes:
					for item in self.tableWidget_3.selectedItems(): 
						vy = item.column()
						vx = item.row()
						vz = self.tabWidget.currentIndex()
						value = "X="+str(vx)+" Y="+str(vy)

						item.setBackground(QtGui.QColor('white'))
						item.setText('')

						for i in range(len(self.mylist)): 
							if self.mylist[i] == value and self.mylist[i-1]=="0"+str(vz+1)+"%":
								self.x = i
								self.secondEdit = True

						for i in range(len(self.mylabel)):
							if self.mylabel[i] == value and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.y = i
								self.flagEdit = True

						if self.flagEdit == True:
							self.mylabel.pop(self.y+1)
							self.mylabel.pop(self.y)
							self.mylabel.pop(self.y-1)
							self.flagEdit = False

						if self.secondEdit == True: 
							self.mylist.pop(self.x+2)
							self.mylist.pop(self.x+1)
							self.mylist.pop(self.x) #se recorre un lugar a la izquierda
							self.mylist.pop(self.x-1)
							self.secondEdit = False

		if self.tableWidget_4.isVisible()==True:
			print("clearTable4")
			msgClear = QtWidgets.QMessageBox()
			for item in self.tableWidget_4.selectedItems():
				if item.text()!='':
					self.editDelete = True 

			if self.editDelete == True:
				returnValue = msgClear.warning(self.MainWindow,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
				self.editDelete = False

				if returnValue == msgClear.Yes:
					for item in self.tableWidget_4.selectedItems(): 
						vy = item.column()
						vx = item.row()
						vz = self.tabWidget.currentIndex()
						value = "X="+str(vx)+" Y="+str(vy)

						item.setBackground(QtGui.QColor('white'))
						item.setText('')

						for i in range(len(self.mylist)): 
							if self.mylist[i] == value and self.mylist[i-1]=="0"+str(vz+1)+"%":
								self.x = i
								self.secondEdit = True

						for i in range(len(self.mylabel)):
							if self.mylabel[i] == value and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.y = i
								self.flagEdit = True

						if self.flagEdit == True:
							self.mylabel.pop(self.y+1)
							self.mylabel.pop(self.y)
							self.mylabel.pop(self.y-1)
							self.flagEdit = False

						if self.secondEdit == True: 
							self.mylist.pop(self.x+2)
							self.mylist.pop(self.x+1)
							self.mylist.pop(self.x) #se recorre un lugar a la izquierda
							self.mylist.pop(self.x-1) 
							self.secondEdit = False
		
		if self.tableWidget_5.isVisible()==True:
			print("clearTable5")
			msgClear = QtWidgets.QMessageBox()
			for item in self.tableWidget_5.selectedItems():
				if item.text()!='':
					self.editDelete = True 

			if self.editDelete == True:
				returnValue = msgClear.warning(self.MainWindow,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
				self.editDelete = False

				if returnValue == msgClear.Yes:
					for item in self.tableWidget_5.selectedItems(): 
						vy = item.column()
						vx = item.row()
						vz = self.tabWidget.currentIndex()
						value = "X="+str(vx)+" Y="+str(vy)

						item.setBackground(QtGui.QColor('white'))
						item.setText('')

						for i in range(len(self.mylist)): 
							if self.mylist[i] == value and self.mylist[i-1]=="0"+str(vz+1)+"%":
								self.x = i
								self.secondEdit = True

						for i in range(len(self.mylabel)):
							if self.mylabel[i] == value and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.y = i
								self.flagEdit = True

						if self.flagEdit == True:
							self.mylabel.pop(self.y+1)
							self.mylabel.pop(self.y)
							self.mylabel.pop(self.y-1)
							self.flagEdit = False

						if self.secondEdit == True: 
							self.mylist.pop(self.x+2)
							self.mylist.pop(self.x+1)
							self.mylist.pop(self.x) #se recorre un lugar a la izquierda
							self.mylist.pop(self.x-1)
							self.secondEdit = False

		if self.tableWidget_6.isVisible()==True:
			print("clearTable6")
			msgClear = QtWidgets.QMessageBox()
			for item in self.tableWidget_6.selectedItems():
				if item.text()!='':
					self.editDelete = True 

			if self.editDelete == True:
				returnValue = msgClear.warning(self.MainWindow,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
				self.editDelete = False

				if returnValue == msgClear.Yes:
					for item in self.tableWidget_6.selectedItems(): 
						vy = item.column()
						vx = item.row()
						vz = self.tabWidget.currentIndex()
						value = "X="+str(vx)+" Y="+str(vy)

						item.setBackground(QtGui.QColor('white'))
						item.setText('')

						for i in range(len(self.mylist)): 
							if self.mylist[i] == value and self.mylist[i-1]=="0"+str(vz+1)+"%":
								self.x = i
								self.secondEdit = True

						for i in range(len(self.mylabel)):
							if self.mylabel[i] == value and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.y = i
								self.flagEdit = True

						if self.flagEdit == True:
							self.mylabel.pop(self.y+1)
							self.mylabel.pop(self.y)
							self.mylabel.pop(self.y-1)
							self.flagEdit = False

						if self.secondEdit == True: 
							self.mylist.pop(self.x+2)
							self.mylist.pop(self.x+1)
							self.mylist.pop(self.x) #se recorre un lugar a la izquierda
							self.mylist.pop(self.x-1) 
							self.secondEdit = False

		if self.tableWidget_7.isVisible()==True:
			print("clearTable7")
			msgClear = QtWidgets.QMessageBox()
			for item in self.tableWidget_7.selectedItems():
				if item.text()!='':
					self.editDelete = True 

			if self.editDelete == True:
				returnValue = msgClear.warning(self.MainWindow,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
				self.editDelete = False

				if returnValue == msgClear.Yes:
					for item in self.tableWidget_7.selectedItems(): 
						vy = item.column()
						vx = item.row()
						vz = self.tabWidget.currentIndex()
						value = "X="+str(vx)+" Y="+str(vy)

						item.setBackground(QtGui.QColor('white'))
						item.setText('')

						for i in range(len(self.mylist)): 
							if self.mylist[i] == value and self.mylist[i-1]=="0"+str(vz+1)+"%":
								self.x = i
								self.secondEdit = True

						for i in range(len(self.mylabel)):
							if self.mylabel[i] == value and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.y = i
								self.flagEdit = True

						if self.flagEdit == True:
							self.mylabel.pop(self.y+1)
							self.mylabel.pop(self.y)
							self.mylabel.pop(self.y-1)
							self.flagEdit = False

						if self.secondEdit == True: 
							self.mylist.pop(self.x+2)
							self.mylist.pop(self.x+1)
							self.mylist.pop(self.x) #se recorre un lugar a la izquierda
							self.mylist.pop(self.x-1)
							self.secondEdit = False

		if self.tableWidget_8.isVisible()==True:
			print("clearTable8")
			msgClear = QtWidgets.QMessageBox()
			for item in self.tableWidget_8.selectedItems():
				if item.text()!='':
					self.editDelete = True 

			if self.editDelete == True:
				returnValue = msgClear.warning(self.MainWindow,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
				self.editDelete = False

				if returnValue == msgClear.Yes:
					for item in self.tableWidget_8.selectedItems(): 
						vy = item.column()
						vx = item.row()
						vz = self.tabWidget.currentIndex()
						value = "X="+str(vx)+" Y="+str(vy)

						item.setBackground(QtGui.QColor('white'))
						item.setText('')

						for i in range(len(self.mylist)): 
							if self.mylist[i] == value and self.mylist[i-1]=="0"+str(vz+1)+"%":
								self.x = i
								self.secondEdit = True

						for i in range(len(self.mylabel)):
							if self.mylabel[i] == value and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.y = i
								self.flagEdit = True

						if self.flagEdit == True:
							self.mylabel.pop(self.y+1)
							self.mylabel.pop(self.y)
							self.mylabel.pop(self.y-1)
							self.flagEdit = False

						if self.secondEdit == True: 
							self.mylist.pop(self.x+2)
							self.mylist.pop(self.x+1)
							self.mylist.pop(self.x) #se recorre un lugar a la izquierda
							self.mylist.pop(self.x-1)
							self.secondEdit = False

		if self.tableWidget_9.isVisible()==True:
			print("clearTable9")
			msgClear = QtWidgets.QMessageBox()
			for item in self.tableWidget_9.selectedItems():
				if item.text()!='':
					self.editDelete = True 

			if self.editDelete == True:
				returnValue = msgClear.warning(self.MainWindow,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
				self.editDelete = False

				if returnValue == msgClear.Yes:
					for item in self.tableWidget_9.selectedItems(): 
						vy = item.column()
						vx = item.row()
						vz = self.tabWidget.currentIndex()
						value = "X="+str(vx)+" Y="+str(vy)

						item.setBackground(QtGui.QColor('white'))
						item.setText('')

						for i in range(len(self.mylist)): 
							if self.mylist[i] == value and self.mylist[i-1]=="0"+str(vz+1)+"%":
								self.x = i
								self.secondEdit = True

						for i in range(len(self.mylabel)):
							if self.mylabel[i] == value and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.y = i
								self.flagEdit = True

						if self.flagEdit == True:
							self.mylabel.pop(self.y+1)
							self.mylabel.pop(self.y)
							self.mylabel.pop(self.y-1)
							self.flagEdit = False

						if self.secondEdit == True: 
							self.mylist.pop(self.x+2)
							self.mylist.pop(self.x+1)
							self.mylist.pop(self.x) #se recorre un lugar a la izquierda
							self.mylist.pop(self.x-1)
							self.secondEdit = False

		if self.tableWidget_10.isVisible()==True:
			print("clearTable10")
			msgClear = QtWidgets.QMessageBox()
			for item in self.tableWidget_10.selectedItems():
				if item.text()!='':
					self.editDelete = True 

			if self.editDelete == True:
				returnValue = msgClear.warning(self.MainWindow,'Warning','Are you sure you want to delete?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
				self.editDelete = False

				if returnValue == msgClear.Yes:
					for item in self.tableWidget_10.selectedItems(): 
						vy = item.column()
						vx = item.row()
						vz = self.tabWidget.currentIndex()
						value = "X="+str(vx)+" Y="+str(vy)

						item.setBackground(QtGui.QColor('white'))
						item.setText('')

						for i in range(len(self.mylist)): 
							if self.mylist[i] == value and self.mylist[i-1]=="0"+str(vz+1)+"%":
								self.x = i
								self.secondEdit = True

						for i in range(len(self.mylabel)):
							if self.mylabel[i] == value and self.mylabel[i-1]=="0"+str(vz+1)+"%":
								self.y = i
								self.flagEdit = True

						if self.flagEdit == True:
							self.mylabel.pop(self.y+1)
							self.mylabel.pop(self.y)
							self.mylabel.pop(self.y-1)
							self.flagEdit = False

						if self.secondEdit == True: 
							self.mylist.pop(self.x+2)
							self.mylist.pop(self.x+1)
							self.mylist.pop(self.x) #se recorre un lugar a la izquierda
							self.mylist.pop(self.x-1)
							self.secondEdit = False

	flagCancel = False
	def bttnCancel(self):
		self.flagCancel = False
		if self.tableWidget.isVisible()==True:
			print("CancelT1")  
			for item in self.tableWidget.selectedItems():
				self.flagCancel = True
				c = item.text()
				#print("c:",c)
				if item.text():
					print("Con text-Cancel")
				else:
					self.continuesCancel()

		if self.tableWidget_2.isVisible()==True:
			print("CancelT2")  
			for item in self.tableWidget_2.selectedItems():
				self.flagCancel = True
				c = item.text()
				#print("c:",c)
				if item.text():
					print("Con text-Cancel")
				else:
					self.continuesCancel()

		if self.tableWidget_3.isVisible()==True:
			print("CancelT3")  
			for item in self.tableWidget_3.selectedItems():
				self.flagCancel = True
				c = item.text()
				#print("c:",c)
				if item.text():
					print("Con text-Cancel")
				else:
					self.continuesCancel()

		if self.tableWidget_4.isVisible()==True:
			print("CancelT4")  
			for item in self.tableWidget_4.selectedItems():
				self.flagCancel = True
				c = item.text()
				#print("c:",c)
				if item.text():
					print("Con text-Cancel")
				else:
					self.continuesCancel()

		if self.tableWidget_5.isVisible()==True:
			print("CancelT5")  
			for item in self.tableWidget_5.selectedItems():
				self.flagCancel = True
				c = item.text()
				#print("c:",c)
				if item.text():
					print("Con text-Cancel")
				else:
					self.continuesCancel()

		if self.tableWidget_6.isVisible()==True:
			print("CancelT6")  
			for item in self.tableWidget_6.selectedItems():
				self.flagCancel = True
				c = item.text()
				#print("c:",c)
				if item.text():
					print("Con text-Cancel")
				else:
					self.continuesCancel()
		
		if self.tableWidget_7.isVisible()==True:
			print("CancelT7")  
			for item in self.tableWidget_7.selectedItems():
				self.flagCancel = True
				c = item.text()
				#print("c:",c)
				if item.text():
					print("Con text-Cancel")
				else:
					self.continuesCancel()

		if self.tableWidget_8.isVisible()==True:
			print("CancelT8")  
			for item in self.tableWidget_8.selectedItems():
				self.flagCancel = True
				c = item.text()
				#print("c:",c)
				if item.text():
					print("Con text-Cancel")
				else:
					self.continuesCancel()

		if self.tableWidget_9.isVisible()==True:
			print("CancelT9")  
			for item in self.tableWidget_9.selectedItems():
				self.flagCancel = True
				c = item.text()
				#print("c:",c)
				if item.text():
					print("Con text-Cancel")
				else:
					self.continuesCancel()

		if self.tableWidget_10.isVisible()==True:
			print("CancelT10")  
			for item in self.tableWidget_10.selectedItems():
				self.flagCancel = True
				c = item.text()
				#print("c:",c)
				if item.text():
					print("Con text-Cancel")
				else:
					self.continuesCancel()

		if self.flagCancel != True:
			self.continuesCancel()

	def continuesCancel(self):
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

	def on_cellClickedTableW(self):
		print("mylist",self.mylist)
		print("mylabel",self.mylabel)
		if self.tableWidget.isVisible()==True:
			print("Tabla1")
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
	def newPage(self): ## verificar tab actual para poner al agregar 
		print("newPage")
		y = self.tabWidget.count()
		print("countTabs:",y)

		

		if y != 0:
			self.count = y + 1
			
		else:
			self.count = self.count + 1
		
		
		print("countNEW:",self.count)



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

	flagSave = False
	def saveLayout(self): 
		print("Save")
		if len(self.mylist) != 0 or len(self.mylabel) != 0:
			self.flagSave = True
			print("hay algo que guardar")
			settings = QtCore.QSettings('Settings/archivo.ini', QtCore.QSettings.NativeFormat)
			settings.setValue("mylist",self.mylist)
			settings.setValue("mylabel",self.mylabel)

	flagDelete = False
	def deletePage(self): #borrar y actualizar valores de tabs
		print("DeletePage")
		self.count = self.count - 1
		print("COUNT:",self.count)
		x = self.tabWidget.currentIndex()
		print("index:",x)

		self.tabWidget.removeTab(x)
		

		#if self.verticalLayout.
		#	print("tab1Ve")
			#self.verticalLayout.removeWidget()

		y = self.tabWidget.count()
		print("tabC:",y)

		dif = y - x
		
		for k in range(0,dif+1):
			#print("k:",k)
			j = k + 1
			print("x+k",x+k)
			#print("x+j:",x+j)
			self.tabWidget.setTabText(x+k,"Page"+str(x+j))

			for i in range(0,len(self.mylist)-1,4):
				#if self.mylist[i] == '0'+str(x+1)+'%':
				#	self.tempCut.append(self.mylist[i]+self.mylist[i+1]+'/'+self.mylist[i+2]+"\n"+self.mylist[i+3])
				if self.mylist[i] == '0'+str(x+j)+'%':
					#print("cambia valor tabList")
					self.flagDelete = True
					self.tempCut.append(self.mylist[i]+self.mylist[i+1]+'/'+self.mylist[i+2]+"\n"+self.mylist[i+3])
					if k != 0:
						self.tempTabsList.append(self.mylist[i])
						self.tempTabsList.append(self.mylist[i+1])
						self.tempTabsList.append(self.mylist[i+2])
						self.tempTabsList.append(self.mylist[i+3])

			for i in range(0,len(self.mylabel)-1,3):
				#if self.mylabel[i] == '0'+str(x+1)+'%':
				#	self.tempCut.append(self.mylabel[i]+self.mylabel[i+1]+'/'+self.mylabel[i+2])
				if self.mylabel[i] == '0'+str(x+j)+'%': #x+2
					#print("cambia valor tabLabel")
					self.flagDelete = True
					self.tempCut.append(self.mylabel[i]+self.mylabel[i+1]+'/'+self.mylabel[i+2])
					if k != 0:
						self.tempTabsLabel.append(self.mylabel[i])
						self.tempTabsLabel.append(self.mylabel[i+1])
						self.tempTabsLabel.append(self.mylabel[i+2])

		self.cleanMylist()
		self.tempCut.clear()

		if self.flagDelete != False:
			self.flagDelete = False
			#print("TempTabslist:",self.tempTabsList)
			#print("TempTabslabel:",self.tempTabsLabel)
			
			for k in range(0,dif):
				#print("k2:",k)
				j = k + 2
				df = x+j
				#print("2x+j:",x+j)
				
				for i in range(0,len(self.tempTabsList),4):
					if  self.tempTabsList[i] == '0'+str(x+j)+'%':
						self.mylist.append('0'+str(df-1)+'%')
						self.mylist.append(self.tempTabsList[i+1])
						self.mylist.append(self.tempTabsList[i+2])
						self.mylist.append(self.tempTabsList[i+3])

				for i in range(0,len(self.tempTabsLabel),3):
					if  self.tempTabsLabel[i] == '0'+str(x+j)+'%':
						self.mylabel.append('0'+str(df-1)+'%')
						self.mylabel.append(self.tempTabsLabel[i+1])
						self.mylabel.append(self.tempTabsLabel[i+2])

		self.tempTabsList.clear()
		self.tempTabsLabel.clear()

	def exitLayout(self):
		print("Exit") 
		cl = QtGui.QCloseEvent 
		self.closeEvent(cl)
		'''
		if (len(self.mylist) != 0 or len(self.mylabel) != 0) and self.flagSave != True: 
			if self.settingsList != self.mylist or self.settingsLabel != self.mylabel:
				print("se han hecho cambios y no se ha guardado")
				msgExit = QtWidgets.QMessageBox()
				returnExit = msgExit.warning(self.MainWindow,'Warning','Do you want to save changes?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Cancel)
				if returnExit == msgExit.Yes:
					self.saveLayout()
					MainWindow.close()
				if returnExit == msgExit.No:
					MainWindow.close()
			else:
				MainWindow.close()
		else:
			MainWindow.close()
		'''

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
