import networkx as nx
import matplotlib.pyplot as plt
import logging
logging.basicConfig(level=logging.INFO)

logging.info('1')

'''
G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

plt.show()
'''

'''
G = nx.read_shp('shapes/Streets_clipped.shp') #Read shapefile as graph
logging.info('2')
pos = {xy: xy for xy in G.nodes()}
logging.info('3')

nx.draw_networkx_nodes(G, pos, node_size=10, node_color='r')
logging.info('4')

nx.draw_networkx_edges(G, pos, edge_color='b')
logging.info('5')

plt.show()
'''


from shapely.geometry import shape
import fiona
logging.info('4')
geoms =[shape(feature['geometry']) for feature in fiona.open("shapes/Streets_clipped.shp")]
logging.info('4')
import itertools
# create a Graph
import networkx as nx
logging.info('4')
G = nx.Graph()
logging.info('4')
for line in geoms:
   #for seg_start, seg_end in itertools.izip(list(line.coords),list(line.coords)[1:]):

   if line.type=='LineString':
       for seg_start, seg_end in zip(list(line.coords),list(line.coords)[1:]):
        G.add_edge(seg_start, seg_end)
   elif line.type=='MultiString':
       for mline in line:
           for seg_start, seg_end in zip(list(mline.coords), list(mline.coords)[1:]):
               G.add_edge(seg_start, seg_end)
logging.info('5')
#nx.draw_networkx_nodes(G, node_size=10, node_color='r')
logging.info('4')
nx.draw(G, with_labels=True, font_weight='bold')
#nx.draw_networkx_edges(G,  edge_color='b')
logging.info('5')

plt.show()