# Creating a hash function in python

def create_hash_table(size):
    return [None] * size
def hash_func(value, size):
    return hash(value) % size

def insert(hash_table, value):
    key = hash_func(value, len(hash_table))
    if hash_table[key] is not None:
        print("Collision occurred Unable to insert")
        return 
    hash_table[key] = value
    print("Value inserted successfully")

def get(hash_table, value):
    key = hash_func(value, len(hash_table))
    return key, hash_table[key]

def display(hash_table):
    print("Hash Table:")
    for index, value in enumerate(hash_table):
        print(f"{index} -> {value}")

def main():
    size = int(input("Enter the size of the hash table: "))
    hash_table = create_hash_table(size)
    while True:
        print("\n1. Insert value")
        print("2. Retrieve value")
        print("3. Display hash table")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            value = input("Enter value: ")
            insert(hash_table, value)
        elif choice == '2':
            value = input("Enter value to retrieve: ")
            result = get(hash_table, value)
            if result is not None:
                print(f"Value found: {result}")
            else:
                print("Value not found.")
        elif choice == '3':
            display(hash_table)
        elif choice == '4':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")
main()

