from hanoi import *
from hanoi import colocar_discos1

def mover_torre(a, b):
  if a == 1 and b == 2:
    mover1_2()
  elif a == 1 and b == 3:
    mover1_3()
  elif a == 2 and b == 3:
    mover2_3()
  elif a == 2 and b == 1:
    mover2_1()
  elif a == 3 and b == 1:
    mover3_1()
  elif a == 3 and b == 2:
    mover3_2()
  else:
    print("Error: Torre de origen o destino inválida")

def menu():
  cantidad_discos = 3
  while True:
    os.system("cls")
    print("Torres de Hanoi")
    print("Jugar ")
    print("Cantidad de discos ")
    for i in range(3):
      print("")
    x = input()
    inicializar_torres()

    if x == "1":
      return cantidad_discos

    elif x == "2":
      while True:
        cantidad_discos = int(input("Escoja la cantidad de discos con la que quiere jugar (hasta 10): "))
        if not cantidad_discos < 1 and not cantidad_discos > 10:
          break
      return cantidad_discos

    else:
      print("Opción inválida")

def colocar_discos(cantidad_discos):
    global matriz
    global array

    crear()

    for i in range(cantidad_discos):
        # Place disks based on their size
        if i == 0:
            colocar_discos1(l1, cantidad_discos - i, 12, 16)
        elif i == 1:
            colocar_discos1(l2, cantidad_discos - i, 46, 50)
        elif i == 2:
            colocar_discos1(l3, cantidad_discos - i, 80, 84)
        else:
            print("Error: Posición de disco inválida")

def mostrar_torres(pasos):
  global matriz
  global array

  for x in range(20):
    for i in range(100):
      if i == 99:
        print(matriz[x][i])
        continue
      print(matriz[x][i], end='')

  print("Pasos realizados :", pasos, "   reiniciar     menu      salir ")
def mover1_2():
  global l1, l2
  if len(l1) > 0 and len(l2) == 0:
    l2.append(l1.pop())
    actualizar_matriz()
  elif len(l1) > 0 and last(l1) < last(l2):
    l2.append(l1.pop())
    actualizar_matriz()
  else:
    print("Movimiento inválido")

def mover1_3():
  global l1, l3
  if len(l1) > 0 and len(l3) == 0:
    l3.append(l1.pop())
    actualizar_matriz()
  elif len(l1) > 0 and last(l1) < last(l3):
    l3.append(l1.pop())
    actualizar_matriz()
  else:
    print("Movimiento inválido")

def mover2_3():
  global l2, l3
  if len(l2) > 0 and len(l3) == 0:
    l3.append(l2.pop())
    actualizar_matriz()
  elif len(l2) > 0 and last(l2) < last(l3):
    l3.append(l2.pop())
    actualizar_matriz()
  else:
    print("Movimiento inválido")

def mover2_1():
  global l2, l1
  if len(l2) > 0 and len(l1) == 0:
    l1.append(l2.pop())
    actualizar_matriz()
  elif len(l2) > 0 and last(l2) < last(l1):
    l1.append(l2.pop())
    actualizar_matriz()
  else:
    print("Movimiento inválido")

def mover3_1():
  global l3, l1
  if len(l3) > 0 and len(l1) == 0:
    l1.append(l3.pop())
    actualizar_matriz()
  elif len(l3) > 0 and last(l3) < last(l1):
    l1.append(l3.pop())
    actualizar_matriz()
  else:
    print("Movimiento inválido")

def mover3_2():
  global l3, l2
  if len(l3) > 0 and len(l2) == 0:
    l2.append(l3.pop())
    actualizar_matriz()
  elif len(l3) > 0 and last(l3) < last(l2):
    l2.append(l3.pop())
    actualizar_matriz()
  else:
    print("Movimiento inválido")
