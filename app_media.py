#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_media import Ui_Media
from app_mediaedit import MediaEditDialog
from app_encounter import EncounterDialog
from app_usage import UsageDialog
from database import Media, Session, Encounter, Root
from datetime import datetime
import locale

class MediaDialog(QtWidgets.QDialog, Ui_Media):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)
		self.session=Session()
		self.usage=UsageDialog(session=self.session)
		self.roots=sorted(self.session.query(Root).order_by(Root.root).all(), key=lambda r:locale.strxfrm(r.root))
		self.media=self.session.query(Media).order_by(Media.name).all()

		self.encDialog=EncounterDialog(self)
		self.encDialog.setwords(self.roots)
		self.encDialog.setmedia(self.media)
		self.encDialog.accepted.connect(self.acceptenc)
		self.newEncButton.clicked.connect(self.newenc)
		self.editEncButton.clicked.connect(self.editenc)
		self.deleteEncButton.clicked.connect(self.delenc)

		self.editDialog=MediaEditDialog(self)
		self.editDialog.accepted.connect(self.acceptmed)
		self.searchButton.clicked.connect(self.search)
		self.editButton.clicked.connect(self.editmedia)
		self.newButton.clicked.connect(self.newmedia)
		self.deleteButton.clicked.connect(self.delmedia)
		self.mediaTable.currentCellChanged.connect(self.changed)
		self.mediaTable.setColumnWidth(0,200)
		self.encDialog.saveandnew.connect(self.encapply)
		self.encountersTable.cellDoubleClicked.connect(self.openword)

		self.search()

	def openword(self, row, col):
		cell=self.encountersTable.item(row,0)
		encounter=cell.data(QtCore.Qt.UserRole)
		self.usage.settext(encounter.root.root)
		self.usage.show()
		print("Openword",encounter.root.root)	
	def encapply(self):
		self.session.add(self.encounter)
		self.session.commit()
		self.newenc()

	def delenc(self):
		row=self.encountersTable.currentRow()
		cell=self.encountersTable.item(row,0)
		self.encounter=cell.data(QtCore.Qt.UserRole)
		self.session.delete(self.encounter)
		self.session.commit()
		self.search()

	def newenc(self):
		row=self.mediaTable.currentRow()
		cell=self.mediaTable.item(row,0)
		media=cell.data(QtCore.Qt.UserRole)
		self.encounter=Encounter(media=media,skill=60,notes="Put Notes Here")
		self.encDialog.setdata(self.encounter)
		self.encDialog.show()

	def editenc(self):
		row=self.encountersTable.currentRow()
		cell=self.encountersTable.item(row,0)
		self.encounter=cell.data(QtCore.Qt.UserRole)
		self.encDialog.setdata(self.encounter)
		self.encDialog.show()

	def acceptenc(self):
		self.session.add(self.encounter)
		self.session.commit()
		self.search()

	def changed(self):
		row=self.mediaTable.currentRow()
		if row>-1:
			cell=self.mediaTable.item(row,0)
			media=cell.data(QtCore.Qt.UserRole)
			self.notesText.setText(media.notes)
			for _ in range(self.encountersTable.rowCount()):
				self.encountersTable.removeRow(0)
			for ndx,encounter in enumerate(media.encounters):
				self.encountersTable.insertRow(ndx)
				cell=QtWidgets.QTableWidgetItem(encounter.root.root)
				cell.setData(QtCore.Qt.UserRole,encounter)
				self.encountersTable.setItem(ndx,0,cell)
				self.encountersTable.setItem(ndx,1,
					QtWidgets.QTableWidgetItem(encounter.encounter_time.strftime('%y-%m-%d')))
				self.encountersTable.setItem(ndx,2,
					QtWidgets.QTableWidgetItem(str(encounter.skill)))

	def delmedia(self):
		row=self.mediaTable.currentRow()
		cell=self.mediaTable.item(row,0)
		self.subject=cell.data(QtCore.Qt.UserRole)
		self.session.delete(self.subject)
		self.session.commit()
		self.search()

	def acceptmed(self):
		self.session.add(self.subject)
		self.session.commit()
		self.search()

	def newmedia(self):
		self.subject=Media(created=datetime.now())
		self.editDialog.setmedia(self.subject)
		self.editDialog.show()

	def editmedia(self):
		row=self.mediaTable.currentRow()
		if row>-1:
			cell=self.mediaTable.item(row,0)
			self.subject=cell.data(QtCore.Qt.UserRole)
			self.editDialog.setmedia(self.subject)
			self.editDialog.show()

	def search(self):
		snip=self.wordLine.text()
		self.medialist=self.session.query(Media).filter(Media.name.like("%{}%".format(snip))).order_by(Media.name).all()
		
		for _ in range(self.mediaTable.rowCount()):
			self.mediaTable.removeRow(0)

		for cnt,media in enumerate(self.medialist):
			self.mediaTable.insertRow(cnt)
			cell=QtWidgets.QTableWidgetItem(media.name)
			cell.setData(QtCore.Qt.UserRole,media)
			self.mediaTable.setItem(cnt,0, cell)

			# Calculate skill and date from encounters
			encdate=media.created.strftime("%Y-%m-%d")
			self.mediaTable.setItem(cnt,4,QtWidgets.QTableWidgetItem(encdate))

		if self.mediaTable.rowCount()>0:
			self.mediaTable.setCurrentCell(0,0)
if __name__ == "__main__":
	import sys
	import signal

	signal.signal(signal.SIGINT, signal.SIG_DFL)
	locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
	app = QtWidgets.QApplication(sys.argv)
	win=MediaDialog()
	win.show()
	sys.exit(app.exec_())
