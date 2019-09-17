# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_vowels import Ui_Vowels
from database import *

class SButton(QtWidgets.QPushButton):
	notify = QtCore.pyqtSignal(str)
	def __init__(self, parent):
		super(QtWidgets.QPushButton, self).__init__(parent)
		self.clicked.connect(self.sendit)
	def sendit(self):
		self.notify.emit(self.text())

class Sub(QtWidgets.QHBoxLayout):
	def __init__(self, parent, lblunr, lblrnd):
		super(QtWidgets.QHBoxLayout, self).__init__()

		if lblunr:
			unr=SButton(parent)
			unr.setText(lblunr)
			unr.setStyleSheet("background-color: rgb(180,180,200);")
			unr.notify.connect(parent.click)
			self.addWidget(unr)
		if lblrnd:
			rnd=SButton(parent)
			rnd.setStyleSheet("background-color: rgb(200,180,180);")
			rnd.notify.connect(parent.click)
			rnd.setText(lblrnd)
			self.addWidget(rnd)
	
	
class Vowels(QtWidgets.QDialog, Ui_Vowels):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)

		self.session=Session()
		self.clearButton.clicked.connect(self.searchLine.clear)
		self.searchButton.clicked.connect(self.search)


		row=0
		self.gridLayout.addLayout(Sub(self,'i','y'),row,0,1,1)
		self.gridLayout.addLayout(Sub(self,None,"u"),row,4,1,1)

		row=row+1
		self.gridLayout.addLayout(Sub(self,'e','ø'),row,1,1,1)
		self.gridLayout.addLayout(Sub(self,"\u0259",None),row,3,1,1)
		self.gridLayout.addLayout(Sub(self,None,"o"),row,4,1,1)

		row=row+1
		self.gridLayout.addLayout(Sub(self,"\u025b","\u0153"),row,2,1,1)
		self.gridLayout.addLayout(Sub(self,None,"\u0254"),row,4,1,1)
		self.gridLayout.addLayout(Sub(self,None,"\u0254"),row,4,1,1)

		row=row+1
		self.gridLayout.addLayout(Sub(self,"\u025b\u0303","\u0153\u0303"),row,2,1,1)
		self.gridLayout.addLayout(Sub(self,None,"\u0254\u0303"),row,4,1,1)

		row=row+1
		self.gridLayout.addLayout(Sub(self,"\u0061","\u0276"),row,3,1,1)
		self.gridLayout.addLayout(Sub(self,"\u0251","\u0252"),row,4,1,1)

		row=row+1
		self.gridLayout.addLayout(Sub(self,"\u0251\u0303",None),row,4,1,1)

	def click(self, lbl="Empty"):
		self.searchLine.insert(lbl)
		print("Click",lbl)

	def search(self):
		snip=self.searchLine.text()
		res=self.session.query(Usage).filter(Usage.phonetic.like("%{}%".format(snip)))
		for _ in range(self.resultTable.rowCount()):
			self.resultTable.removeRow(0)
		for cnt,ans in enumerate(res):
			self.resultTable.insertRow(cnt)
			self.resultTable.setItem(cnt,0,QtWidgets.QTableWidgetItem(ans.address))
			self.resultTable.setItem(cnt,1,QtWidgets.QTableWidgetItem(ans.phonetic))
			self.resultTable.setItem(cnt,2,QtWidgets.QTableWidgetItem(ans.grammar))

		print([x.root for x in res])
			
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=Vowels()
	win.show()
	sys.exit(app.exec_())
