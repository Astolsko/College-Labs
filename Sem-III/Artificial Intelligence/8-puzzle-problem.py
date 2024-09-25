import heapq
def manhattan_distance(start, goal):
    distance = 0
    for i in range(1, 9):
        start_index = start.index(i)
        goal_index = goal.index(i)
        distance += abs(start_index // 3 - goal_index // 3) + abs(start_index % 3 - goal_index % 3)
    return distance


def get_neighbors(state):
    neighbors = []
    empty_index = state.index(0)
    row, col = empty_index // 3, empty_index % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
            neighbors.append(tuple(new_state))
    return neighbors

# A* algo
def a_star(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (manhattan_distance(start, goal), 0, start, []))
    visited = set()

    while priority_queue:
        heuristic, cost, current_state, path = heapq.heappop(priority_queue)

        if current_state in visited:
            continue

        visited.add(current_state)

        # Goal reached
        if current_state == goal:
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                new_cost = cost + 1
                heapq.heappush(priority_queue, (new_cost + manhattan_distance(neighbor, goal), new_cost, neighbor, path + [current_state]))

    return None


start_state = (1, 2, 3,
               4, 0, 5,
               6, 7, 8)

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

solution = a_star(start_state, goal_state)

if solution:
    for step in solution:
        print(f"{step[0]} {step[1]} {step[2]}")
        print(f"{step[3]} {step[4]} {step[5]}")
        print(f"{step[6]} {step[7]} {step[8]}")
        print()
else:
    print("No solution found")
