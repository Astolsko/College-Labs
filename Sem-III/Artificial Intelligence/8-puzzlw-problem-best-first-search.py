import heapq

# Manhattan distance heuristic
def manhattan_distance(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            # Find the position of the current tile in the goal state
            goal_pos = goal.index(state[i])
            # Calculate the Manhattan distance for each tile
            distance += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return distance

# Get the neighbors of the current state
def get_neighbors(state):
    neighbors = []
    empty_index = state.index(0)
    row, col = empty_index // 3, empty_index % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
            neighbors.append(tuple(new_state))
    return neighbors

# Best-First Search
def best_first_search(start, goal):
    # Priority queue for the states (heuristic value, state, path)
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start, goal), start, []))
    visited = set()

    while open_list:
        _, current_state, path = heapq.heappop(open_list)

        if current_state in visited:
            continue
        visited.add(current_state)

        # Goal reached
        if current_state == goal:
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                heapq.heappush(open_list, (manhattan_distance(neighbor, goal), neighbor, path + [current_state]))

    return None

# Define the start and goal states
start_state = (1, 2, 3,
               4, 0, 5,
               6, 7, 8)

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Run Best-First Search
solution = best_first_search(start_state, goal_state)

# Print the solution path
if solution:
    for step in solution:
        print(f"{step[0]} {step[1]} {step[2]}")
        print(f"{step[3]} {step[4]} {step[5]}")
        print(f"{step[6]} {step[7]} {step[8]}")
        print()
else:
    print("No solution found")
