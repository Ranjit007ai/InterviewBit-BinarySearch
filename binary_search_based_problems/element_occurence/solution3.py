# finding the first occurence  of the key using b_search ,let it be i index
# finding the last occurence of the key using b_search ,let it be j index
# so no of times the key occured will be (j - i + 1)
def b_search(arr,key,first_flag):
    length = len(arr)
    low = 0
    high = length - 1
    res = -1
    while low <= high :
        mid = low + (high - low)//2
        if arr[mid] == key :
            res = mid
            if first_flag: # incase of finding the first occurence
                high = mid - 1
            else: # incase of finding the last occurence
                low = mid + 1
        elif arr[mid] < key :
            low = mid + 1
        else:
            high = mid - 1
    return res

def occurence(arr,key):
    # finding the first occurence of the key
    first_index = b_search(arr,key,True)
    if first_index == -1: # if no element found
        return 0
    else:
        last_index = b_search(arr,key,False)
        out =( last_index - first_index + 1 )
        return out

arr = [2,2,2,3,3,4,5]
key = 1
ans = occurence(arr,key)
print(ans)