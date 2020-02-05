# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newcircuit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewCircuit(object):
    def setupUi(self, NewCircuit):
        NewCircuit.setObjectName("NewCircuit")
        NewCircuit.resize(268, 186)
        self.widget = QtWidgets.QWidget(NewCircuit)
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
        self.horizontalLayout_2.addWidget(self.lineAddrs)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(NewCircuit)
        self.buttonBox.accepted.connect(NewCircuit.accept)
        self.buttonBox.rejected.connect(NewCircuit.reject)
        QtCore.QMetaObject.connectSlotsByName(NewCircuit)

    def retranslateUi(self, NewCircuit):
        _translate = QtCore.QCoreApplication.translate
        NewCircuit.setWindowTitle(_translate("NewCircuit", "Dialog"))
        self.lblName.setText(_translate("NewCircuit", "Name    "))
        self.lblAddrs.setText(_translate("NewCircuit", "Address"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewCircuit = QtWidgets.QDialog()
    ui = Ui_NewCircuit()
    ui.setupUi(NewCircuit)
    NewCircuit.show()
    sys.exit(app.exec_())
