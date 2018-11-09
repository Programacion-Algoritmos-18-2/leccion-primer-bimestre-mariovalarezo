
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
    def agregar_nombre(self, nombre):
        self.nombre= nombre
    def obtener_nombre(self):
        return self.nombre
    def agregar_apellido(self, apellido):
        self.apellido = apellido
    def obtenee_apellido(self):
        return self.apellido
    def agregar_cedula(self, cedula):
        self.cedula = cedula
    def obtener_cedula(self):
        return self.cedula
    def presentar_datos(self):
         cadena = "Informancion de\n %s %s \n cedula %s" % (self.obtener_nombre(),
                                                       self.obtenee_apellido(),
                                                       self.obtener_cedula())
         return cadena

