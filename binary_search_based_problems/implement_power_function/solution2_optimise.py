def find_pow(x,n):
    if n == 0:
        return 1
    temp = find_pow(x,n//2)
    if n % 2 == 0: # if even number
        return (temp * temp)
    else: # if odd number
        return (x * temp * temp)

# test case
x = 2
n = 3
ans = find_pow(x,n)
print(ans)