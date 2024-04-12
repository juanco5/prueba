from funcionesbarco import init_tablero

TABLERO = init_tablero()


#barcos
barco_1 = [(0,1), (1,1)] 
barco_2 = [(1,3), (1,4), (1,5), (1,6)]
lista_barcos = [barco_1, barco_2]

for i in lista_barcos:
    for j in i:
        TABLERO[j] = "O"

print(TABLERO)