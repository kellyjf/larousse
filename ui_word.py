# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Word(object):
	def setupUi(self, Word):
		Word.setObjectName("Word")
		Word.resize(482, 389)
		self.verticalLayout = QtWidgets.QVBoxLayout(Word)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.findCombo = QtWidgets.QComboBox(Word)
		self.findCombo.setEditable(True)
		self.findCombo.setObjectName("findCombo")
		self.horizontalLayout.addWidget(self.findCombo)
		self.loadButton = QtWidgets.QPushButton(Word)
		self.loadButton.setObjectName("loadButton")
		self.horizontalLayout.addWidget(self.loadButton)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.mainTable = QtWidgets.QTableWidget(Word)
		self.mainTable.setObjectName("mainTable")
		self.mainTable.setColumnCount(2)
		self.mainTable.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.mainTable.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.mainTable.setHorizontalHeaderItem(1, item)
		self.verticalLayout.addWidget(self.mainTable)
		self.buttonBox = QtWidgets.QDialogButtonBox(Word)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(Word)
		self.buttonBox.accepted.connect(Word.accept)
		self.buttonBox.rejected.connect(Word.reject)
		QtCore.QMetaObject.connectSlotsByName(Word)

	def retranslateUi(self, Word):
		_translate = QtCore.QCoreApplication.translate
		Word.setWindowTitle(_translate("Word", "Word Definitiions"))
		self.loadButton.setText(_translate("Word", "&Load"))
		item = self.mainTable.horizontalHeaderItem(0)
		item.setText(_translate("Word", "Name"))
		item = self.mainTable.horizontalHeaderItem(1)
		item.setText(_translate("Word", "Definition"))


