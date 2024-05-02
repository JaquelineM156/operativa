class Movimiento:
    __Nro_Cuenta: str
    __Fecha: str
    __Descripcion: str
    __Tipo_Movimiento:str
    __Importe:float

    def __init__(self, nrocuenta, fecha,desc, tipo, importe) :
        self.__Nro_Cuenta: nrocuenta
        self.__Fecha: fecha
        self.__Descripcion: desc
        self.__Tipo_Movimiento:tipo
        self.__Importe:importe

    def getnro(self):
        return self.__Nro_Cuenta
    def getfecha (self):
        return self.__Fecha
    def getdes (self):
        return self.__Descripcion
    def gettipo (self):
        return self.__Tipo_Movimiento
    def getimp (self):
        return self.__Importe
    def __it__ (self, other):
        return self.__Nro_Cuenta<other.__Nro_Cuenta
    def __gt__ (self, other):
        return self.__Nro_Cuenta<other.__Nro_Cuenta