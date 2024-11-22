def first_fit(available, requests):
    partitions = len(available)
    no_process = len(requests)
    block_allocated = {}
    visited = [False] * partitions
    result = [False] * no_process

    for i in range(no_process):
        for j in range(partitions):
            if requests[i] <= available[j]:
                result[i] = True
                available[j] -= requests[i]
                visited[j] = True
                block_allocated[i + 1] = j + 1
                break

    for i in range(no_process):
        if result[i]:
            print(f"Process {i + 1} is allocated to block {block_allocated[i + 1]}")
        else:
            print(f"Process {i + 1} is not allocated")

available = [100, 500, 200, 300, 600]  # Memory blocks available
requests = [212, 417, 112, 426]       # Memory requests by processes
first_fit(available, requests)
