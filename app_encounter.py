#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_encounter import Ui_Encounter
import time
from database import Encounter, Root

class EncounterDialog(QtWidgets.QDialog, Ui_Encounter):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=EncounterDialog()
	win.show()
	sys.exit(app.exec_())
