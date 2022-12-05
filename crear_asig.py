import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from conexion_sqlite import Comunicacion

class Registrar_Asig(QMainWindow):
    def __init__(self):
        super(Registrar_Asig, self).__init__()
        loadUi('interfaces/crear_asignatura.ui', self)
        self.base_datos = Comunicacion()

        self.btnRegistrar_2.clicked.connect(self.registrar_curso)


    def registrar_curso(self):
        idasignatura = self.lblIDAsig.text().upper()
        nombreasig = self.lblNombreAsig.text().upper()
        ncreditos = self.lblCredito.text().upper()
        nombre_docente = self.lblNombreDoc.text().upper()

        if idasignatura != '' and nombreasig != '' and ncreditos != '' and nombre_docente != '':
            self.base_datos.insertar_asignatura(idasignatura, nombreasig, ncreditos, nombre_docente)
            self.txtMsg.setText('Registrado correctamente')
            self.lblIDAsig.clear()
            self.lblNombreAsig.clear()
            self.lblCredito.clear()
            self.lblNombreDoc.clear()
        else:
            self.txtMsg.setText('Faltan datos')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_app = Registrar_Asig()
    mi_app.show()
    sys.exit(app.exec_())