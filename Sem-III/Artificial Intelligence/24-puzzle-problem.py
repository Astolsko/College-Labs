import heapq
import copy

# Goal state
goal_state = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 0]  # 0 is the empty space
]

# Moves in (row, col) format: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Calculate Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(5):
        for j in range(5):
            if state[i][j] != 0:
                target_x, target_y = divmod(state[i][j] - 1, 5)
                distance += abs(target_x - i) + abs(target_y - j)
    return distance

# Find the position of the empty tile (0)
def find_empty_tile(state):
    for i in range(5):
        for j in range(5):
            if state[i][j] == 0:
                return (i, j)

# Generate the next possible states
def get_neighbors(state):
    neighbors = []
    empty_tile = find_empty_tile(state)
    x, y = empty_tile

    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if 0 <= new_x < 5 and 0 <= new_y < 5:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# A* algorithm
def a_star_search(initial_state):
    # Priority queue for A* (min-heap based on f = g + h)
    open_list = []
    
    # g_cost is the cost to reach the current state (number of moves)
    # h_cost is the heuristic (Manhattan distance)
    # f_cost = g_cost + h_cost
    g_cost = {str(initial_state): 0}
    h_cost = {str(initial_state): manhattan_distance(initial_state)}
    f_cost = {str(initial_state): g_cost[str(initial_state)] + h_cost[str(initial_state)]}
    
    # Push the initial state into the priority queue
    heapq.heappush(open_list, (f_cost[str(initial_state)], initial_state))
    
    # Dictionary to keep track of the parent of each state
    parent_map = {str(initial_state): None}
    
    # Set to store visited states
    closed_set = set()

    while open_list:
        # Get the state with the lowest f_cost
        _, current_state = heapq.heappop(open_list)
        
        # Check if we've reached the goal
        if current_state == goal_state:
            return reconstruct_path(current_state, parent_map), g_cost[str(current_state)]

        # Mark the current state as visited
        closed_set.add(str(current_state))

        # Explore neighbors
        for neighbor in get_neighbors(current_state):
            neighbor_str = str(neighbor)
            
            if neighbor_str in closed_set:
                continue

            tentative_g_cost = g_cost[str(current_state)] + 1  # Move to the neighbor

            # If this path to neighbor is better or neighbor has not been explored yet
            if neighbor_str not in g_cost or tentative_g_cost < g_cost[neighbor_str]:
                parent_map[neighbor_str] = current_state
                g_cost[neighbor_str] = tentative_g_cost
                h_cost[neighbor_str] = manhattan_distance(neighbor)
                f_cost[neighbor_str] = g_cost[neighbor_str] + h_cost[neighbor_str]

                # Add the neighbor to the priority queue
                heapq.heappush(open_list, (f_cost[neighbor_str], neighbor))

    return None, -1  # Return failure if no solution is found

# Reconstruct the path from the initial state to the goal state
def reconstruct_path(current_state, parent_map):
    path = []
    while current_state is not None:
        path.append(current_state)
        current_state = parent_map[str(current_state)]
    return path[::-1]  # Reverse the path

# Function to check if the current state is the goal state
def is_goal(state):
    return state == goal_state

# Random initial state for testing
initial_state = [
    [1, 2, 0, 3, 4],
    [6, 7, 8, 9, 5],
    [11, 12, 13, 10, 15],
    [16, 17, 18, 14, 19],
    [21, 22, 23, 24, 20]
]

# Solve the 24-puzzle problem using A* algorithm
solution_path, steps = a_star_search(initial_state)

if solution_path:
    print(f"Solution found in {steps} steps:")
    for state in solution_path:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
