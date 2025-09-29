import heapq

# Grafo con estaciones y conexiones (tiempos en minutos)
graph = {
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
heuristic = {
    "MA": 40, "PE": 37, "VE": 35, "PS": 38,
    "GS": 30, "BA": 20, "JI": 10, "20J": 0
}

# Penalización por cambio de troncal
PENALIZACION_TRANSFERENCIA = 5

def a_star_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start, [], 0, None))  
    closed_set = set()

    while open_list:
        f, current, path, g, last_line = heapq.heappop(open_list)

        if current in closed_set:
            continue
        closed_set.add(current)

        path = path + [current]

        if current == goal:
            return path, g

        for neighbor, (time, line) in graph[current].items():
            new_g = g + time
            if last_line and last_line != line:
                new_g += PENALIZACION_TRANSFERENCIA  

            f = new_g + heuristic.get(neighbor, 0)
            heapq.heappush(open_list, (f, neighbor, path, new_g, line))

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
        ruta, tiempo = a_star_search(inicio, fin)
        print(f"Ruta de {inicio} a {fin}: {ruta} - Tiempo estimado: {tiempo} minutos")
