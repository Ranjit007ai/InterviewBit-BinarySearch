# using binary search to find the index of value and start checking both adjacents side since they are sorted
def b_search(arr,key):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high :
        mid = low + (high - low)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key :
            low = mid + 1
        else:
            high = mid - 1
    return -1

def occurence(arr,key):
    n = len(arr)
    # first find the index of the key 
    index = b_search(arr,key)
    # if the index = -1 ,means that value is not present , in that case we will return 0
    if index == -1:
        return 0
    else:
        # check counting the left sides of the index
        i = index - 1 
        count = 1
        while arr[i] == key and i >= 0:
            count += 1
            i -= 1
        # checking the count on right side of index
        i = index + 1
        while arr[i] == key and i < n :
            count += 1
            i += 1
        return count

arr = [ 2,3,4,5,5,5,5,6,7]
key = 5
ans = occurence(arr,key)
print(ans)

