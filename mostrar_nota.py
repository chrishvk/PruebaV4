import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from conexion_sqlite import Comunicacion


class Mostrar_Nota(QMainWindow):
    def __init__(self):
        super(Mostrar_Nota, self).__init__()
        loadUi('interfaces/mostrar_notas.ui', self)
        self.base_datos = Comunicacion()


    def mostrar_nota(self):
        datos = self.base_datos.mostrar_notas()
        i = len(datos)
        self.tbl_notas.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.id = row[0]
            self.tbl_notas.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tbl_notas.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[2]))
            self.tbl_notas.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[3]))
            self.tbl_notas.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[4]))
            self.tbl_notas.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_app = Mostrar_Nota()
    mi_app.show()
    sys.exit(app.exec_())