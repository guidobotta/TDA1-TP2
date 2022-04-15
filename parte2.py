from math import inf

def read_file():
    # TODO Cambiar grafo.txt
    graph = dict()
    initial = ''
    
    with open("grafo.txt") as file:
        initial = file.readline().strip()
        for line in file:
            node1, node2, weight = line.strip().split(',')
            if node1 in graph:
                graph[node1].append((node2, int(weight)))
            else:
                graph[node1] = [(node2, int(weight))]

    return initial, graph

def find_negative_cycle(initial, graph):
    costs = dict()
    predecessor = dict()

    for node in graph:
        costs[node] = inf

    costs[initial] = 0

    # Hacemos iteracion extra para encontrar ciclo negativo
    for n in range(len(graph)):
        modified = False
        for node in graph:
            if costs[node] < inf:
                for neighbour, weight in graph[node]:
                    if weight + costs[node] < costs[neighbour]:
                        modified = True
                        costs[neighbour] = weight + costs[node]
                        predecessor[neighbour] = node

        if not modified:
            return [], 0

    # TODO CAMBIAR RETURN
    return costs, 0

def main():
    initial, graph = read_file()
    cycle, cost = find_negative_cycle(initial, graph)
    if not cycle:
        print("No existen ciclos negativos en el grafo")
    else:
        print(f"Existe al menos un ciclo negativo en el grafo. {cycle} → Costo: {cost}")

main()