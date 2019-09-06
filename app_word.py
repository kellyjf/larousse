# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_word import Ui_Word
import time

class Web(QtCore.QObject):
	loaded=QtCore.pyqtSignal()

	def __init__(self, parent=None):
		super(QtCore.QObject,self).__init__(parent)

	def run(self):
		time.sleep(20)
		self.loaded.emit()
	
class Word(QtWidgets.QDialog, Ui_Word):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)
		self.thread=QtCore.QThread()
		self.web=Web()
		self.web.moveToThread(self.thread)
		self.web.loaded.connect(self.loaded)
		self.thread.start()
		self.loadButton.clicked.connect(self.web.run)

	def loaded(self):
		print("Loaded")




if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=Word()
	win.show()
	sys.exit(app.exec_())
