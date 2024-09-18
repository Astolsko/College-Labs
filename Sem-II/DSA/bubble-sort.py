# Implement bubble sort

def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Iterate over each element in the array
        for j in range(0, n-i-1):  # Last i elements are already in place
            if arr[j] > arr[j+1]:  # If current element is greater than the next one
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap them

def insert_element(arr, element):
    arr.append(element)  
    bubble_sort(arr) 
def display_list(arr):
    print("Current list:", arr)  

# Example usage
my_list = [5, 3, 8, 1, 2]
display_list(my_list)

insert_element(my_list, 4)  # Insert 4 into the list
display_list(my_list)

insert_element(my_list, 6)  # Insert 6 into the list
display_list(my_list)

insert_element(my_list, 0)  # Insert 0 into the list
display_list(my_list)
