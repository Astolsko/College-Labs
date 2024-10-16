import threading
import time

flag = [False, False]  
turn = 0  
count1 = 0
count2 = 0
# max number of critical section entries 
max_count = 5

# critical section 
def critical_section(process_id):
    global count1, count2
    if process_id == 0:
        count1 += 1
        print(f"Process {process_id} is in the critical section. Count: {count1}")
    else:
        count2 += 1
        print(f"Process {process_id} is in the critical section. Count: {count2}")

    time.sleep(1) 

def process_0():
    global turn, flag

    for _ in range(max_count):
        flag[0] = True
        # Set turn to 1 give priority to process 1
        turn = 1
        # wait while process 1 wants to enter and it's its turn
        while flag[1] and turn == 1:
            pass  # Busy wait

        # enter
        critical_section(0)
        # exit
        flag[0] = False

def process_1():
    global turn, flag
    for _ in range(max_count):
        flag[1] = True
        turn = 0
        # Wait while process 0 wants to enter and it's its turn
        while flag[0] and turn == 0:
            pass  # Busy wait

        # enter
        critical_section(1)
        # exit
        flag[1] = False

t0 = threading.Thread(target=process_0)
t1 = threading.Thread(target=process_1)
t0.start()
t1.start()
t0.join()
t1.join()
print("Both processes completed.")
