from math import inf
import sys

def read_file(file):
    graph = dict()
    initial = ''
    
    with open(file) as file:
        initial = file.readline().strip()
        for line in file:
            node1, node2, weight = line.strip().split(',')
            if node1 in graph:
                graph[node1].append((node2, int(weight)))
            else:
                graph[node1] = [(node2, int(weight))]
            
            if node2 not in graph:
                graph[node2] = []

    return initial, graph

def find_negative_cycle_node(costs, graph, predecessor):
    # Hacemos iteracion extra para encontrar ciclo negativo
    for n in range(len(graph)):
        modified = False
        for node in graph:
            if costs[node] < inf:
                for neighbour, weight in graph[node]:
                    if weight + costs[node] < costs[neighbour]:
                        modified = True
                        costs[neighbour] = weight + costs[node]
                        predecessor[neighbour] = [node, weight]
                        if n == len(graph) - 1:
                            return neighbour

        if not modified:
            return None
    
    raise Exception("Unreachable section has been reached")

def find_negative_cycle(initial, graph):
    costs = dict()
    predecessor = dict()

    for node in graph:
        costs[node] = inf
    costs[initial] = 0

    cycle_target = find_negative_cycle_node(costs, graph, predecessor)
    if not cycle_target:
        return [], 0

    # Tomamos un camino de largo n, donde debe encontrarse
    # al menos una instancia del ciclo negativo
    negative_cycle = []
    found = dict()
    for i in range(len(graph) + 1):
        negative_cycle.append(cycle_target)

        if cycle_target in found:
            negative_cycle = negative_cycle[found[negative_cycle[i]]:i]
            break
        else:
            found[cycle_target] = i

        cycle_target = predecessor[cycle_target][0]

    total_cost = 0
    for i in range(len(negative_cycle)):
        total_cost += predecessor[negative_cycle[i]][1]

    return negative_cycle[::-1], total_cost

def main():
    if len(sys.argv) < 2:
        print("Error: faltan parámetros.")
        print("Uso: solucion.py <ruta_archivo>")
        return
    initial, graph = read_file(sys.argv[1])
    cycle, cost = find_negative_cycle(initial, graph)
    if not cycle:
        print("No existen ciclos negativos en el grafo")
    else:
        print(f"Existe al menos un ciclo negativo en el grafo. {cycle} → Costo: {cost}")

main()