import networkx as nx
import matplotlib.pyplot as plt
import logging
logging.basicConfig(level=logging.INFO)

logging.info('1')

G = nx.Graph()

nodes = [i for i in range(15)]

G.add_nodes_from(nodes)
G.add_edges_from([(1, 2, {'fc': True, 'weight': 10}), (1, 3), (4, 1)])

G.add_edges_from([(11, 5, {'fc':True, 'weight': 10}), (5, 8), (5,0), (8,13, {'fc':True, 'weight': 10})])

G.add_edges_from([(12, 10, {'fc':True, 'weight': 10}), (10, 14), (7,14), (6,9)])

logging.info('5')
# nx.draw_networkx_nodes(G, node_size=10, node_color='r')
logging.info('4')

edges = G.edges()

colors = []
weights = []
for u, v in edges:
    color = 'r'
    weight = 1
    if 'fc' in G[u][v]:
        if G[u][v]['fc']:
            color = 'b'
    if 'weight' in G[u][v]:
        if G[u][v]['weight']:
            weight = G[u][v]['weight']
    colors.append(color)
    weights.append(weight)

nx.draw(G, with_labels=True, font_weight='bold', edge_color=colors, width=weights)
# nx.draw_networkx_edges(G,  edge_color='b')
logging.info('5')

plt.show()