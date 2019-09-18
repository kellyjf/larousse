# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_usage import Ui_Usage
from database import *

	
class UsageDialog(QtWidgets.QDialog, Ui_Usage):
	def __init__(self, parent=None, word=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)

		self.session=Session()
		self.searchButton.clicked.connect(self.search)
		self.usageTable.cellDoubleClicked.connect(self.setusage)
		if word:
			self.wordLine.setText(word)
			self.search()

	def search(self):
		snip=self.wordLine.text()
		self.root=self.session.query(Root).filter(Root.root==snip).first()

		for _ in range(self.usageTable.rowCount()):
			self.usageTable.removeRow(0)
		res=[]
		if self.root:
			res=self.root.usages

		for cnt,ans in enumerate(res):
			self.usageTable.insertRow(cnt)
			self.usageTable.setItem(cnt,0,QtWidgets.QTableWidgetItem(ans.address))
			self.usageTable.setItem(cnt,1,QtWidgets.QTableWidgetItem(ans.phonetic))
			self.usageTable.setItem(cnt,2,QtWidgets.QTableWidgetItem(ans.grammar))

		
	def setusage(self,row,col):
		print(row,col)
		self.usage=self.root.usages[row]
		self.meanings=self.usage.meanings

		for _ in range(self.meaningTable.rowCount()):
			self.meaningTable.removeRow(0)
		for cnt,ans in enumerate(self.meanings):
			self.meaningTable.insertRow(cnt)
			self.meaningTable.setItem(cnt,0,QtWidgets.QTableWidgetItem(ans.meaning))
		
	
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=UsageDialog(word='avoir')
	win.show()
	sys.exit(app.exec_())
