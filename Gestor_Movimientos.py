from Clase_Movimientos import Movimiento
import csv

class Manejador_Movimiento:
    __Lista_Movimientos: list

    def __init__ (self):
        self.__Lista_Movimientos=[]

    def Cargar (self):
        archivo= ('MovimientoAbril2024.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in range (len(archivo)):
            if fila > 0:
                m = Movimiento(fila[0], fila[1], fila[2], fila [3], float(fila[4]))
                self.__Lista_Movimientos.append(m)
        archivo.close ()

    def ordenar (self):
        self.__Lista_Movimientos= sorted(self.__Lista_Movimientos)