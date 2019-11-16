#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_word import Ui_Word
import time
import locale
from app_work import Web
from app_usage import UsageDialog
from app_encounter import EncounterDialog
from database import Session, Root, Media, Encounter
import parse

class Word(QtWidgets.QDialog, Ui_Word):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)

		self.session = Session()
		self.usage = UsageDialog()

		self.roots=self.session.query(Root).order_by(Root.root).all()
		self.media=self.session.query(Media).order_by(Media.name).all()

		self.encDialog=EncounterDialog(self)
		self.encDialog.setwords(self.roots)
		self.encDialog.setmedia(self.media)
		self.encDialog.accepted.connect(self.acceptenc)
		self.newButton.clicked.connect(self.newenc)
		self.editButton.clicked.connect(self.editenc)
		self.deleteButton.clicked.connect(self.delenc)

		#self.wordLine.editingFinished.connect(self.search)		
		self.searchButton.clicked.connect(self.search)		
		self.downloadButton.clicked.connect(self.download)		
		self.wordTable.cellDoubleClicked.connect(self.open_usage)		
		self.wordTable.currentCellChanged.connect(self.setenc)		

	def delenc(self):
		row=self.encountersTable.currentRow()
		cell=self.encountersTable.item(row,0)
		self.encounter=cell.data(QtCore.Qt.UserRole)
		self.session.delete(self.encounter)
		self.session.commit()
		self.search()

	def newenc(self):
		row=self.wordTable.currentRow()
		cell=self.wordTable.item(row,0)
		root=cell.data(QtCore.Qt.UserRole)
		self.encounter=Encounter(root=root,skill=60,notes="Put Notes Here")
		self.encDialog.setdata(self.encounter)
		print(self.encounter)
		self.encDialog.show()

	def editenc(self):
		row=self.encountersTable.currentRow()
		cell=self.encountersTable.item(row,0)
		self.encounter=cell.data(QtCore.Qt.UserRole)
		self.encDialog.setdata(self.encounter)
		self.encDialog.show()

	def acceptenc(self):
		print(self.encounter,self.encounter.root.root,self.encounter.media.name,self.encounter.skill)
		self.session.add(self.encounter)
		self.session.commit()
		self.search()

	def setenc(self,row,col):
		print("setenc",row,col)
		if row<0:
			return
		cell=self.wordTable.item(row,0)
		root=cell.data(QtCore.Qt.UserRole)
		for _ in range(self.encountersTable.rowCount()):
			self.encountersTable.removeRow(0)
		for row, encounter in enumerate(root.encounters):
			self.encountersTable.insertRow(row)
			cell=QtWidgets.QTableWidgetItem(encounter.media.name)
			cell.setData(QtCore.Qt.UserRole, encounter)
			self.encountersTable.setItem(row,0, cell)
			self.encountersTable.setItem(row,1,
				QtWidgets.QTableWidgetItem(encounter.encounter_time.strftime('%Y-%m-%d')))
			self.encountersTable.setItem(row,2,
				QtWidgets.QTableWidgetItem(str(encounter.skill)))
			
	def open_usage(self,row,col):
		tgt=self.wordTable.item(row,0).text()
		self.usage.settext(tgt)
		self.usage.show()

	def search(self):
		snip=self.wordLine.text()
		self.words=self.session.query(Root).filter(Root.root.like("%{}%".format(snip))).order_by(Root.root).all()
		self.words=sorted(self.words, key=lambda r: locale.strxfrm(r.root))
		
		for _ in range(self.wordTable.rowCount()):
			self.wordTable.removeRow(0)

		for cnt,root in enumerate(self.words):
			self.wordTable.insertRow(cnt)
			cell=QtWidgets.QTableWidgetItem(root.root)
			cell.setData(QtCore.Qt.UserRole, root)
			red=green=blue=255
			if root.usages and root.usages[0].grammar:
				gram=root.usages[0].grammar
				if 'masc' in gram:
					red = red-25
					green = green-25
				if 'minin' in gram:
					green = green -25
					blue = blue - 25
			cell.setBackground(QtGui.QColor(red,green,blue))
			self.wordTable.setItem(cnt,0, cell)
			self.wordTable.setItem(cnt,1, QtWidgets.QTableWidgetItem(root.importance))
			# Calculate skill and date from encounters
			encdate=root.created.strftime("%Y-%m-%d")
			self.wordTable.setItem(cnt,4,QtWidgets.QTableWidgetItem(encdate))
		
		if len(self.words)>0:
			self.wordTable.setCurrentCell(0,0)	

	def download(self):
		snip=self.wordLine.text()
		parse.download(snip)



if __name__ == "__main__":
	import sys
	import signal

	signal.signal(signal.SIGINT, signal.SIG_DFL)
	locale.setlocale(locale.LC_ALL,'fr_FR.utf8')

	app = QtWidgets.QApplication(sys.argv)
	win=Word()
	win.show()
	sys.exit(app.exec_())
