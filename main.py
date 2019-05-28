import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()

n = 7  # 10 nodes
m = 20  # 20 edges

g = nx.gnm_random_graph(n, m,directed=True)

edges={n: adj for n, adj in g.adjacency()}
nodes=list(g.nodes())

max=0
a=0
b=0
for i in range(0,len(nodes)):
    for j in range(i+1,len(g.nodes)):
        intersection=list(set(edges[i]) & set(edges[j]))
        n=len(intersection)
        if n>max:
            a,b,max=i,j,n
print(a,b,max)
nx.draw(g , with_labels=True)
plt.show()