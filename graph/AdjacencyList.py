def add_node(node, graph):
    global node_count
    if node in nodes:
        print(node, "Already in graph")
        return
    else:
        nodes.append(node)
        graph[node] = []


def add_edge(v1, v2, graph):
    if v1 not in graph:
        print(v1,"edge not in graph")
    elif v2 not in graph:
        print(v2,"not inn ngraph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[v1].append(v2)
        graph[v2].append(v1)


def delete_node(node, graph):
    if node not in graph:
        print(node, "not in graph")
        return None
    graph.pop(node)
    for i in graph:
        if node in graph[i]:
            graph[i].remove(node)


def delete_edge(v1,v2,graph):
    if v1 not in graph:
        print(v1,"not in graph")
    elif v2 not in graph:
        print(v2,"not in graph")
    else:
        graph[v1].remove(v2)
        graph[v2].remove(v1)


def DFS(node,graph,visited):
    if node not in graph:
        print('node not found')
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for a in graph[node]:
            DFS(a,graph,visited)


visited=set()
node_count = 0
nodes = []
graph = {}
add_node("A", graph)
add_node("B", graph)
add_node("C", graph)
add_node("D", graph)
add_node("E", graph)
add_edge("A", "B", graph)
add_edge("A", "C", graph)
add_edge("A", "D", graph)
add_edge("B", "D", graph)
add_edge("D", "E", graph)
add_edge("G", "B", graph)
add_edge("D", "C", graph)
for a, b in graph.items():
    print(a, b)




DFS('A',graph,visited)