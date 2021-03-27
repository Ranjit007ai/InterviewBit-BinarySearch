def binary_search(arr,key):
    # the array will be sorted in ascending order
    n = len(arr)
    left = 0  #starting index
    right = n - 1  # last index
    while left <= right :
        mid = left + (right-left)//2
        if arr[mid] == key :
            return mid
        elif arr[mid] < key :
            left = mid + 1
        else:
            right = mid - 1
    return -1 # if the value is not present

# array should be sorted
arr = [2,3,6,7,39,40]
key = 39
ans = binary_search(arr,key)
print(ans)
