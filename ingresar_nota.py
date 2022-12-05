import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from conexion_sqlite import Comunicacion

class Registrar_Nota(QMainWindow):
    def __init__(self):
        super(Registrar_Nota, self).__init__()
        loadUi('interfaces/ingresar_notas.ui', self)
        self.base_datos = Comunicacion()
        self.btnBuscar.clicked.connect(self.buscar_alum)
        self.btnAceptar.clicked.connect(self.registrar_nota)


    def registrar_nota(self):
        nombrealumno = self.txtNombre.text().upper()
        apellidopat = self.txtApat.text().upper()
        p1 = self.lblp1.text()
        p2 = self.lblp2.text()
        p3 = self.lblp3.text()

        if nombrealumno != '' and apellidopat != '' and p1 != '' and p2 != '' and p3 != '':
            self.base_datos.registrar_nota(nombrealumno, apellidopat, p1, p2, p3)
            self.txtNombre.clear()
            self.txtApat.clear()
            self.lblp1.clear()
            self.lblp2.clear()
            self.lblp3.clear()
        else:
            self.txtMsg.setText('Faltan datos')

    def buscar_alum(self):
        apellido_alumno = self.txtNombre.text()
        self.nomb = self.base_datos.buscar_apellido(apellido_alumno)
        if len(self.nomb) != 0:
            self.txtResultado.setText(self.nomb)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_app = Registrar_Nota()
    mi_app.show()
    sys.exit(app.exec_())