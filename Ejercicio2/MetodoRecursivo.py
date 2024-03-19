import random

def generar_matriz_aleatoria(dim=3):
    """Genera una matriz cuadrada de 3x3 con números enteros aleatorios."""
    return [[random.randint(1, 10) for _ in range(dim)] for _ in range(dim)]

def determinanteRecursivo(matriz, dim=3):
    if dim == 2:
        # Caso base para una submatriz 2x2
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    suma = sum(matriz[0][i] * determinanteRecursivo(
        [fila[:i] + fila[i+1:] for fila in matriz[1:]], dim-1) * (-1)**i
        for i in range(dim))
    return suma

# Ejemplo de uso
matriz_aleatoria = generar_matriz_aleatoria()
print("Matriz Aleatoria:", matriz_aleatoria)
print("Determinante (aproximación 'recursiva'):", determinanteRecursivo(matriz_aleatoria))
