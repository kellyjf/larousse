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

	def setwords(self,matches):
		for _ in range(self.wordCombo.count()):
			self.wordCombo.removeRow(0)
		for row,match in enumerate(matches):
			self.wordCombo.insertItem(row,match.root,match)

	def setmedia(self,media):
		for _ in range(self.mediaCombo.count()):
			self.mediaCombo.removeRow(0)
		for row,medium in enumerate(media):
			self.mediaCombo.insertItem(row,medium.name,medium)

	def setdata(self,encounter):
		if encounter.root:
			self.wordCombo.setEditText(encounter.root.root)
			row=self.wordCombo.findText(encounter.root.root)
			if row>-1:
				self.wordCombo.setCurrentIndex(row)
		if encounter.media:
			self.mediaCombo.setEditText(encounter.media.name)
			row=self.mediaCombo.findText(encounter.media.name)
			if row>-1:
				self.mediaCombo.setCurrentIndex(row)
		self.skillSpin.setValue(encounter.skill)
		self.enc=encounter

	def accept(self):
		root=self.wordCombo.itemData(self.wordCombo.currentIndex())
		media=self.mediaCombo.itemData(self.mediaCombo.currentIndex())
		skill=self.skillSpin.value()
		cdate=self.encounterDate.date()
		edate=date(cdate.year(),cdate.month(),cdate.day())

		self.enc.root=root
		self.enc.media=media
		self.enc.skill=skill
		self.enc.encounter_time=edate
		self.enc.notes=self.notesText.toPlainText()

		super(type(self),self).accept()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=EncounterDialog()
	win.show()
	sys.exit(app.exec_())
