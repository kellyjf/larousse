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

		if lblunr:
			unr=QtWidgets.QPushButton(parent)
			unr.setText(lblunr)
			unr.setStyleSheet("background-color: rgb(180,180,200);")
			self.addWidget(unr)
		if lblrnd:
			rnd=QtWidgets.QPushButton(parent)
			rnd.setStyleSheet("background-color: rgb(200,180,180);")
			rnd.setText(lblrnd)
			self.addWidget(rnd)
	
	
class Vowels(QtWidgets.QDialog, Ui_Vowels):
	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)
		row=0
		self.gridLayout.addLayout(Sub(self,'i','y'),row,0,1,1)
		self.gridLayout.addLayout(Sub(self,None,"u"),row,4,1,1)

		row=row+1
		self.gridLayout.addLayout(Sub(self,'e','ø'),row,1,1,1)
		self.gridLayout.addLayout(Sub(self,"\u0259",None),row,3,1,1)
		self.gridLayout.addLayout(Sub(self,None,"o"),row,4,1,1)

		row=row+1
		self.gridLayout.addLayout(Sub(self,"\u025b","\u0153"),row,2,1,1)
		self.gridLayout.addLayout(Sub(self,None,"\u0254"),row,4,1,1)
		self.gridLayout.addLayout(Sub(self,None,"\u0254"),row,4,1,1)

		row=row+1
		self.gridLayout.addLayout(Sub(self,"\u025b\u0303","\u0153\u0303"),row,2,1,1)
		self.gridLayout.addLayout(Sub(self,None,"\u0254\u0303"),row,4,1,1)

		row=row+1
		self.gridLayout.addLayout(Sub(self,"\u0061","\u0276"),row,3,1,1)
		self.gridLayout.addLayout(Sub(self,"\u0251","\u0252"),row,4,1,1)

		row=row+1
		self.gridLayout.addLayout(Sub(self,"\u0251\u0303",None),row,4,1,1)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win=Vowels()
	win.show()
	sys.exit(app.exec_())
