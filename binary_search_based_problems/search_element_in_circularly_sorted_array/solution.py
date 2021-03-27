def search_rotated_array(arr,key):
    length = len(arr)
    low = 0 
    high = length - 1
    while low <= high :
        mid = low + (high - low) // 2
        if arr[mid] == key :
            return mid
        elif arr[mid] >= arr[low] : # in case of left side is sorted
            if key >=arr[low] and key < arr[mid] : # if the key is b/w left side range
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] <= arr[high] : # in case of right side is sorted
            if key > arr[mid] and key <= arr[high] : # if the key is b/w right side range
                low = mid + 1
            else:
                high = mid - 1
    return -1


arr = [6,7,9,12,45,2,3,4,5]
key = 5
ans = search_rotated_array(arr,key)
print(ans)


