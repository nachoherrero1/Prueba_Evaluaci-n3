import os
from time import time
import doctest

def crear_matriz():
    matriz = []
    for x in range(20):
        fila = []
        for i in range(100):
            fila.append(" ")
        matriz.append(fila)
    return matriz

def mostrar_torres(matriz, p):
    for fila in matriz:
        print("".join(fila))
    print("Pasos realizados:", p, "   reiniciar     menu      salir")

def colocar_disco(matriz, fila, columna):
    matriz[fila][columna] = "\u25A0"

def mover_disco(origen, destino):
    if len(origen) > 0 and (len(destino) == 0 or origen[-1] < destino[-1]):
        destino.append(origen.pop())

def jugar_torres_hanoi():
    while True:
        cantidad_discos = int(input("Ingrese el número de discos (1-74): "))
        if cantidad_discos < 1 or cantidad_discos > 74:
            print("Número de discos inválido. Intente nuevamente.")
        else:
            break

    matriz = crear_matriz()
    torre1 = list(range(cantidad_discos, 0, -1))
    torre2 = []
    torre3 = []
    pasos = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_torres(matriz, pasos)
        print("1: Mover disco de la torre 1 a la torre 2")
        print("2: Mover disco de la torre 1 a la torre 3")
        print("3: Mover disco de la torre 2 a la torre 1")
        print("4: Mover disco de la torre 2 a la torre 3")
        print("5: Mover disco de la torre 3 a la torre 1")
        print("6: Mover disco de la torre 3 a la torre 2")
        print("0: Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mover_disco(torre1, torre2)
        elif opcion == "2":
            mover_disco(torre1, torre3)
        elif opcion == "3":
            mover_disco(torre2, torre1)
        elif opcion == "4":
            mover_disco(torre2, torre3)
        elif opcion == "5":
            mover_disco(torre3, torre1)
        elif opcion == "6":
            mover_disco(torre3, torre2)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue

        pasos += 1
        actualizar_matriz(matriz, torre1, torre2, torre3)

        if ganar(torre3, cantidad_discos):
            os.system('cls' if os.name == 'nt' else 'clear')
            mostrar_torres(matriz, pasos)
            print("¡Felicidades, has ganado!")
            break

def actualizar_matriz(matriz, torre1, torre2, torre3):
    matriz = crear_matriz()
    for i, disco in enumerate(torre1):
        colocar_disco(matriz, 18 - i, 16)
    for i, disco in enumerate(torre2):
        colocar_disco(matriz, 18 - i, 50)
    for i, disco in enumerate(torre3):
        colocar_disco(matriz, 18 - i, 84)

def ganar(torre, cantidad_discos):
    return len(torre) == cantidad_discos and torre == list(range(cantidad_discos, 0, -1))

def move_tower(height, from_pole, to_pole, with_pole):
    """
    >>> move_tower(3, 'A', 'B', 'C')
    moving disk from A to B
    moving disk from A to C
    moving disk from B to C
    moving disk from A to B
    moving disk from C to A
    moving disk from C to B
    moving disk from A to B
    """
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(fp, tp):
    print("moving disk from", fp, "to", tp)

def main():
    while True:
        height = int(input("Height of hanoi (1-74): ").strip())
        if height < 1 or height > 74:
            print("Invalid height. Please try again.")
        else:
            break
    move_tower(height, "A", "B", "C")

if __name__ == "__main__":
    main()

doctest.testmod(verbose=True)
