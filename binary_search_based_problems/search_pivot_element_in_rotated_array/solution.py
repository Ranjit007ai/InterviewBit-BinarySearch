# prev_ele<=pivot_ele <=next_ele 

def pivot_ele(arr):
    length = len(arr)
    low = 0
    high = length - 1
    while low <=high:
        mid = low + (high - low) //2
        # if already sorted 
        if arr[low] <= arr[high] :
            return arr[low]
        prev_index = (mid + (length - 1)) % length
        next_index = (mid + 1) % length
        if arr[mid] <= arr[prev_index] and arr[mid] <= arr[next_index] :
            return arr[mid]
        elif arr[mid] >= arr[low]: 
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [7,8,9,1,2,4,6]
ans = pivot_ele(arr)
print(ans)        