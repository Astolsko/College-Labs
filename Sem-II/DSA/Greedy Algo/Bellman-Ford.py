import sys
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
def bellman_ford(graph, src):
    dist = [sys.maxsize] * graph.V
    dist[src] = 0
    for i in range(graph.V - 1):
        for u, v, w in graph.graph:
            if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in graph.graph:
        if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return
    return dist
def main():
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)
    src = 0
    dist = bellman_ford(g, src) #src -> source vertex
    print("Vertex \t Distance from Source")
    for i, d in enumerate(dist):
        print(f"{i}\t {d}")

main()
