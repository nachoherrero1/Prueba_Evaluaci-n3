import random

# Definición de la lista de naves espaciales
naves = [
    {"nombre": "Estrella Brillante", "longitud": 120, "tripulantes": 15, "pasajeros": 50},
    {"nombre": "Cometa Veloz", "longitud": 150, "tripulantes": 20, "pasajeros": 80},
    {"nombre": "Titán del Cosmos", "longitud": 180, "tripulantes": 25, "pasajeros": 100},
    {"nombre": "GX-200", "longitud": 90, "tripulantes": 10, "pasajeros": 40},
    {"nombre": "GX-300", "longitud": 100, "tripulantes": 12, "pasajeros": 45},
    {"nombre": "Nebulosa Rápida", "longitud": 200, "tripulantes": 30, "pasajeros": 120},
    {"nombre": "Voyager 1", "longitud": 80, "tripulantes": 8, "pasajeros": 30}
]

# 1. Ordenar la lista de naves por nombre de forma ascendente y por longitud de forma descendente
naves_ordenadas = sorted(naves, key=lambda x: (x['nombre'], -x['longitud']))

# 2. Mostrar toda la información de las naves "Cometa Veloz" y "Titán del Cosmos"
print("Información específica de naves solicitadas:")
for nave in naves_ordenadas:
    if nave["nombre"] in ["Cometa Veloz", "Titán del Cosmos"]:
        print("Nombre:", nave["nombre"], "- Longitud:", nave["longitud"], "- Tripulantes:", nave["tripulantes"], "- Pasajeros:", nave["pasajeros"])

# 3. Determinar las cinco naves con mayor cantidad de pasajeros
naves_top_pasajeros = sorted(naves, key=lambda x: x['pasajeros'], reverse=True)[:5]

# Mezclar aleatoriamente antes de mostrar resultados
random.shuffle(naves_top_pasajeros)
print("\nLas cinco naves con mayor cantidad de pasajeros (orden aleatorio):")
for nave in naves_top_pasajeros:
    print(nave["nombre"])

# 4. Indicar la nave que requiere la mayor cantidad de tripulación
nave_max_tripulacion = max(naves, key=lambda x: x['tripulantes'])
print("\nLa nave que requiere la mayor cantidad de tripulación es:", nave_max_tripulacion["nombre"])

# 5. Mostrar todas las naves cuyo nombre comience con "GX"
naves_con_GX = [nave for nave in naves if nave["nombre"].startswith("GX")]
print("\nNaves cuyo nombre comienza con 'GX':", ', '.join(nave["nombre"] for nave in naves_con_GX))

# 6. Listar todas las naves que pueden llevar seis o más pasajeros
naves_seis_pasajeros_o_mas = [nave for nave in naves if nave["pasajeros"] >= 6]
print("\nNaves que pueden llevar seis o más pasajeros:", ', '.join(nave["nombre"] for nave in naves_seis_pasajeros_o_mas))

# 7. Mostrar toda la información de la nave más pequeña y la más grande
nave_mas_pequena = min(naves, key=lambda x: x['longitud'])
nave_mas_grande = max(naves, key=lambda x: x['longitud'])
print("\nInformación de la nave más pequeña:")
print("Nombre:", nave_mas_pequena["nombre"], "- Longitud:", nave_mas_pequena["longitud"], "- Tripulantes:", nave_mas_pequena["tripulantes"], "- Pasajeros:", nave_mas_pequena["pasajeros"])
print("\nInformación de la nave más grande:")
print("Nombre:", nave_mas_grande["nombre"], "- Longitud:", nave_mas_grande["longitud"], "- Tripulantes:", nave_mas_grande["tripulantes"], "- Pasajeros:", nave_mas_grande["pasajeros"])