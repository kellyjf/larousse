#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_usage import Ui_Usage
from database import *
import os
import parse
import locale
	
class UsageDialog(QtWidgets.QDialog, Ui_Usage):
	def __init__(self, parent=None, word=None, session=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)

		if session:
			self.session=session
		else:
			self.session=Session()

		self.wordLine.editingFinished.connect(self.search)
		self.searchButton.clicked.connect(self.search)
		self.downloadButton.clicked.connect(self.download)
		self.usageTable.cellClicked.connect(self.setusage)
		self.meaningTable.cellClicked.connect(self.setmeaning)
		self.exampleTable.cellDoubleClicked.connect(self.setexample)
		self.exampleTree.itemDoubleClicked.connect(self.tsetexample)
		self.exampleTree.setColumnWidth(0,300)
		self.exampleTree.setColumnWidth(1,300)
		self.playButton.clicked.connect(self.rsetexample)
		self.populate_combo()
		self.grammarCombo.currentIndexChanged[str].connect(self.setgrammar)
		self.showExButton.clicked.connect(self.showtext)
		self.showTrButton.clicked.connect(self.showtext)
		self.nextButton.clicked.connect(self.movereview)

		if word:
			self.wordLine.setText(word)
			self.search()

	def showtext(self, widget=None):
		if not self.review:
			return
		if self.showExButton.isChecked():
			self.exampleText.setText(self.review[self.rcnt].expression)
		else:
			self.exampleText.setText("")

		if self.showTrButton.isChecked():
			self.transText.setText(self.review[self.rcnt].translation)
		else:
			self.transText.setText("")

	def settext(self, word):
		self.grammarCombo.setCurrentIndex(0)
		self.wordLine.setText(word)
		self.search()

	def setgrammar(self, ndx):
		self.wordLine.clear()
		self.search()

	def populate_combo(self):
		opts=self.session.query(Usage.grammar).group_by("grammar").order_by("grammar").all()
		self.grammarCombo.clear()
		self.grammarCombo.insertItem(0,"")
		for cnt,grammar in enumerate([x[0] for x in opts if x[0]]):
			self.grammarCombo.insertItem(cnt+1,grammar)


	def tsearch(self, usages):
		self.exampleTree.clear()
		self.exampleTree.invisibleRootItem().setExpanded(True)
		self.review=[]
		for cnt,usage in enumerate(self.usages):
			uitem=QtWidgets.QTreeWidgetItem([usage.address,usage.phonetic])
			self.exampleTree.insertTopLevelItem(cnt,uitem)
			uitem.setExpanded(True)
			for mcnt,meaning in enumerate(usage.meanings):
				mitem=QtWidgets.QTreeWidgetItem(uitem,[meaning.meaning])
				mitem.setExpanded(True)
				for ecnt,example in enumerate(meaning.examples):
					eitem=QtWidgets.QTreeWidgetItem(mitem,[example.expression,example.translation])
					eitem.setData(0,QtCore.Qt.UserRole,example)
					self.review.append(example)

		self.rcnt=-1
		self.movereview()

	def movereview(self):
		self.numLabel.setText("{:d} of {:d}".format(self.rcnt+1,len(self.review)))
		if self.review:
			self.rcnt=(self.rcnt+1)%(len(self.review))
		self.showExButton.setChecked(False)
		self.showTrButton.setChecked(False)
		self.showtext()

	def search(self):
		snip=self.wordLine.text()
		gram=self.grammarCombo.currentText()

		for _ in range(self.usageTable.rowCount()):
			self.usageTable.removeRow(0)

		self.usage=[]
		if snip:
			self.root=self.session.query(Root).filter(Root.root==snip).first()
			if not self.root:
				return
			self.usages=self.root.usages
		elif gram:
			self.usages=self.session.query(Usage).filter(Usage.grammar==gram).all()

		self.tsearch(self.usages)

		for cnt,usage in enumerate(self.usages):
			self.usageTable.insertRow(cnt)
			cell=QtWidgets.QTableWidgetItem(usage.address)
			cell.setData(QtCore.Qt.UserRole,usage)
			self.usageTable.setItem(cnt,0,cell)
			self.usageTable.setItem(cnt,1,QtWidgets.QTableWidgetItem(usage.phonetic))
			self.usageTable.setItem(cnt,2,QtWidgets.QTableWidgetItem(usage.grammar))

		self.usageTable.setCurrentCell(0,0)
		self.setusage(0,0)
	
	def setusage(self,row,col):
		cell=self.usageTable.item(row,0)
		usage=cell.data(QtCore.Qt.UserRole)	

		for _ in range(self.meaningTable.rowCount()):
			self.meaningTable.removeRow(0)
		for cnt,meaning in enumerate(usage.meanings):
			self.meaningTable.insertRow(cnt)
			cell=QtWidgets.QTableWidgetItem(meaning.meaning)
			cell.setData(QtCore.Qt.UserRole,meaning)
			self.meaningTable.setItem(cnt,0,cell)
		self.meaningTable.setCurrentCell(0,0)
		self.setmeaning(0,0)	
		
	def setmeaning(self,row,col):
		cell=self.meaningTable.item(row,0)
		meaning=cell.data(QtCore.Qt.UserRole)	
		for _ in range(self.exampleTable.rowCount()):
			self.exampleTable.removeRow(0)
		for cnt,example in enumerate(meaning.examples):
			self.exampleTable.insertRow(cnt)
			cell=QtWidgets.QTableWidgetItem(example.expression)
			cell.setData(QtCore.Qt.UserRole,example)
			self.exampleTable.setItem(cnt,0,cell)
			self.exampleTable.setItem(cnt,1,QtWidgets.QTableWidgetItem(example.translation))
		
	def playexample(self,example):
		if example and example.lienson:
			path=example.lienson.split("/")
			os.system("mpg123 audio/"+path[-1])
	
	def setexample(self,row,col):
		cell=self.exampleTable.item(row,0)
		self.playexample(cell.data(QtCore.Qt.UserRole))

	def tsetexample(self,item,col):
		self.playexample(item.data(0,QtCore.Qt.UserRole))

	def rsetexample(self):
		self.playexample(self.review[self.rcnt])

	def download(self):
		snip=self.wordLine.text()
		parse.download(snip)

	
if __name__ == "__main__":
	import sys
	import signal
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	locale.setlocale('fr_FR.utf8')
	app = QtWidgets.QApplication(sys.argv)
	if len(sys.argv)>1:
		win=UsageDialog(word=sys.argv[1])
	else:
		win=UsageDialog(word='avoir')
	win.show()
	sys.exit(app.exec_())
