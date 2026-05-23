def create_graph(rutas):
    grafo = {}

    for origen, destino, distancia, tiempo in rutas:
        if origen not in grafo:
            grafo[origen] = {}

        grafo[origen][destino] = {
            "distance": distancia,
            "time": tiempo
        }

    return grafo