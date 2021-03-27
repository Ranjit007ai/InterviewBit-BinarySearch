def time_valid(A,time,C):
    no_of_painters = 1
    time_taken = 0
    length = len(C)
    for i in range(0,length):
        time_taken += C[i]
        if time_taken > time :
            no_of_painters += 1
            time_taken = C[i]
    if no_of_painters <= A:
        return True
    else:
        return False



def painter_partition(A,B,C):
    # A is the no of painters available
    # B is the total time units taken by each painter
    # C is the array of size N ,which contain length of the N boards
    # let say each painter takes 1 unit of time ,later we will multiply by B
    min_time = max(C)
    max_time = sum (C)
    result = 0
    while min_time <= max_time :
        mid = min_time + (max_time - min_time)//2
        if time_valid(A,mid,C) :
            result = mid 
            max_time = mid - 1
        else:
            min_time = mid + 1
    return (result * B) % 10000003 



# test case
A = 2
B = 5
C = [1,10]
minimum_time = painter_partition(A,B,C)
print(minimum_time)
