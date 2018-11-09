
class Empleado(object):
    def _init_(self):
        self.nombre= ""
        self.apellido =""
        self.cedula =""
        self.comision_fija =0
    def agregar_comision(self ,comision):
        self.comision_fija= comision
    def obtener_comision(self):
        return self.comision_fija
    def agregar_nombre(self, nom):
        self.nombre= nom
    def obtener_nombre(self):
        return self.nombre
    def agregar_apellido(self, ape):
        self.apellido = ape
    def obtenee_apellido(self):
        return self.apellido
    def agregar_cedula(self, ced):
        self.cedula = ced
    def obtener_cedula(self):
        return self.cedula
    def presentar_datos(self):
         cadena = "Informancion de\n %s %s \n cedula %s" % (self.obtener_nombre(),
                                                       self.obtenee_apellido(),
                                                       self.obtener_cedula())
         return cadena

class EmpleadoPorHoras(Empleado):
    def _init_(self):
        super(EmpleadoPorHoras, self). _init_()
        self.numero_horas=0
        self.valor_hora=0
    def agregar_numero_horas(self, num):
        self.numero_horas = num
    def obtener_numero_horas(self):
        return self.numero_horas
    def agregar_valor_hora(self, va):
        self.valor_hora = va
    def obtener_valor_hora(self):
        return self.valor_hora

    def calcular_valor_sueldo(self):
        va=self.numero_horas*self.valor_hora
        return va

    def presentar_datos(self):
        cadena1 = "%s \n Numero horas: %s \n Valor Hora: %s \n Sueldo Final: %s" % (
        super(EmpleadoPorHoras, self).presentar_datos(), self.obtener_numero_horas(), self.obtener_valor_hora(),
        self.calcular_valor_sueldo())
        return cadena1




class EmpleadoFijo(Empleado):
    def _init_(self):
        super(EmpleadoFijo, self). _init_()
        self.sueldo_fijo=0
        self.descuento_seguro=0
    def agregar_sueldo_fijo(self, sueldo):
        self.sueldo_fijo = sueldo
    def obtener_sueldo_fijo(self):
        return self.sueldo_fijo
    def agregar_descuento_seguro(self, des):
        self.descuento_seguro = des
    def obtener_descuento_seguro(self):
        return self.descuento_seguro


    def calcular_valor_des(self):
        des= self.sueldo_fijo-self.descuento_seguro+self.comision_fija
        return des

    def presentar_datos(self):
        Cadena2 = "%s \n Sueldo Fijo: %s \n Descuento: %s \n Comision %s \n Sueldo Final: %s" % (
            super(EmpleadoFijo, self).presentar_datos(), self.obtener_sueldo_fijo(), self.obtener_descuento_seguro(),self.comision_fija,
            self.calcular_valor_des())
        return Cadena2


class EmpleadoPorSemana(Empleado):
    def _init_(self):
        super(EmpleadoFijo, self). _init_()
        self.numero_sem=0
        self.valor_sem=0
    def agregar_numero_sem(self, nsem):
        self.numero_sem = nsem
    def obtener_numero_sem(self):
        return self.numero_sem
    def agregar_valor_sem(self, vsem):
        self.valor_sem = vsem
    def obtener_valor_sem(self):
        return self.valor_sem
    def calcular_valor_sem(self):
        valor= self.numero_sem*self.valor_sem
        return valor

    def presentar_datos(self):
        Cadena3 = "%s \n Numero de Semanas:  %s \n Valor semanal %s \n Sueldo Final: %s" % (
            super(EmpleadoPorSemana, self).presentar_datos(), self.obtener_numero_sem(), self.obtener_valor_sem(),
            self.calcular_valor_sem())
        return Cadena3

