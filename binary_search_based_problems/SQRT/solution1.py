def sqrt(number):
    i = 1
    while i*i <= number :
        i += 1
    return i - 1


number = 35
ans = sqrt(number)
print(ans)