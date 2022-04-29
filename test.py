import math

def cal(n):
    if n == 0:
        return n
    else:
        k = math.floor(math.log(n, 2))
        n = n - 2**k
        print("^", k)
        return cal(n)

cal(100)
