def min_max(mat,rows,cols):
    min_value = mat[0][0]
    max_value = mat[0][cols - 1]
    # for max value
    for i in range(1,rows):
        if mat[i][cols-1] > max_value :
            max_value = mat[i][cols-1]
    # for min value
    for i in range(1,cols):
        if mat[i][0] < min_value :
            min_value = mat[i][0]
    return min_value, max_value

def b_search(arr,key):
    length = len(arr)
    low = 0
    high = length - 1
    res = 0
    while low <= high :
        mid = low + (high - low) //2
        if arr[mid] == key :
            res = mid + 1
            low = mid + 1
        elif arr[mid] < key :
            res = mid + 1
            low = mid + 1
        else:
            high = mid - 1
    return res


def count_value(mat,mid):
    rows = len(mat)
    cols = len(mat[0])
    counts = 0
    for i in range(0,rows):
        count = b_search(mat[i],mid)
        counts += count
    return counts

def matrix_median(mat):
    rows = len(mat)
    cols = len(mat[0])
    min_value , max_value = min_max(mat,rows,cols)
    desired_value = ((rows*cols) + 1 )//2
    while min_value < max_value :
        mid = min_value + (max_value - min_value)//2
        counts = count_value(mat,mid)
        if counts < desired_value :
            min_value = mid  + 1
        else:
            max_value = mid
    return min_value



        

mat = [
        [1,3,5],
        [2,6,9],
        [3,6,9]
    ]
median = matrix_median(mat)
print(median)