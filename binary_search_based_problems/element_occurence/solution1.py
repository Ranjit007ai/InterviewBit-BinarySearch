# counting the number of time the given number occured using Linear traversal approach
def occurence(arr,key):
    count = 0
    n = len(arr)
    for i in range(0,n):
        if arr[i] == key :
            count += 1
    return count


arr = [2,3,4,5,7,6,5,5,5]
key = 5
ans = occurence(arr,key)
print(ans)