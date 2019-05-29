import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()

n = 7  # nodes
m = 10  # directed edge

g = nx.gnm_random_graph(n, m,directed=True) #random directed graph(|V|=n,|E|=m)

graph={n: adj for n, adj in g.adjacency()} #make dic from graph
nodes=list(graph.keys())
lenNodes=len(nodes)
ans=set()
# make matrix of vertex for matual adjacency.
intersections={}
for i in range(0,lenNodes):
    intersections[i]={}
    for j in range(0,lenNodes):
        intersection=list(set(graph[i]) & set(graph[j]))
        intersections[i][j]=intersection

activeNode=set()
deactiveNode=set(nodes)
# deep activity finder with recursive func.
# So search what nodes will be active when you active m and n nodes and their intersections.
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


# find max influence for couple of first nodes.
max=0
a=0
b=0
for i in range(0,lenNodes):
    for j in range(i+1,lenNodes):
        influence=checkActivity(activeNode,nodes[i],nodes[j])
        n=len(influence)
        if n>max:
            a,b,max=i,j,n
        if max==lenNodes:
            break
ans.add(a)
ans.add(b)
activeNode=checkActivity(activeNode,list(deactiveNode)[a],list(deactiveNode)[b])
deactiveNode-=activeNode
if max==lenNodes:
    print("We need to active this nodes to active all:/n",ans)
    # print("To active these (max influence): "activeNode)
    exit()

for k in range(0, lenNodes - 2):
    max=0
    a=0
    b=0
    for i in range(0,len(deactiveNode)):
        for j in range(0,len(activeNode)):
            influence=checkActivity(activeNode,list(deactiveNode)[i],list(activeNode)[j])
            n=len(influence)
            if n>max:
                a,b,max=i,j,n
            if max==lenNodes:
                break
    activeNode=checkActivity(activeNode,nodes[a],nodes[b])
    deactiveNode-=activeNode
    ans.add(b)

print("We need to active this nodes to active all: ",ans)
print("To active these (max influence): ",activeNode)
    
nx.draw(g , with_labels=True)
plt.show()

