def search(A,B):
    # A is the rotated sorted array
    # B is the value to be searched
    length = len(A)
    low = 0
    high = length - 1
    while low <= high :
        mid = low + (high - low) // 2
        if A[mid] == B :
            return mid
        elif A[mid] >= A[low] : # left side sorted
            if B >= A[low] and B < A[mid] :
                high = mid - 1
            else:
                low = mid + 1
        else: # right side sorted
            if B > A[mid] and B <= A[high] :
                low = mid + 1
            else:
                high = mid - 1
    return -1

# test case
A = [4,5,6,7,8,1,2,3]
B = 6
ans = search(A,B)
print(ans)
