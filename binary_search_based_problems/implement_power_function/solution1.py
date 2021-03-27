
def find_power(x,n):
    # x is the base
    # n is the power
    res = 1
    i = 1
    while i <= n:
        res = res * x
        i += 1
    return res

# test case
x = 2
n = 3
ans = find_power(x,n)
print(ans)