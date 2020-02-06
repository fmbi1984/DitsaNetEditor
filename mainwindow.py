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
		

		self.MainWindow = MainWindow

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		#self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
		#self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

		self.newtb = QtWidgets.QAction(QtGui.QIcon('image/nuevo.png'),'New',MainWindow)
		self.savetb = QtWidgets.QAction(QtGui.QIcon('image/guardar.png'),'Save',MainWindow)
		self.deletetb = QtWidgets.QAction(QtGui.QIcon('image/borrar.png'),'Delete',MainWindow)
		self.exittb = QtWidgets.QAction(QtGui.QIcon('image/salir.png'),'Exit',MainWindow)

		self.toolB = MainWindow.addToolBar('ToolBar')
		
		self.rbCM = QtWidgets.QRadioButton('Circuit Mode')
		self.rbLM = QtWidgets.QRadioButton('Label Mode')
		self.rbCM.setChecked(False)
		self.rbLM.setChecked(True)

		self.toolB.addWidget(self.rbCM)
		self.toolB.addWidget(self.rbLM)
		self.toolB.addAction(self.newtb)
		self.toolB.addAction(self.savetb)
		self.toolB.addAction(self.deletetb)
		self.toolB.addAction(self.exittb)

	def showEvent(self,event):
		print("ShowEvent")

	def closeEvent(self,event):
		print("CloseEvent")

	def tabSelected(self):
		print("tabSelect")
		
	def tableValue(self,sizeW,text,textAlign):
		vx = self.tableWidget.currentRow()
		vy = self.tableWidget.currentColumn()
		print("x1",vx)
		print("y1",vy)

		item = QtWidgets.QTableWidgetItem(text)
		lblt = QtGui.QFont("Arial",int(sizeW), QtGui.QFont.Black)

		if textAlign == 'AlignTop':
			item.setTextAlignment(QtCore.Qt.AlignTop)
			item.setFont(lblt)
		else:
			item.setTextAlignment(QtCore.Qt.AlignBottom)
			item.setFont(lblt)

		self.tableWidget.setItem(vx,vy,item)

		


	def on_cellClickedTableW(self):
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
				self.CircuitWindow = QtWidgets.QDialog()
				self.CircuitWindow.setModal(True)
				self.ui = Ui_NewCircuit()
				self.ui.setupUi(self.CircuitWindow)
				self.CircuitWindow.show()
			else:
				#self.LabelWindow = QtWidgets.QDialog()
				#self.LabelWindow.setModal(True)
				##self.ui2 = Ui_NewLabel(self.LabelWindow)
				#self.ui2.setupUi(self.LabelWindow)
				#self.ui2.__init__(self.LabelWindow)
				##self.LabelWindow.show()
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
