from funcionesbarco import *
from variablesbarco import TABLERO

#tablero_maquina = TABLERO
tablero_jugador = TABLERO

print("Hola bienvenido al juego de hlf!")

print("Disfruta!")
counter = 0

print(tablero_jugador)

while "O" in tablero_jugador and counter < 5:
    disparar(tablero=tablero_jugador)
    print(tablero_jugador)
    counter += 1
    if "O" not in tablero_jugador and counter < 5:
        print("Has ganado!")
        break

if "O" in tablero_jugador:
    print("Has perdido!")
    
print('Hola mundo')