queue = []
def enqueue(item):
  queue.append(item)
  print("Item added to queue:", item)
def dequeue():
  if not queue:
    print("Queue is empty.")
  else:
    item = queue.pop(0)
    print("Item removed from queue:", item)
    return item
def peek():
  if not queue:
    print("Queue is empty.")
  else:
    print("First item in queue:", queue[0])
def size():
  print("Queue size:", len(queue))
def main():
  while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Size")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
      item = input("Enter the item to enqueue: ")
      enqueue(item)
    elif choice == 2:
      dequeue()
    elif choice == 3:
      peek()
    elif choice == 4:
      size()
    elif choice == 5:
      break
    else:
      print("Invalid choice")
if __name__ == "__main__":
  main()
