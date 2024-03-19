def solicitar_coeficiente(grado):
    coeficientes = []
    for i in range(grado, -1, -1):
        coef = int(input(f"Please enter the coefficient for x^{i}: "))
        coeficientes.append(coef)
    return coeficientes

def restar_polinomios(p1, p2):
    max_len = max(len(p1), len(p2))
    resultado = [0] * max_len
    for i in range(max_len):
        coef_p1 = p1[i] if i < len(p1) else 0
        coef_p2 = p2[i] if i < len(p2) else 0
        resultado[i] = coef_p1 - coef_p2
    return resultado

def dividir_polinomios(p1, p2):
    # Nota: Esta es una implementación simplificada y no maneja divisiones que no sean exactas.
    resultado = [0] * (len(p1) - len(p2) + 1)
    divisor_lead_coef = p2[0]
    for i in range(len(resultado)):
        coeficiente = p1[i] / divisor_lead_coef
        resultado[i] = coeficiente
        for j in range(len(p2)):
            if i+j < len(p1):
                p1[i+j] -= coeficiente * p2[j]
    return resultado

def eliminar_termino(polinomio, grado_termino):
    grado_polinomio = len(polinomio) - 1
    if grado_termino <= grado_polinomio:
        polinomio[grado_polinomio - grado_termino] = 0
    return polinomio

def existe_termino(polinomio, grado_termino):
    grado_polinomio = len(polinomio) - 1
    return grado_termino <= grado_polinomio and polinomio[grado_polinomio - grado_termino] != 0

# Solicitar al usuario los grados de los polinomios
grado_p1 = int(input("Please enter the degree for the first polynomial: "))
grado_p2 = int(input("Please enter the degree for the second polynomial: "))

# Solicitar coeficientes
print("For the first polynomial:")
p1 = solicitar_coeficiente(grado_p1)
print("For the second polynomial:")
p2 = solicitar_coeficiente(grado_p2)

# Restar polinomios
print("Subtracting the polynomials results in:", restar_polinomios(p1, p2))

# Eliminar término de polinomio
grado_termino = int(input("Please enter the degree of the term to be removed: "))
print("Polynomial after removing the term:", eliminar_termino(p1, grado_termino))

# Verificar existencia de término
print("Does the term exist in the first polynomial?", "Yes" if existe_termino(p1, grado_termino)else"No")
