def inter(arr1, arr2):          #3
    arr1.sort()
    arr2.sort()
    
    i = 0
    j = 0
    inter = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            inter.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    
    return inter

print(inter([1,2,3,4,5], [8,7,6,5,4,3]))

def pair(arr1, arr2, n):        #4
    arr1.sort()
    arr2.sort()

    i = 0
    j = len(arr2) - 1
    # count = 0
    lst = []

    while i < len(arr1) and j >= 0:
        sum = arr1[i] + arr2[j]
        if sum == n:
            lst.append([arr1[i], arr2[j]])
            i += 1
            j -= 1
        elif sum < n:
            i += 1
        else:
            j -=1
    
    return lst

print(pair([1,2,3,4,5], [8,7,6,5,4,3], 5))