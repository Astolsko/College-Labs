# binary search on list in python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  
def main():
    arr_input = input("Enter a list of numbers : ")
    arr = [int(x) for x in arr_input.split()]
    target = int(input("Enter the Element you want to search for: "))
    arr.sort()
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the list.")
main()
