from collections import deque
def round_robin(process_no, arrival_time, burst_time, time_quantum):
    n = len(process_no)
    completed_time = [0] * n
    turn_around_time = [0] * n
    waiting_time = [0] * n
    remaining_time = burst_time[:]
    
    # Sort processes by arrival time
    indices = list(range(n))
    indices.sort(key=lambda i: arrival_time[i])

    completed = 0
    current_time = 0
    ready_queue = deque()
    i = 0

    while completed != n:
        while i < n and arrival_time[indices[i]] <= current_time:
            ready_queue.append(indices[i])
            i += 1

        if ready_queue:
            index = ready_queue.popleft()

            time_spent = min(time_quantum, remaining_time[index])
            current_time += time_spent
            remaining_time[index] -= time_spent

            if remaining_time[index] == 0:
                completed_time[index] = current_time
                turn_around_time[index] = current_time - arrival_time[index]
                waiting_time[index] = turn_around_time[index] - burst_time[index]
                completed += 1

            while i < n and arrival_time[indices[i]] <= current_time:
                ready_queue.append(indices[i])
                i += 1

            if remaining_time[index] > 0:
                ready_queue.append(index)
        else:
            current_time += 1

    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turn_around_time)

    print(f"Average Waiting Time: {total_waiting_time / n:.2f}")
    print(f"Average Turnaround Time: {total_turnaround_time / n:.2f}")
    print(f"Completion Time: {current_time}")


process_no = [1, 2, 3, 4]         
arrival_time = [0, 1, 2, 4]      
burst_time = [5, 4, 2, 1]        
time_quantum = 3                   
round_robin(process_no, arrival_time, burst_time, time_quantum)
