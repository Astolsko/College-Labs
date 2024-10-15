import heapq
def best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    while priority_queue:
        _, node = heapq.heappop(priority_queue)
        # If the goal is reached
        if node == goal:
            print(f"Goal {goal} reached")
            return
        
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
heuristic = {
    'A': 5,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 3,
    'F': 0  
}
best_first_search(graph, 'A', 'F', heuristic)