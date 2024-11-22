def best_fit(available, requests):
    partitions = len(available)
    no_process = len(requests)
    block_allocated = {}
    result = [False] * no_process

    for i in range(no_process):
        min_size = float('inf')
        block_index = -1
        # Find the smallest block that can accommodate the request
        for j in range(partitions):
            if requests[i] <= available[j] and available[j] < min_size:
                min_size = available[j]
                block_index = j
        # Allocate the block if a suitable one is found
        if block_index != -1:
            result[i] = True
            available[block_index] -= requests[i]
            block_allocated[i + 1] = block_index + 1
    for i in range(no_process):
        if result[i]:
            print(f"Process {i + 1} is allocated to block {block_allocated[i + 1]}")
        else:
            print(f"Process {i + 1} is not allocated")

available = [100, 500, 200, 300, 600]  # Memory blocks available
requests = [212, 417, 112, 426]       # Memory requests by processes
print("Best Fit Allocation:")
best_fit(available, requests)
