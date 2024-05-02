class Clientes:
    __Nombres: str
    __Apellido:str
    __dni: int
    __Nro_Cuenta:int
    __Saldo_Anterior: float

    def __init__(self, nombre, apellido, dni, nrocuenta, saldoanterior):
        self.__Nombres: nombre
        self.__Apellido:apellido
        self.__dni: dni
        self.__Nro_Cuenta:nrocuenta
        self.__Saldo_Anterior: saldoanterior
    
    def getnombre (self):
        return self.__Nombres
    def getdni(self):
        return self.__dni
    def getapellido(self):
        return self.__Apellido
    def getnro(self):
        return self.__Nro_Cuenta
    def getsaldo (self):
        return self.__Saldo_Anterior
    def acttualizar_saldo(self, s):
        self.__Saldo_Anterior= s

