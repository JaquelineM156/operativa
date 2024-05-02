from Clase_Clientes import Clientes
import csv

class Manejador_Clientes:
    __Lista_Clientes:list 

    def __init__ (self):
        self.__Lista_Clientes= [ ]
        
        
    def Cargar (self):
        archivo= ('ClienteFarmaCiudad.csv')
        reader= csv.reader(archivo, delimiter=';')
        for fila in range (len(archivo)):
            if fila >0:
                c= Clientes(fila[0], fila[1], int (fila[2]), int(fila [3]), float(fila[4]))
                self.__Lista_Movimientos.append(c)
        archivo.close()

    def Actualizar (self, dni, m):
        i=0
        while i<(len(self.__Lista_Clientes)):
            if dni == self.__Lista_Clientes[i].getdni():
                print ('Cliente: ', self.__Lista_Clientes[i].getnombre(), self.__Lista_Clientes[i].getapellido())
                print ('Nuemro de cuanta: ', self.__Lista_Clientes[i].getnro() )
                print ('Saldo anterior: ', self.__Lista_Clientes[i].getsaldo())
                saldo=self.__Lista_Clientes[i].getsaldo()
                for j in range (len(m._Manejador_Movimiento__Lista_Movimientos)):
                    from Clase_Movimientos import Movimiento
                    if self.__Lista_Clientes[i]== m._Manejador_Movimiento__Lista_Movimientos[j].getnro():
                        print ('Fecha:',  m._Manejador_Movimiento__Lista_Movimientos[j].getfecha())
                        print ('Decripcion: ', m._Manejador_Movimiento__Lista_Movimientos[j].getdes())
                        print ('Importe: ', m._Manejador_Movimiento__Lista_Movimientos[j].getimp())
                        imp= m._Manejador_Movimiento__Lista_Movimientos[j].getimp()
                        print ('Tipo de movimiento: ', m._Manejador_Movimiento__Lista_Movimientos[j].gettipo())
                        tipo= m._Manejador_Movimiento__Lista_Movimientos[j].gettipo()
                        if tipo == 'c':
                            saldo+=imp
                        elif tipo =='p':
                            saldo-=imp
                self.actualizar_saldo(saldo)
                print ('Saldo actualizado: {}', format(saldo))

    def informar (self, dni, m):
        bandera=0
        i=0
        while i<(len(self.__Lista_Clientes)):
            if dni == self.__Lista_Clientes[i].getdni():
                nro= self.__Lista_Clientes[i].detnro()
                for j in range (len(m._Manejador_Movimiento__Lista_Movimientos)):
                    from Clase_Movimientos import Movimiento
                    if nro== m._Manejador_Movimiento__Lista_Movimientos[j].getnro():
                        bandera =-1
        return bandera 


