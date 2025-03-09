from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import globalvar
import simuladorui
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant

class simulador_ventana(QMainWindow):

    def __init__(self):
        super(simulador_ventana, self).__init__()
        self.ui = simuladorui.Ui_Form()
        self.ui.setupUi(self)

        self.tabla_particiones()
        self.ui.pushButton_3.clicked.connect(self.ingresar_tareas)
        self.ui.pushButton_2.clicked.connect(self.tareas_posicion)
        self.ui.pushButton.clicked.connect(self.designar_tarea)

    def tabla_particiones(self):

        self.ui.tableWidget_3.setRowCount(len(globalvar.lista_particiones))
        self.ui.tableWidget_3.setColumnCount(len(globalvar.lista_particiones[0]))
        
        for fila, registro in enumerate(globalvar.lista_particiones):
            for columna, valor in enumerate(registro):
                item = QTableWidgetItem(str(valor))
                self.ui.tableWidget_3.setItem(fila, columna, item)

    def tareas_posicion(self):
        for i in range(len(globalvar.lista_ingreso)):
            for j in range(len(globalvar.lista_particiones)):
                if globalvar.lista_ingreso[i][2] <= globalvar.lista_particiones[j][1]:
                    if globalvar.lista_particiones[j][2] == True:
                            globalvar.lista_tarea.append([globalvar.lista_particiones[j][0], globalvar.lista_ingreso[i][1]])
                            globalvar.lista_particiones[j][2] = False
                            print(globalvar.lista_tarea)
                            break
                    else:
                        print(".")
            

        self.ui.tableWidget.setRowCount(len(globalvar.lista_tarea))
        self.ui.tableWidget.setColumnCount(len(globalvar.lista_tarea[0]))
        for fila, registro in enumerate(globalvar.lista_tarea):
            for columna, valor in enumerate(registro):
                item = QTableWidgetItem(str(valor))
                self.ui.tableWidget.setItem(fila, columna, item)

        self.tabla_particiones()
        globalvar.lista_ingreso.clear()
        print(globalvar.lista_ingreso)
        self.ui.tableWidget_2.clearContents()
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.setColumnCount(0)



    def ingresar_tareas(self):

        self.tarea = str(self.ui.lineEdit.text())
        self.tamaño = int(self.ui.lineEdit_2.text())

        for i in range (len(globalvar.lista_particiones)):
            if self.tamaño <= globalvar.lista_particiones[i][1]:
                globalvar.i += 1
                globalvar.lista_ingreso.append([globalvar.i, self.tarea, self.tamaño])
                print(globalvar.lista_ingreso)
                break

        self.ui.tableWidget_2.setRowCount(len(globalvar.lista_ingreso))
        self.ui.tableWidget_2.setColumnCount(len(globalvar.lista_ingreso[0]))
        for fila, registro in enumerate(globalvar.lista_ingreso):
            for columna, valor in enumerate(registro):
                item = QTableWidgetItem(str(valor))
                self.ui.tableWidget_2.setItem(fila, columna, item)
        


    def designar_tarea(self):
        self.tarea = str(self.ui.lineEdit.text())
        for i in range (len(globalvar.lista_tarea)):
            if self.tarea == globalvar.lista_tarea[i][1]:
                globalvar.lista_particiones[i][2] = True
                globalvar.lista_tarea.pop(i)
                print(globalvar.lista_tarea)
                break
        
        self.ui.tableWidget.setRowCount(len(globalvar.lista_tarea))
        self.ui.tableWidget.setColumnCount(len(globalvar.lista_tarea[0]))
        for fila, registro in enumerate(globalvar.lista_tarea):
            for columna, valor in enumerate(registro):
                item = QTableWidgetItem(str(valor))
                self.ui.tableWidget.setItem(fila, columna, item)
       
        self.tabla_particiones()

       