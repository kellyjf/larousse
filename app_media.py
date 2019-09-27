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
from database import Media, Session, Encounter

class MediaDialog(QtWidgets.QDialog, Ui_Media):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)
		self.session=Session()
		self.editDialog=MediaEditDialog(self)
		self.editDialog.accepted.connect(self.accepted)
		self.searchButton.clicked.connect(self.search)
		self.editButton.clicked.connect(self.editmedia)

	def accepted(self):
		self.session.commit()

	def editmedia(self):
		row=self.mediaTable.currentRow()
		self.subject=self.medialist[row]

		if row>-1:
			self.editDialog.setmedia(self.subject)
			self.editDialog.show()

	def search(self):
		snip=self.wordLine.text()
		self.medialist=self.session.query(Media).filter(Media.name.like("%{}%".format(snip))).order_by(Media.name).all()
		
		for _ in range(self.mediaTable.rowCount()):
			self.mediaTable.removeRow(0)

		for cnt,media in enumerate(self.medialist):
			self.mediaTable.insertRow(cnt)
			self.mediaTable.setItem(cnt,0, QtWidgets.QTableWidgetItem(media.name))
			# Calculate skill and date from encounters
			print("LEN",len(media.encounters))
			encdate=media.created.strftime("%Y-%m-%d")
			self.mediaTable.setItem(cnt,4,QtWidgets.QTableWidgetItem(encdate))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=MediaDialog()
	win.show()
	sys.exit(app.exec_())
