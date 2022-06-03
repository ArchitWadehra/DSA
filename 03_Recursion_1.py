def power(x, n):    #1
    if n == 0:
        return 1
    return power(x, n - 1) * x

print(power(2, 4))

def printTillOne(n):    #2
    if n == 0:
        return
    printTillOne(n - 1)
    print(n)

printTillOne(10)

def numDigits(n):       #3
    if n == 0:
        return 0
    return numDigits(n // 10) + 1

print(numDigits(10980))

def checkNumber(arr,n):     #5
    if len(arr) == 0:
        return False
    if arr[0] == n:
        return True
    return checkNumber(arr[1:], n)

print(checkNumber([1,2,3,4,5,6], 10))

def first(arr, n):      #6
    if len(arr) == 0:
        return -1
    if arr[0] == n:
        return 0
    SmallAns = first(arr[1:], n)
    if SmallAns == -1:
        return -1
    else:
        return SmallAns + 1

def last(arr, n):       #7
    if len(arr) == 0:
        return -1
    if arr[-1] == n:
        return len(arr) - 1
    SmallAns = last(arr[:-1], n)
    if SmallAns == -1:
        return -1
    else:
        return SmallAns

def all(arr, n):        #8
    if len(arr) == 0:
        return []
    SmallAns = all(arr[1:], n)
    if arr[0] == n:
        return [0] + [i+1 for i in SmallAns]
    else:
        return [i+1 for i in SmallAns]

arr = [2,3,4,5,1,3,1,4,2,3,4,1,4,1,4,5]
n = 1

print(first(arr, n))
print(last(arr, n))
print(all(arr, n))

def gp(n):      #11
    if n == 0:
        return 1
    return 1 + 0.5 * (gp(n-1))

print(gp(4))

def pal(str):       #12
    if len(str) == 1 or len(str) == 0:
        return True
    if len(str) == 2:
        if str[0] == str[1]:
            return True
        else: 
            return False

    if str[0] == str[-1] and pal(str[1:-1]):
        return True
    else:
        return False

print(pal('racecar'))