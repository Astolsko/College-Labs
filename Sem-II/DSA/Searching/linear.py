import time

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

def main():
    array = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        element = int(input("Enter element " + str(i + 1) + ": "))
        array.append(element)
    target = int(input("Enter the element to search: "))

    start_time = time.time()
    result = linear_search(array, target)
    end_time = time.time()

    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found in the array")

    print("Time taken:", end_time - start_time, "seconds")
main()
