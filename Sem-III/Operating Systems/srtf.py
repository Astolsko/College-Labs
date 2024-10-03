import heapq
def shortest_remaining_time_first(process_no, arrival_time, burst_time):
    n = len(process_no)

    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    remaining_time = burst_time.copy()

    # Custom comparator for priority queue
    pq = []
    current_time = 0
    completed = 0
    i = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    while completed != n:
        
        while i < n and arrival_time[i] <= current_time:
            heapq.heappush(pq, (remaining_time[i], arrival_time[i], i))  
            i += 1

        if pq:
            # Pop the process with the smallest remaining time
            remaining, _, index = heapq.heappop(pq)
            
            # execute for 1 unit of time
            current_time += 1
            remaining_time[index] -= 1
            
            # if process is completed
            if remaining_time[index] == 0:
                completion_time[index] = current_time
                turnaround_time[index] = completion_time[index] - arrival_time[index]
                waiting_time[index] = turnaround_time[index] - burst_time[index]
                completed += 1
            else:
                # If not completed push it back into the queue
                heapq.heappush(pq, (remaining_time[index], arrival_time[index], index))

        else:
            # If no process is ready increment the current time
            current_time += 1

    # Calculate average turnaround and waiting times
    total_turnaround_time = sum(turnaround_time)
    total_waiting_time = sum(waiting_time)

    print(f"Average Turnaround Time: {total_turnaround_time / n}")
    print(f"Average Waiting Time: {total_waiting_time / n}")
    print(f"Total Completion Time: {current_time}")


process_no = [1, 2, 3, 4]
arrival_time = [0, 1, 2, 3]
burst_time = [5, 4, 2, 1]
shortest_remaining_time_first(process_no, arrival_time, burst_time)
