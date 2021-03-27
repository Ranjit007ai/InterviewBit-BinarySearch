# finding the sqrt using the binary search approach
def sqrt(number):
    low = 1
    high = number // 2
    res = 0
    while low <= high :
        mid  = low + (high - low) // 2 
        sq = mid * mid 
        if sq == number:
            return mid
        elif sq < number :
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res

number = 17
ans = sqrt(number)
print(ans)
