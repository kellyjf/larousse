# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from local import get_tree

class Web(QtCore.QObject):

	loaded=QtCore.pyqtSignal()

	def __init__(self, parent=None):
		super(QtCore.QObject,self).__init__(parent)

	def load(self, word):
		tree=get_tree(word)
		print(tree)			
		self.loaded.emit()

if __name__ == "__main__":
	import sys
	win=Web()
	win.load("bonjour")

