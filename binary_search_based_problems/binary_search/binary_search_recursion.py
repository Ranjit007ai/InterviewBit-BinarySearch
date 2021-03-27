# binary search using recursion approach
def b_search_recursion(arr,left,right,key):
    # base condition
    if left > right :
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == key :
        return mid
    if arr[mid] < key :
        return b_search_recursion(arr,mid + 1,right,key)
    else:
        return b_search_recursion(arr,left,mid - 1,key)
    
arr = [3,5,7,9,10,23]
key = 23
left = 0
right = len(arr) - 1
ans = b_search_recursion(arr,left,right,key)
print(ans)
