import heapq

def longest_runtime_first(process_no, arrival_time, burst_time):
    n = len(process_no)

    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    remaining_time = burst_time.copy()  

    # max-heap 
    pq = []
    current_time = 0
    completed = 0
    i = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    while completed != n:
        
        while i < n and arrival_time[i] <= current_time:
            # add process with negative remaining time for max-heap behavior
            heapq.heappush(pq, (-remaining_time[i], arrival_time[i], i))
            i += 1

        if pq:
            # Get the process with the longest remaining time
            _, _, index = heapq.heappop(pq)

            # Execute process for 1 unit of time
            current_time += 1
            remaining_time[index] -= 1

            if remaining_time[index] == 0:
                completion_time[index] = current_time
                turnaround_time[index] = completion_time[index] - arrival_time[index]
                waiting_time[index] = turnaround_time[index] - burst_time[index]
                completed += 1
            else:
                # If not complete reinsert with updated remaining time
                heapq.heappush(pq, (-remaining_time[index], arrival_time[index], index))

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
longest_runtime_first(process_no, arrival_time, burst_time)
