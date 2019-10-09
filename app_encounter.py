#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_encounter import Ui_Encounter
from datetime import datetime,date
from database import Encounter, Root, Media, Session

class EncounterDialog(QtWidgets.QDialog, Ui_Encounter):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)

		self.setupUi(self)
		self.session=Session()
		self.encounterDate.setDate(datetime.now())
		self.setword("")


	def setword(self,skey):

		self.wordCombo.clear()
		matches=self.session.query(Root).all()
		for row,match in enumerate(matches):
			self.wordCombo.insertItem(row,match.root,match)

		self.mediaCombo.clear()
		media=self.session.query(Media).all()
		for row,medium in enumerate(media):
			self.mediaCombo.insertItem(row,medium.name,medium)

	def accept(self):
		root=self.wordCombo.itemData(self.wordCombo.currentIndex())
		media=self.mediaCombo.itemData(self.mediaCombo.currentIndex())
		skill=self.skillSpin.value()
		cdate=self.encounterDate.date()
		edate=date(cdate.year(),cdate.month(),cdate.day())

		enc=Encounter(root=root,media=media,skill=skill,encounter_time=edate,notes=self.notesText.toPlainText())
		self.session.add(enc)
		self.session.commit()

		super(type(self),self).accept()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=EncounterDialog()
	win.show()
	sys.exit(app.exec_())
