#Binary Search algorithm implementation

def Binary_Search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high) // 1 #Rounds down
        if list[mid] == item:
            return item
        elif list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
test_binary = [1,2,3,4,5,6,7,8,19]
print(Binary_Search(test_binary,-1))