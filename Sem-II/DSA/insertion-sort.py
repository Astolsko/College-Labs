# Implement insertion sort algorithm

def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def insert_element(arr, element):
    arr.append(element)  
    insertion_sort(arr)  

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
