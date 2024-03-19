import random

def generar_matriz_aleatoria(dim=3):
    """Genera una matriz cuadrada de dim x dim con números enteros aleatorios."""
    return [[random.randint(1, 100) for _ in range(dim)] for _ in range(dim)]

def determinante_sarrus(matriz):
    """Calcula el determinante de una matriz utilizando el método de Sarrus."""
    suma = sum(matriz[i][j] * matriz[(i+1)%3][(j+1)%3] * matriz[(i+2)%3][(j+2)%3] for i in range(3) for j in range(3))
    suma -= sum(matriz[i][j] * matriz[(i+1)%3][(j+2)%3] * matriz[(i+2)%3][(j+1)%3] for i in range(3) for j in range(3))
    return suma

# Generar y calcular el determinante de una matriz 3x3 aleatoria
matriz_aleatoria = generar_matriz_aleatoria()
print("Matriz Aleatoria:", matriz_aleatoria)
print("Determinante (método iterativo):", determinante_sarrus(matriz_aleatoria))
