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
		Word.resize(673, 511)
		self.verticalLayout = QtWidgets.QVBoxLayout(Word)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.label = QtWidgets.QLabel(Word)
		self.label.setObjectName("label")
		self.horizontalLayout_2.addWidget(self.label)
		self.wordLine = QtWidgets.QLineEdit(Word)
		self.wordLine.setObjectName("wordLine")
		self.horizontalLayout_2.addWidget(self.wordLine)
		self.grammarCombo = QtWidgets.QComboBox(Word)
		self.grammarCombo.setObjectName("grammarCombo")
		self.horizontalLayout_2.addWidget(self.grammarCombo)
		self.searchButton = QtWidgets.QPushButton(Word)
		self.searchButton.setDefault(True)
		self.searchButton.setObjectName("searchButton")
		self.horizontalLayout_2.addWidget(self.searchButton)
		self.downloadButton = QtWidgets.QPushButton(Word)
		self.downloadButton.setObjectName("downloadButton")
		self.horizontalLayout_2.addWidget(self.downloadButton)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		self.wordTable = QtWidgets.QTableWidget(Word)
		self.wordTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.wordTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.wordTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.wordTable.setObjectName("wordTable")
		self.wordTable.setColumnCount(5)
		self.wordTable.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.wordTable.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.wordTable.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.wordTable.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.wordTable.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.wordTable.setHorizontalHeaderItem(4, item)
		self.wordTable.horizontalHeader().setStretchLastSection(True)
		self.verticalLayout.addWidget(self.wordTable)
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
		Word.setWindowTitle(_translate("Word", "Words"))
		self.label.setText(_translate("Word", "Word"))
		self.searchButton.setText(_translate("Word", "Search"))
		self.downloadButton.setText(_translate("Word", "Download"))
		self.wordTable.setSortingEnabled(True)
		item = self.wordTable.horizontalHeaderItem(0)
		item.setText(_translate("Word", "Word"))
		item = self.wordTable.horizontalHeaderItem(1)
		item.setText(_translate("Word", "Importance"))
		item = self.wordTable.horizontalHeaderItem(2)
		item.setText(_translate("Word", "Skill"))
		item = self.wordTable.horizontalHeaderItem(3)
		item.setText(_translate("Word", "Visits"))
		item = self.wordTable.horizontalHeaderItem(4)
		item.setText(_translate("Word", "Latest"))


