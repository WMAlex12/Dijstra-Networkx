import networkx as nx
import matplotlib.pyplot as plt
import time

def dijkstra(graph, start_node, end_node):
    start_time= time.time()
    G = nx.Graph(graph)

    shortest_paths = nx.single_source_dijkstra_path_length(G, start_node)
    
    end_time = time.time()
    print("Nodo de inicio:", start_node)
    print("Caminos más cortos:")
    #for node, distance in shortest_paths.items():
        #print(f"Nodo: {node}, Distancia: {distance}")

    
    # Encontrar el camino más corto desde el nodo de inicio al nodo final
    shortest_path = nx.shortest_path(G, source=start_node, target=end_node)
    shortest_distance = nx.shortest_path_length(G, source=start_node, target=end_node)
    
    print(f"\nCamino más corto desde {start_node} a {end_node}: {shortest_path}")
    print(f"Distancia total: {shortest_distance}")

    elapsed_time = end_time - start_time
    print(f"\nTiempo de ejecución: {elapsed_time} segundos")

    # Visualizar el grafo y resaltar los caminos más cortos
    pos = nx.spring_layout(G)
    
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    
    # Resaltar los nodos del camino más corto
    path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
    
    nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    
    #plt.show()
    


# Crear el grafo dinámicamente
G = nx.Graph()
width_matrix = 1200
height_matrix = 1600
total_nodes = width_matrix * height_matrix
matriz = range(1, total_nodes + 1)
print(matriz)

G.add_nodes_from(matriz)

count = 1
for x in range(1, total_nodes + 1):
    if x <= total_nodes - width_matrix:
        G.add_edge(x, x + width_matrix)
    if x < count * width_matrix:
        G.add_edge(x, x + 1)
    else:
        count = count + 1

# Ejemplo de uso
if __name__ == "__main__":
    start_node = int(input("Ingrese el nodo de inicio: "))
    end_node = int(input("Ingrese el nodo final: "))
    
    dijkstra(G, start_node, end_node)

    