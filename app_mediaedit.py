# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_mediaedit import Ui_MediaEdit
import time
from database import Media, Root

class MediaEditDialog(QtWidgets.QDialog, Ui_MediaEdit):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=MediaEditDialog()
	win.show()
	sys.exit(app.exec_())
