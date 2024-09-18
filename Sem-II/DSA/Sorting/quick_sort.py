def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def main():
    n = int(input("Enter the number of elements: "))
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)

    print("\nOriginal Array:", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted Array:", sorted_arr)
main()
