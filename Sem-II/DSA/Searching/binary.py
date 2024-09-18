import time

def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    array = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        element = int(input("Enter element " + str(i + 1) + ": "))
        array.append(element)
    array.sort()
    target = int(input("Enter the element to search: "))

    start_time = time.time()
    result = binary_search(array, target)
    end_time = time.time()

    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found in the array")

    print("Time taken:", end_time - start_time, "seconds")

main()
