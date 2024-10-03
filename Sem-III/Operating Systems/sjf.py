import heapq

def shortest_job_first(process_no, arrival_time, burst_time):
    n = len(process_no)

    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    # Custom comparator for the priority queue
    def cmp(i, j):
        if burst_time[i] == burst_time[j]:
            return arrival_time[i] > arrival_time[j]
        return burst_time[i] > burst_time[j]

    pq = []
    current_time = 0
    completed = 0
    i = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    while completed != n:
        # add processes to the priority queue when they arrive
        while i < n and arrival_time[i] <= current_time:
            heapq.heappush(pq, (burst_time[i], i))  # Push by burst time (SJF)
            i += 1

        if pq:
            # Pop the process with the smallest burst time
            _, index = heapq.heappop(pq)
            
            # Execute the process
            current_time += burst_time[index]
            completion_time[index] = current_time

            turnaround_time[index] = completion_time[index] - arrival_time[index]
            waiting_time[index] = turnaround_time[index] - burst_time[index]

            completed += 1
        else:
            # If no process is ready, increment time
            current_time += 1

    # Calculate average turnaround time and waiting time
    total_turnaround_time = sum(turnaround_time)
    total_waiting_time = sum(waiting_time)

    print(f"Average Turnaround Time: {total_turnaround_time / n}")
    print(f"Average Waiting Time: {total_waiting_time / n}")
    
    print(f"Total Completion Time: {completion_time[-1]}")


process_no = [1, 2, 3, 4, 5]
arrival_time = [1, 2, 3, 4, 5]
burst_time = [7, 5, 1, 2, 8]
shortest_job_first(process_no, arrival_time, burst_time)
