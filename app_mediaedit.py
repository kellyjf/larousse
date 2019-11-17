#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_mediaedit import Ui_MediaEdit
from datetime import date, datetime
from database import Media, Root, Session

#
class MediaEditDialog(QtWidgets.QDialog, Ui_MediaEdit):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)

	def setmedia(self,media):
		self.media=media
		self.nameLine.setText(media.name)
		self.urlLine.setText(media.url)
		self.createdDate.setDate(QtCore.QDate(media.created.year,media.created.month,media.created.day))
		self.notesText.setText(media.notes)

	def accept(self):
		self.media.name=self.nameLine.text()
		self.media.url=self.urlLine.text()
		cdate=self.createdDate.date()
		self.media.created=date(cdate.year(),cdate.month(),cdate.day())
		self.media.notes=self.notesText.toPlainText()

		print("accept")
		super(MediaEditDialog,self).accept()

	def reject(self):
		print("reject")
		super(MediaEditDialog,self).reject()
		

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=MediaEditDialog()
	win.setmedia(Media(created=datetime.now()))
	win.show()
	sys.exit(app.exec_())
