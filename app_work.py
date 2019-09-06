# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import requests
from lxml import html

class Web(QtCore.QObject):

	loaded=QtCore.pyqtSignal()

	def __init__(self, parent=None):
		super(QtCore.QObject,self).__init__(parent)
		self.base="https://www.larousse.fr/dictionnaires/francais-anglais"

	def load(self, word):
		req=requests.get("{0}/{1}".format(self.base,word))
		if req.status_code==200:
			tree=html.fromstring(req.content)
			print(tree)			
		self.loaded.emit()

if __name__ == "__main__":
	import sys
	win=Web()
	win.load("bonjour")

