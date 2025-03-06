import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
import particionesui
import random
import rangoui
import globalvar
from simulador_window import simulador_ventana

class particiones_ventana(QMainWindow):
    
    def __init__(self):
        super(particiones_ventana, self).__init__()
        self.ui = particionesui.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.generar_particion)
    
    def open_rango(self):
        self.ventana2 = rango_ventana()
        self.ventana2.show()

    def generar_particion(self):
        globalvar.cantidad_particiones = int(self.ui.lineEdit.text())
        if globalvar.cantidad_particiones != '' and globalvar.cantidad_particiones > 0:
            self.open_rango()

class rango_ventana(QMainWindow):

    def __init__(self):
        super(rango_ventana, self).__init__()
        self.ui = rangoui.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.asignar_rango)

    ######
    def particionestabla(self):
        for i in range(globalvar.cantidad_particiones):
            globalvar.lista_particiones.append([i + 1, random.randint(globalvar.rango_min, globalvar.rango_max), True])
    ######

    def open_simulador(self):
        self.ventana3 = simulador_ventana()
        self.ventana3.show()

    def asignar_rango(self):
        globalvar.rango_min = int(self.ui.lineEdit.text())
        globalvar.rango_max = int(self.ui.lineEdit_2.text())
        if globalvar.rango_min != '' and globalvar.rango_min >= 0 and globalvar.rango_max != '' and globalvar.rango_max >= 0:
            self.particionestabla()
            self.open_simulador()