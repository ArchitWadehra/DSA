# 1
def highFreq(lst):
    mydict = {}
    maxk, maxv = -1, -1
    firstKey = lst[0]
    for i in lst:
        val = 1 + mydict.get(i, 0)
        mydict[i] = val
        if (maxv < val) or (maxv <= val and i == firstKey):
            maxv = val
            maxk = i
    print(mydict.items())
    return maxk, maxv

# print(highFreq([2,1,1,1,1,2,3,1,3,2,1,4,5,6,2,2,2]))

# 2
def inter(lst1, lst2):
    map1, map2 = {}, {}
    for i in lst1:
        map1[i] = 1 + map1.get(i, 0)
    for i in lst2:
        map2[i] = 1 + map2.get(i, 0)
    lst = []
    for i in lst1:
        if map1[i] > 0 and map2[i] > 0:
            lst.append(i)
            map1[i] -= 1
            map2[i] -= 1
    return lst

# print(inter([1,1,2,3,4,1,2,3,2,1], [2,1,3,1,2,4]))

# 3
def pairSum(lst):
    mydict = {}
    for i in lst:
        mydict[i] = 1 + mydict.get(i, 0)
    count, pair = 0, []
    for i in lst:
        if -i in mydict and mydict[-i] > 0:
            count += 1
            pair.append((i, -i))
            mydict[i] -= 1
            mydict[-i] -= 1
    print(count)
    print(pair)

# pairSum([1,2,3,-1,4,-2,-3])

# 4 
def uniqChar(str):
    mydict, ans = {}, ''
    for i in str:
        mydict[i] = 1 + mydict.get(i, 0)
        if mydict[i] == 1: 
            ans += i
    return ans

print(uniqChar('abcdabcdefggfeeet'))