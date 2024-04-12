import numpy as np

def init_tablero(size = (10, 10), fill = " "):
    tablero = np.full(size, fill)
    return tablero


def disparar(tablero):
    coord_x = int(input("Coord X:"))
    coord_y = int(input("Coord Y:"))

    if tablero[coord_x, coord_y] == "O":
        tablero[coord_x, coord_y] = "X"
        print("Has acertado!")

    elif tablero[coord_x, coord_y] == " ":
        tablero[coord_x, coord_y] = "-"
        print("Has fallado!")

    else:
        print("Has repetido el disparo.")

    print(tablero)