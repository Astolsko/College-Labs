import os

def fork():
    pid = os.fork()

    if pid < 0:
        print("Fork failed!")
    elif pid == 0:
        print("Hello from Child process!")
    else:
        print("Hello from Parent process!")
        
fork()
