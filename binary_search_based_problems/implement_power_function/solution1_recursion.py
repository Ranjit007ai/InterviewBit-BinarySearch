def find_pow(x,n):
    if n == 0 :
        return 1
    return x * find_pow(x,n-1)

# test case
x = 2
n = 3
ans = find_pow(x,n)
print(ans)
