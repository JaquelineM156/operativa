from Gestor_Clientes import Manejador_Clientes
from Gestor_Movimientos import Manejador_Movimiento

class test ():
    m=Manejador_Movimiento()
    c=Manejador_Clientes()
    c.Cargar()
    m.Cargar()


    print ('1. Actualizar datos')
    print ('2. Informar si hay movimiento')
    print ('3. Ordenar')
    print ('0. Para terminar')

    op= int(input('Ingrese la opcion'))
    while op==0:
        if op==1:
            dni= int (input('Ingrese dni: '))
            c.Actualizar(dni, m)
        elif op==2:
            dni= int (input('Ingrese dni: '))
            if c.Informar(dni, m)==-1: 
                print ('El cliente {}', format(dni), 'si realizo movimientos')
            else: print ('El cliente {}', format(dni), 'no realizo movimientos')
        elif op==3:
            m.ordenar()

        op= int(input('Ingrese la opcion'))

