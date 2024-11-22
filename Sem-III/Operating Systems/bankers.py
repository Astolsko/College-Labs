def detect_safe_sequence(process_count, resource_count, allocated, requested, available):
    safe_sequence = []
    is_finished = [False] * process_count
    completed = False

    while True:
        completed = False

        for process in range(process_count):
            if is_finished[process]:
                continue

            # Check if requested resources are available 
            can_allocate = all(
                requested[process][resource] <= available[resource]
                for resource in range(resource_count)
            )

            # Allocate resources if requirements are met
            if can_allocate:
                for resource in range(resource_count):
                    available[resource] += allocated[process][resource]

                is_finished[process] = True
                completed = True
                safe_sequence.append(process)

        # If no resources were allocated in this pass, break the loop
        if not completed:
            break

    # Check if all processes are completed
    if not all(is_finished):
        return -1  # Deadlock detected

    # Print the safe sequence if no deadlock
    print("Safe Sequence:", safe_sequence)
    return 1  # No deadlock detected



allocation = [
    [0, 1, 0],
    [3, 0, 2],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
]

request = [
    [7, 4, 3],
    [0, 2, 0],
    [6, 0, 0],
    [0, 1, 1],
    [4, 3, 1],
]

available_resources = [2, 3, 0]  # Available resources
process_count = len(allocation)
resource_count = len(available_resources)
result = detect_safe_sequence(process_count, resource_count, allocation, request, available_resources)
if result == -1:
    print("Deadlock will occur")
else:
    print("Deadlock will not occur")
