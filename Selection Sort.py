#Selection Sort
#Selection sort is a sorting algorithm that takes in a list and finds the smallest or greatest element in the unsorted list and moves it to the sorted portion of the list.

#Selection Sort implementation using new list
def selection_sort(lst):
    sorted_list = []
    for i in range(len(lst)):
        current_smallest = lst[0]
        current_smallest_index = 0
        for j in range(len(lst)):
            if lst[j] < current_smallest:
                current_smallest = lst[j]
                current_smallest_index = j
        sorted_list.append(lst.pop(current_smallest_index))
    return sorted_list
#Selection Sort implementation using swap method
def swap_selection_sort(lst):
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i,len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        
        if min_index != i:#Ensures we are not swapping to same index
            temp = lst[i]
            lst[i]= lst[min_index]
            lst[min_index] = temp
    return lst

test_selection = [1,4,6,23,1,3,7,9,3]
test_selection_swap = [1,4,6,23,1,3,7,9,3]
print(selection_sort(test_selection))
print(swap_selection_sort(test_selection_swap))

