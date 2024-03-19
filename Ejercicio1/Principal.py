import funciones

from time import time
cantidad_de_discos = 0

while True:
  pasos = 0
  cantidad_de_discos = funciones.menu()
  funciones.colocar_discos(cantidad_de_discos)
  funciones.mostrar_torres(pasos)

  time1 = time()
  while not funciones.ganar(cantidad_de_discos):
    torre1 = int(input("Ingrese su movimiento " + str(pasos + 1) + ": "))
    if torre1 > 5:
      break
    elif torre1 == 5:
      cantidad_de_discos = funciones.menu()
      break
    elif torre1 == 4:
      funciones.inicializar_torres(cantidad_de_discos)
      break
    else:
      torre2 = int(input("Ingrese su movimiento " + str(pasos + 1) + ": "))
      if torre2 == 4:
        funciones.inicializar_torres(cantidad_de_discos)
        break
      if torre2 == 5:
        cantidad_de_discos = funciones.menu()
        break
      if torre2 == 6:
        break

      funciones.mover_torre(torre1, torre2)
      funciones.mostrar_torres(pasos)
      pasos += 1

  time2 = time()
  funciones.mostrar_torres(pasos)
  funciones.mensaje(time1, time2)
  k = input()
  if k == "3":
    break

  # Update best time if applicable
  if mejor_tiempo is None or time2 - time1 < mejor_tiempo:
    mejor_tiempo = time2 - time1