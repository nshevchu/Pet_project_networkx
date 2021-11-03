import networkx as nx
import matplotlib.pyplot as plt
import logging
logging.basicConfig(level=logging.INFO)

logging.info('1')

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (4,1)])

logging.info('5')
#nx.draw_networkx_nodes(G, node_size=10, node_color='r')
logging.info('4')
nx.draw(G, with_labels=True, font_weight='bold')
#nx.draw_networkx_edges(G,  edge_color='b')
logging.info('5')

plt.show()