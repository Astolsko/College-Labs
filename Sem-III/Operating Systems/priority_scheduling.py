import heapq
def priority_scheduling(process_no, arrival_time, burst_time, priority):
    n = len(process_no)

    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    # comparator for priority queue
    def cmp(i, j):
        if priority[i] == priority[j]:
            return arrival_time[i] > arrival_time[j]
        return priority[i] > priority[j]

    # Create priority queue
    pq = []
    current_time = 0
    completed = 0
    i = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    while completed != n:
        while i < n and arrival_time[i] <= current_time:
            # Push processes into priority queue
            heapq.heappush(pq, (priority[i], arrival_time[i], i))
            i += 1

        if pq:
            _, _, index = heapq.heappop(pq)

            current_time += burst_time[index]
            completion_time[index] = current_time

            turnaround_time[index] = completion_time[index] - arrival_time[index]
            waiting_time[index] = turnaround_time[index] - burst_time[index]
            completed += 1
        else:
            # No process available at the current time
            current_time += 1

    for i in range(n):
        total_turnaround_time += turnaround_time[i]
        total_waiting_time += waiting_time[i]

    print("Average Turnaround Time:", total_turnaround_time / n)
    print("Average Waiting Time:", total_waiting_time / n)
    print("Total Completion Time:", max(completion_time))

process_no = [1, 2, 3, 4, 5]
arrival_time = [1, 2, 3, 4, 5]
burst_time = [7, 5, 1, 2, 8]
priority = [7, 1, 3, 2, 10]

priority_scheduling(process_no, arrival_time, burst_time, priority)
