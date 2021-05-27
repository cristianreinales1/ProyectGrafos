import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

nodes = np.array(["Azul", "Sapo", "Lobos", "Rojo", "Picuchullos", "Rocosos", "Cangrejo"])

row = np.array(["Azul", "Azul", "Lobos", "Sapo", "Sapo", "Rojo", "Rojo", "Rocosos", "Picuchillos"])
col = np.array(["Sapo", "Lobos", "Sapo", "Picuchillos", "Rojo", "Rocosos", "Cangrejo", "Cangrejo", "Rojo"])

#Los valores que cambian segun el campeon son los pesos.
value = np.array([25, 27, 19, 29, 32, 29, 36, 35, 11])


#Tiempos
#Azul -> sapo: 3
#Azul -> Lobos: 5
#Lobos -> sapo: 8
#Sapo -> Picuchillos: 18
#Sapo -> rojo:  21
#Rojo -> Rocosos: 6
#Rojo -> Cangrejo: 13
#Rocosos -> Cangrejo: 13
#Picuchillos -> Rojo : 5


#Valores Amumu: value = np.array([27, 29, 17, 27, 30, 30, 37, 35])
#Valores Nocturne: value = np.array([25, 27, 19, 29, 32, 29, 36, 35, 11])
#Valores Olaf: value = np.array([23, 25, 22, 29, 32, 27, 34, 32, 22])
#Valores Trynda: value = np.array([29, 31, 21, 32, 35, 33, 40, 38, 22])
#Valores Warwick value = np.array([20, 24, 22, 29, 32, 23, 30, 30, 26])

G = nx.Graph()
for i in range(0, np.size(nodes)):
    G.add_node(nodes[i])

for i in range(0, np.size(row)):
    G.add_weighted_edges_from([(row[i], col[i], value[i])])

pos = nx.shell_layout(G)

nx.draw(G,pos,with_labels=True, node_color='white', edge_color='b', node_size=800, alpha=0.5)
edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels)
plt.draw()
plt.pause(1)# Interval seconds: 3s
plt.close()



#algoritmo dijkstra
start,end=input("Ingrese el nombre de los campamentos A y B para encontrar el camino mas corto de A a B: ").split()
path=nx.dijkstra_path(G, source=start, target=end)
print('La ruta que debe seguir para llegar al {1} con nivel 3 y antes del minuto 3:15 es la siguiente:'.format(start,end), path)
distance=nx.dijkstra_path_length(G, source=start, target=end)
print('El tiempo que le tomo ir del campamento "{0}" al campamento "{1}" es:'.format(start,end), distance)