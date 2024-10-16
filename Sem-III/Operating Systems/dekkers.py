import threading
import time

turn = 0  
flag = [False, False]  
count1 = 0
count2 = 0
# max num of entries into critical section
max_count = 5

#critical section
def critical_section(process_id):
    global count1, count2
    if process_id == 0:
        count1 += 1
        print(f"Process {process_id} is in the critical section : Count: {count1}")
    else:
        count2 += 1
        print(f"Process {process_id} is in the critical section : Count: {count2}")

    time.sleep(1)  

def process_0():
    global turn, flag

    for _ in range(max_count):
        flag[0] = True
        while flag[1]:
            if turn == 1:
                flag[0] = False
                while turn == 1:
                    pass
                flag[0] = True
        # enter
        critical_section(0)
        # exit
        turn = 1
        flag[0] = False

def process_1():
    global turn, flag
    for _ in range(max_count):
        flag[1] = True
        while flag[0]:
            if turn == 0:
                flag[1] = False
                while turn == 0:
                    pass
                flag[1] = True
        # enter
        critical_section(1)
        # exit
        turn = 0
        flag[1] = False

# start threads for both processes
t0 = threading.Thread(target=process_0)
t1 = threading.Thread(target=process_1)
t0.start()
t1.start()
t0.join()
t1.join()
print("Both processes completed.")
