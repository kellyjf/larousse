# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_vowels import Ui_Vowels

class Sub(QtWidgets.QHBoxLayout):
	def __init__(self, parent, lblunr, lblrnd):
		super(QtWidgets.QHBoxLayout, self).__init__(parent)

		unr=QtWidgets.QPushButton(parent)
		unr.setText(lblunr)
		rnd=QtWidgets.QPushButton(parent)
		rnd.setText(lblrnd)
	
		self.addWidget(unr)
		self.addWidget(rnd)
	
class Vowels(QtWidgets.QDialog, Ui_Vowels):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)
		self.gridLayout.addLayout(Sub(self,'i','y'),0,0,1,1)
		self.gridLayout.addLayout(Sub(self,'e','ø'),1,1,1,1)
		self.gridLayout.addLayout(Sub(self,"\u025b","\u0153"),2,2,1,1)
		self.gridLayout.addLayout(Sub(self,"\u0061","\u0276"),3,3,1,1)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=Vowels()
	win.show()
	sys.exit(app.exec_())
