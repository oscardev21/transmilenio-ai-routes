import heapq

# Grafo con estaciones y conexiones (tiempos en minutos)
grafo = {
    "MA": {"PE": (3, "Sur"), "PS": (4, "Sur")},        # Madelena
    "PE": {"MA": (3, "Sur"), "VE": (2, "Sur")},
    "VE": {"PE": (2, "Sur"), "GS": (4, "Sur")},
    "PS": {"MA": (4, "Sur")},                          # Portal del Sur
    "GS": {"VE": (4, "Sur"), "BA": (7, "NQS")},        # General Santander
    "BA": {"GS": (7, "NQS"), "JI": (20, "NQS")},       # Banderas
    "JI": {"BA": (20, "NQS"), "20J": (20, "Oriente")}, # Av. Jiménez
    "20J": {"JI": (20, "Oriente")}                     # Portal 20 de Julio
}

# Heurística: estimación simple de tiempo restante (valores ficticios)
heuristica = {
    "MA": 40, "PE": 37, "VE": 35, "PS": 38,
    "GS": 30, "BA": 20, "JI": 10, "20J": 0
}

# Penalización por cambio de troncal
PENALIZACION_CAMBIO_TRONCAL = 5

def busqueda_a_estrella(inicio, destino):
    lista_abierta = []
    heapq.heappush(lista_abierta, (0, inicio, [], 0, None))  
    conjunto_cerrado = set()

    while lista_abierta:
        f, actual, ruta, g, ultima_linea = heapq.heappop(lista_abierta)

        if actual in conjunto_cerrado:
            continue
        conjunto_cerrado.add(actual)

        ruta = ruta + [actual]

        if actual == destino:
            return ruta, g

        for vecino, (tiempo, linea) in grafo[actual].items():
            nuevo_g = g + tiempo
            if ultima_linea and ultima_linea != linea:
                nuevo_g += PENALIZACION_CAMBIO_TRONCAL  

            f = nuevo_g + heuristica.get(vecino, 0)
            heapq.heappush(lista_abierta, (f, vecino, ruta, nuevo_g, linea))

    return None, float("inf")

# Casos de prueba
if __name__ == "__main__":
    casos = [
        ("MA", "PS"),
        ("MA", "JI"),
        ("MA", "20J"),
        ("MA", "BA")
    ]

    for inicio, fin in casos:
        ruta, tiempo = busqueda_a_estrella(inicio, fin)
        print(f"Ruta de {inicio} a {fin}: {ruta} - Tiempo estimado: {tiempo} minutos")
