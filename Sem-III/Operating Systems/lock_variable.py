import threading
class LockVariable:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        with self.lock:
            self.value += 1
            print(f"Value incremented to: {self.value}")

    def decrement(self):
        with self.lock:
            self.value -= 1
            print(f"Value decremented to: {self.value}")

lock_var = LockVariable()
def increment_task():
    for _ in range(10):
        lock_var.increment()
def decrement_task():
    for _ in range(10):
        lock_var.decrement()
thread1 = threading.Thread(target=increment_task)
thread2 = threading.Thread(target=decrement_task)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f"Final value: {lock_var.value}")