import sys
from PyQt5.QtWidgets import QApplication
from particiones_window import particiones_ventana

def main():
    app = QApplication(sys.argv)
    ventana1 = particiones_ventana()  # Instancia la clase
    ventana1.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta el bucle de eventos

if __name__ == "__main__":
    main()