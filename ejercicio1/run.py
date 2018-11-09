# Crear Empleado
from mipaquete.modelo import *
e = Empleado()
e.agregar_nombre("Luis")
e.agregar_apellido("Banitez")
e.agregar_cedula("110000001")
print (e.presentar_datos())







