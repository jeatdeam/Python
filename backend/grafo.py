import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# 1. Cargar los datos
df = pd.read_csv('peliculas_streaming_1000.csv')

# 2. Crear un grafo no dirigido
G = nx.Graph()

# 3. Construir el grafo bipartito (Película <-> Género)
for _, row in df.iterrows():
  pelicula = str(row['titulo']).strip()
  genero = str(row['genero']).strip()

  # Agregar nodos con atributo 'bipartite' para diferenciarlos
  G.add_node(pelicula, tipo='pelicula')
  G.add_node(genero, tipo='genero')

  # Agregar la relación (arista)
  G.add_edge(pelicula, genero)

# -------------------------------------------------------------
# 4. TÉCNICA: Extraer un SUBGRAFO (Ejemplo: Un género y 25 de sus películas)
# -------------------------------------------------------------
genero_objetivo = df['genero'].iloc[0]  # Toma el primer género del archivo

# Obtener los vecinos del género (las películas asociadas)
vecinos_pelicula = list(G.neighbors(genero_objetivo))[:25]  # Limitamos a 25

# Definir la lista de nodos del subgrafo
nodos_subgrafo = [genero_objetivo] + vecinos_pelicula
subgrafo = G.subgraph(nodos_subgrafo)

# -------------------------------------------------------------
# 5. Visualización del Subgrafo
# -------------------------------------------------------------
plt.figure(figsize=(12, 8))

# Algoritmo de distribución de nodos
pos = nx.spring_layout(subgrafo, k=0.5, seed=42)

# Asignar colores por tipo de nodo
colores = [
    '#FF6B6B' if subgrafo.nodes[n]['tipo'] == 'genero' else '#4D96FF'
    for n in subgrafo.nodes()
]
tamanos = [
    2500 if subgrafo.nodes[n]['tipo'] == 'genero' else 600
    for n in subgrafo.nodes()
]

# Dibujar nodos y aristas
nx.draw_networkx_nodes(
    subgrafo, pos, node_color=colores, node_size=tamanos, alpha=0.9
)
nx.draw_networkx_edges(subgrafo, pos, width=1.5, alpha=0.5, edge_color='gray')
nx.draw_networkx_labels(
    subgrafo, pos, font_size=8, font_family='sans-serif', font_weight='bold'
)

plt.title(
    f"Subgrafo Bipartito: Género '{genero_objetivo}' y Muestra de Películas",
    fontsize=14,
)
plt.axis('off')
plt.tight_layout()
plt.show()