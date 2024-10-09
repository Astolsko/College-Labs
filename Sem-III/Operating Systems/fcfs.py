def first_come_first_serve(process_no, arrival_time, burst_time):
    turn_around_time = []
    waiting_time = []
    n = len(process_no)

    indexes = list(range(n))

    # Sort based on arrival_time
    indexes.sort(key=lambda i: arrival_time[i])

    completion_time = 0  # Initialize to 0 to represent the system's start time

    for i in indexes:
        if completion_time < arrival_time[i]:
            completion_time = arrival_time[i]  # Idle until the process arrives
        
        completion_time += burst_time[i]
        tat = completion_time - arrival_time[i]  
        turn_around_time.append(tat)
        wt = tat - burst_time[i]  
        waiting_time.append(wt)

    sum_turn = sum(turn_around_time)
    sum_wait = sum(waiting_time)

    avg_turn = sum_turn / n
    avg_wait = sum_wait / n

    print(f"The average turn around time is: {avg_turn}")
    print(f"The average waiting time is: {avg_wait}")

# Test Case
process_no = [1, 2, 3]
arrival_time = [1,1,0]
burst_time = [1,3,42]
first_come_first_serve(process_no, arrival_time, burst_time)
