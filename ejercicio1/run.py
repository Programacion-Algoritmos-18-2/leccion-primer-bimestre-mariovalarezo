# Crear Empleado
from mipaquete.modelo import *
e = Empleado()
e.agregar_nombre("Luis")
e.agregar_apellido("Banitez")
e.agregar_cedula("110000001")
print (e.presentar_datos())

e1=EmpleadoPorHoras()
nombre=input("Ingrese el nombre: ")
e1.agregar_nombre(nombre)
e1.agregar_apellido("Andrade")
e1.agregar_cedula("112233")
e1.agregar_numero_horas(20.2)
e1.agregar_valor_hora(15)
print(e1.presentar_datos())

e2=EmpleadoFijo()
e2.agregar_sueldo_fijo(3002)
e2.agregar_descuento_seguro(10)
e2.agregar_cedula("112233")
comision=input("Comision: ")
comision=int(comision)
e2.agregar_comision(comision)
e2.agregar_nombre("Ana")
e2.agregar_apellido("Diaz")
print(e2.presentar_datos())

e3= EmpleadoPorSemana()
e3.agregar_numero_sem(10)
e3.agregar_valor_sem(15)
e3.agregar_cedula("112233")
e3.agregar_nombre("Juan")
e3.agregar_apellido("Diaz")
print(e3.presentar_datos())


