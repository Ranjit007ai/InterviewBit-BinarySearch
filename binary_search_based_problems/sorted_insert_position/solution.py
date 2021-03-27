def b_search(arr,key):
    length = len(arr)
    low = 0 
    high = length - 1
    res = -1
    while low <= high :
        mid = low + (high - low ) // 2
        if arr[mid] == key :
            return mid
        elif arr[mid] < key :
            res = mid 
            low = mid + 1
        else:
            high = mid - 1
    return res + 1

def find_pos_to_insert(A,key):
    # A is the sorted list
    # key is the value to be inserted
    position = b_search(A,key)
    return position

# test case
A = [1,3,5,8]
B = 2
position = find_pos_to_insert(A,B)
print(position)

