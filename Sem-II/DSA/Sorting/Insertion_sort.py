def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def main():
    n = int(input("Enter the number of elements: "))
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)
    print("\nOriginal Array:", arr)
    insertion_sort(arr)
    print("Sorted Array:", arr)
main()
