import sqlite3

class Comunicacion():
    def __init__(self):
        self.conexion = sqlite3.connect('database/DB_registro.db')

    def insertar_asignatura(self, id_asig, nombre_asig, ncreditos, nombre_docente):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO tbl_asignatura(IDAsignatura, Nombre Asignatura, N° creditos, Nombre Docente)
        VALUES('{}', '{}', '{}', '{}')'''.format(id_asig, nombre_asig, ncreditos, nombre_docente)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def buscar_apellido(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM tbl_notas WHERE ApellidoPat = {}'''.format(nombre)
        cursor.execute(bd)
        apellidoX = cursor.fetchall()
        cursor.close()
        return apellidoX

    def ingresar_nota(self, id, nombre, apat, n1, n2, n3):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO tbl_notas(ID, Nombre, ApellidoPat, Parcial 1, Parcial 2, Parcial 3)
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}')'''.format(id, nombre, apat, n1, n2, n3)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def mostrar_notas(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM tbl_notas"
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro


