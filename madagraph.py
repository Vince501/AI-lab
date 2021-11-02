# importing networkx library
import networkx as nx

# importing matplotlib.pyplot library
import matplotlib.pyplot as plt

g = nx.Graph()

# creating nodes
g.add_node(1)
g.add_node(2)

# connecting nodes
g.add_edge(1, 2)



nx.draw(g)

plt.show()
