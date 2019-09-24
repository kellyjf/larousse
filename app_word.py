# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_word import Ui_Word
import time
from app_work import Web
from app_usage import UsageDialog
from database import Session, Root
import parse

class Word(QtWidgets.QDialog, Ui_Word):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)

		self.session = Session()
		self.usage = UsageDialog()
		#self.wordLine.editingFinished.connect(self.search)		
		self.searchButton.clicked.connect(self.search)		
		self.downloadButton.clicked.connect(self.download)		
		self.wordTable.cellDoubleClicked.connect(self.open_usage)		

	def open_usage(self,row,col):
		tgt=self.wordTable.item(row,0).text()
		self.usage.settext(tgt)
		self.usage.show()

	def search(self):
		snip=self.wordLine.text()
		self.words=self.session.query(Root).filter(Root.root.like("%{}%".format(snip))).order_by(Root.root).all()
		
		for _ in range(self.wordTable.rowCount()):
			self.wordTable.removeRow(0)

		for cnt,root in enumerate(self.words):
			self.wordTable.insertRow(cnt)
			self.wordTable.setItem(cnt,0, QtWidgets.QTableWidgetItem(root.root))
			self.wordTable.setItem(cnt,1, QtWidgets.QTableWidgetItem(root.importance))
			self.wordTable.setItem(cnt,2, QtWidgets.QTableWidgetItem(root.skill))
			encdate=root.created.strftime("%Y-%m-%d")
			self.wordTable.setItem(cnt,4,QtWidgets.QTableWidgetItem(encdate))

	def download(self):
		snip=self.wordLine.text()
		parse.download(snip)



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=Word()
	win.show()
	sys.exit(app.exec_())
