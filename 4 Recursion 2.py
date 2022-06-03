def remdup(inp):        #2
    if len(inp) == 0 or len(inp) == 1:
        return inp
    sa = remdup(inp[1:])
    if inp[0] == sa[0]:
        return sa
    else:
        return inp[0] + sa

print(remdup('aabcddefggxyzz'))

def ab(inp):            #7
    if len(inp) == 0:
        return True
    if len(inp) == 1:
        if inp == 'a':
            return True
        else:
            return False

    if inp[0] == 'a':
        if inp[1] == 'a' or inp[1:3] == 'bb':
            return ab(inp[1:])

    if inp[:2] == 'bb':
        if inp[2] == 'a':
            return ab(inp[2:])

    return False

print(ab('abbaca'))

import copy

def subset(lst):        #10
    if len(lst) == 0:
        return [[0]]

    sa = subset(lst[:-1])
    dup = copy.deepcopy(sa)

    for i in sa:
        i[0] += 1
        i.append(lst[-1])

    for i in sa:
        dup.append(i)
 
    return dup

lst = [2,1,3,5,4]
sub = subset(lst)
print(sub)

def codes(inp):         #14
    if len(inp) == 0:
        return ['']
    
    out1 = [chr(int(inp[0]) + 96) + x for x in codes(inp[1:])]

    if len(inp) > 1 and int(inp[:2]) <= 26:
        out2 = [chr(int(inp[:2]) + 96) + x for x in codes(inp[2:])]
        out1.extend(out2)
    
    return out1

print(codes('1231413142'))