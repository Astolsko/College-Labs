import heapq
def longest_job_first(process_no, arrival_time, burst_time):
    n = len(process_no)

    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    # maxheap to choose the process with longest burst time
    pq = []
    current_time = 0
    completed = 0
    i = 0  # Index to track process arrival
    total_turnaround_time = 0
    total_waiting_time = 0

    while completed != n:
        # Add processes to the heap that have arrived by the current time
        while i < n and arrival_time[i] <= current_time:
            heapq.heappush(pq, (-burst_time[i], arrival_time[i], i))  # Max-heap (use -burst_time to reverse order)
            i += 1

        if pq:
            # Pop process longest burst time
            _, _, index = heapq.heappop(pq)
            
            current_time += burst_time[index]
            completion_time[index] = current_time

            
            turnaround_time[index] = completion_time[index] - arrival_time[index]
            waiting_time[index] = turnaround_time[index] - burst_time[index]

            completed += 1
        else:
            
            current_time += 1

    total_turnaround_time = sum(turnaround_time)
    total_waiting_time = sum(waiting_time)

    print(f"Average Turnaround Time: {total_turnaround_time / n}")
    print(f"Average Waiting Time: {total_waiting_time / n}")
    print(f"Total Completion Time: {current_time}")

process_no = [1, 2, 3, 4]
arrival_time = [1, 2, 3, 4]
burst_time = [2, 4, 6, 8]
longest_job_first(process_no, arrival_time, burst_time)
