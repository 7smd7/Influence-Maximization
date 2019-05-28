import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()

n = 7  # 10 nodes
m = 10  # 20 graph

g = nx.gnm_random_graph(n, m,directed=True)

graph={n: adj for n, adj in g.adjacency()}
nodes=list(graph.keys())
lenNodes=len(graph.keys())

intersections={}
for i in range(0,lenNodes):
    intersections[i]={}
    for j in range(0,lenNodes):
        intersection=list(set(graph[i]) & set(graph[j]))
        intersections[i][j]=intersection

activeNode={}
# deactiveNode= set(nodes)

def checkActivity( activeNode, m, n ):
    activeNode={m,n}.union(activeNode)
    toActive=set(intersections[m][n]) - activeNode
    merge=activeNode.union(toActive)
    ans=merge
    if toActive==[]:
        return []
    for i in range (0,len(toActive)):
        for j in range (0,len(activeNode)):
            ans=ans.union(checkActivity(merge,list(toActive)[i],list(activeNode)[j]))
        for j in range (i+1, len(toActive)):
            ans=ans.union(checkActivity(merge,list(toActive)[i],list(toActive)[j]))
    return ans

nx.draw(g , with_labels=True)
plt.show()
a=checkActivity(activeNode,nodes[0],nodes[1])
print(a)
print(intersections[nodes[0]][nodes[1]])
