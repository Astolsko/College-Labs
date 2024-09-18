import sys

def dijkstra(graph, src):
    n = len(graph)
    dist = [sys.maxsize] * n
    dist[src] = 0
    visited = [False] * n

    for _ in range(n):
        u = min_distance(dist, visited)
        visited[u] = True
        for v in range(n):
            if not visited[v] and graph[u][v] and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    return dist

def min_distance(dist, visited):
    min_dist = sys.maxsize
    min_index = None
    for i in range(len(dist)):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            min_index = i
    return min_index

def main():
    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    src = 0
    dist = dijkstra(graph, src)
    print("Vertex \t Distance from Source")
    for i, d in enumerate(dist):
        print(f"{i}\t {d}")

main()
