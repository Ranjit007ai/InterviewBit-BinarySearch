def matrix_search(mat,key):
    
    rows = len(mat)
    cols = len(mat[0])
    # since the matrix is sorted both row and column wise
    # applying binary_search row wise
    min_row = 0
    max_row = rows - 1
    row_res = 0
    #return min_row,max_row
    while min_row <= max_row :
        mid = min_row + (max_row - min_row) // 2
        if mat[mid][0] == key :
             return True
        elif mat[mid][0] < key :
            row_res = mid 
            min_row = mid + 1
        else:
            max_row = mid - 1

        # now doing binary search in that row column wise

    
    low = 0
    high = cols - 1
    while low <= high :
        mid = low + (high - low ) // 2
        if mat[row_res][mid] == key :
            return True
        elif mat[row_res][mid] < key :
            low = mid + 1
        else:
            high = mid - 1
    return False
    

# test case
mat = [
        [1,3,5],
        [7,9,10],
        [10,12,13]
      ]

key = 32
#print('hello world')
index = matrix_search(mat,key)
print(index)

        
