def allocate_resource(n, available, allocated, request):
    allocation = [0] * len(request)

    for i in range(len(request)):
        can_allocate = True

        for j in range(n):
            if request[i][j] > available[j]:
                can_allocate = False
                break

        if can_allocate:
            allocation[i] = 1
            for j in range(n):
                available[j] -= request[i][j]
                allocated[i][j] += request[i][j]

    return allocation


def wait_graph(available, allocation, allocated, request):
    process_count = len(request)
    matrix = [[] for _ in range(process_count)]

    for i in range(process_count):
        if allocation[i] == 1:  # Process i's request is not fully satisfied
            for j in range(process_count):
                if i != j:
                    for k in range(len(request[0])):
                        if request[i][k] > available[k] and allocated[j][k] > 0:
                            matrix[i].append(j)  # i waits for j
                            break
    return matrix


# function for cycle detection
def is_cyclic_util(adj, u, visited, rec_stack):
    if not visited[u]:
        visited[u] = True
        rec_stack[u] = True

        for x in adj[u]:
            if not visited[x] and is_cyclic_util(adj, x, visited, rec_stack):
                return True
            elif rec_stack[x]:
                return True

    rec_stack[u] = False
    return False


# to detect cycle in a directed graph
def is_cyclic(adj, V):
    visited = [False] * V
    rec_stack = [False] * V

    for i in range(V):
        if not visited[i] and is_cyclic_util(adj, i, visited, rec_stack):
            return True

    return False

def print_wait_graph(wait_graph):
    print("Wait-for graph:")
    for i in range(len(wait_graph)):
        print(f"Process {i} is waiting for: ", end="")
        if not wait_graph[i]:
            print("None")
        else:
            for j in wait_graph[i]:
                print(f"Process {j} ", end="")
        print()


if __name__ == "__main__":
    available = [3, 3, 2]  # Total available resources 
    n = len(available)
    # Allocate resources
    allocated = [
        [0, 1, 0],  # Resources allocated to Process 0
        [2, 0, 0],  # Resources allocated to Process 1
        [3, 0, 2],  # Resources allocated to Process 2
        [2, 1, 1],  # Resources allocated to Process 3
        [0, 0, 2],  # Resources allocated to Process 4
    ]
    
    # Resource requests for each process
    request = [
        [0, 0, 1], #request of Process 0
        [2, 0, 2], #request of Process 1
        [0, 1, 0], #request of Process 2
        [1, 0, 1], #request of Process 3
        [0, 0, 2], #request of Process 4
    ]

    allocation = allocate_resource(n, available, allocated, request)
    print("Allocation result:", allocation)
    process_count = len(request)

    # Create wait-for graph
    waitgraph = wait_graph(available, allocation, allocated, request)
    # print graph
    print_wait_graph(waitgraph)
    # Check for deadlock
    if is_cyclic(waitgraph, process_count):
        print("Deadlock detected.")
    else:
        print("Deadlock not detected.")
