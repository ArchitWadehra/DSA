import math

def minSteps(n):
    lst = [-1] * (n+1)
    lst[1] = 0
    for i in range(2, n+1):
        case1, case2, case3 = lst[i-1], float('inf'), float('inf')
        if i%2 == 0: case2 = lst[int(i/2)]
        if i%3 == 0: case3 = lst[int(i/3)]
        lst[i] = min(case1, case2, case3) + 1
    return lst[-1]

# print(minSteps(100))

def stairJumps(n):
    lst = [-1] * (n+1)
    lst[0], lst[1], lst[2] = 1, 1, 2
    for i in range(3, n+1):
        lst[i] = lst[i-1] + lst[i-2] + lst[i-3]
    return lst

# print(stairJumps(100))

def minCount(n):
    lst = [-1] * (n+1)
    lst[1] = 1
    for i in range(2, n+1):
        root = math.isqrt(i)
        if i == root**2:
            lst[i] = 1
        else:
            lst[i] = 1 + lst[i - root**2]
    return lst[1:]

# print(minCount(100))

def balancedBTs(h):
    lst = [-1] * (h+1)
    lst[0], lst[1] = 1, 1
    mod = 10**9 + 7
    for i in range(2, h+1):
        # lst[i] = ((lst[i-1] % mod) * ((lst[i-1] + 2*lst[i-2]) % mod) % mod)
        lst[i] = ((lst[i-1]*lst[i-1]) % mod + (2*lst[i-1]*lst[i-2]) % mod) % mod
    return lst

# print(balancedBTs(100))