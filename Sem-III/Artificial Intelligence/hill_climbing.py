import numpy as np
class EightPuzzle:
    def __init__(self, initial_state):
        self.state = initial_state
        self.goal_state = np.array([[1, 2, 3],
                                     [4, 5, 6],
                                     [7, 8, 0]])

    def get_zero_position(self):
        return tuple(np.argwhere(self.state == 0)[0])

    def get_neighbors(self):

        neighbors = []
        zero_pos = self.get_zero_position()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up,down,left and right

        for direction in directions:
            new_pos = (zero_pos[0] + direction[0], zero_pos[1] + direction[1])
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:  # ensure within boundary
                new_state = self.state.copy()
                # swap the blank tile 
                new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
                neighbors.append(new_state)
        
        return neighbors

    def heuristic(self, state):
        return np.sum(state != self.goal_state) - 1  # (-1) is for the blank tile
    
    def hill_climbing(self):
        current_state = self.state
        while True:
            neighbors = self.get_neighbors()  # Get neighboring states
            neighbor_costs = [self.heuristic(neighbor) for neighbor in neighbors]

            min_cost = min(neighbor_costs)
            min_index = neighbor_costs.index(min_cost)

            if self.heuristic(current_state) <= min_cost:
                break

            current_state = neighbors[min_index]
        
        return current_state, self.heuristic(current_state)

initial_state = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 0, 8]])

puzzle = EightPuzzle(initial_state)
solution, cost = puzzle.hill_climbing()

print("Final state:")
print(solution)
print("H-VALUE", cost)
