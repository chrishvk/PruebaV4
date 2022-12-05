from PyQt5 import QtWidgets, uic
#Iniciar la app
app = QtWidgets.QApplication([])

#Cargar los archivos .iu
inicio = uic.loadUi("interfaces/inicio_sesion.ui")
menu_principal = uic.loadUi("interfaces/menu_principal.ui")
crear_asignatura = uic.loadUi("interfaces/crear_asignatura.ui")
registrar_alumno = uic.loadUi("interfaces/registrar_alumnos.ui")
mostrar_notas = uic.loadUi("interfaces/mostrar_notas.ui")
ingresar_notas = uic.loadUi("interfaces/ingresar_notas.ui")


def gui_inicio_sesion():
    nombre = inicio.txtUser
    contra = inicio.txtContra

    if nombre == 'Chris' and contra == '123':
        gui_menu_principal()


def gui_menu_principal():
    inicio.hide()
    menu_principal.show()


def gui_crear_asignatura():
    menu_principal.hide()
    crear_asignatura.show()


def gui_registrar_alumno():
    menu_principal.hide()
    registrar_alumno.show()


def gui_mostrar_notas():
    menu_principal.hide()
    mostrar_notas.show()


def gui_ingresar_notas():
    menu_principal.hide()
    ingresar_notas.show()


#Botones
inicio.btnIngresar.clicked.connect(gui_menu_principal)
menu_principal.btnRegAsig.clicked.connect(gui_crear_asignatura)
menu_principal.btnRegAlum.clicked.connect(gui_registrar_alumno)
menu_principal.btnMostrarNotas.clicked.connect(gui_mostrar_notas)
menu_principal.btnIngresarNotas.clicked.connect(gui_ingresar_notas)


#Ejecutable
inicio.show()
app.exec()
