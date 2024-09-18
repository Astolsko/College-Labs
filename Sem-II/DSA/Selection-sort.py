# Implement selection sort 
def selection_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Iterate over each element in the array
        min_idx = i  # Assume the current index is the minimum
        for j in range(i+1, n):  # Iterate over remaining elements
            if arr[j] < arr[min_idx]:  # If we find a smaller element
                min_idx = j  # Update the index of the minimum element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the current element with the minimum element found
def insert_element(arr, element):

    arr.append(element) 
    selection_sort(arr)  
def display_list(arr):
    print("Current list:", arr) 
# Example usage
my_list = [5, 3, 8, 1, 2]
display_list(my_list)

insert_element(my_list, 4)
display_list(my_list)

insert_element(my_list, 6)
display_list(my_list)

insert_element(my_list, 0)
display_list(my_list)
