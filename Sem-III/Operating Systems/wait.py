import os

def fork():
    pid = os.fork()

    if pid < 0:
        print("Fork failed!")
    elif pid == 0:
        print("Hello from Child process!")
        os._exit(0)  # Child exits here
    else:
        print("Hello from Parent process!")
        os.wait()    # Parent waits for the child to finish
        print("Child process has terminated.")

fork()
