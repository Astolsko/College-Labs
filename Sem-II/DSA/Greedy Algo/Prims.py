class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for i in range(vertices)] for i in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def prim(self):
        mst = []
        visited = [False] * self.V
        key = [float('inf')] * self.V

        key[0] = 0

        for _ in range(self.V):
            u = self.min_key(key, visited)
            visited[u] = True

            for v in range(self.V):
                if self.graph[u][v] and not visited[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    mst.append((u, v, self.graph[u][v]))

        return mst

    def min_key(self, key, visited):
        min_val = float('inf')
        min_index = None
        for i in range(self.V):
            if key[i] < min_val and not visited[i]:
                min_val = key[i]
                min_index = i
        return min_index

def main():
    vertices = 5
    g = Graph(vertices)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    mst = g.prim()
    print("Edges in the Minimum Spanning Tree (Prim's algorithm):")
    for u, v, weight in mst:
        print(f"{u} -- {v}  \tWeight: {weight}")
main()
