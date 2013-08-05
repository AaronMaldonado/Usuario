#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controller
from EliminarGrupo import Ui_Ventana_Eliminar_Grupo

class Ventana_eliminar(QtGui.QDialog):
	
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Ventana_grupo()
		self.ui.setupUi(self)
		#self.load_grupos()
		self.show()
