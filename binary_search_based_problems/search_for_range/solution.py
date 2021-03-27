def b_search(arr,key,is_first_occurence):
    length = len(arr)
    low = 0 
    high = length - 1
    res = -1
    while low <= high :
        mid = low + (high - low) // 2
        if arr[mid] == key :
            res = mid 
            if is_first_occurence : # for finding the first occurence
                high = mid - 1
            else: # to find  the last occurence 
                low = mid + 1
        elif arr[mid] < key :
            low = mid + 1
        else:
            high = mid - 1
    return res
    

def find_range(A,B):
    # A is the sorted array
    # B is the value whose first and last occurence we have to find
    first_occurence = b_search(A,B,True)
    last_occurence = b_search(A,B,False)
    return [first_occurence , last_occurence]
 

# test case
A = [5,7,7,8,8,10]
B =  8
ans = find_range(A,B)
print(ans)