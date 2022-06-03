def pi(inp):        #1
    if len(inp) == 0:
        return ''
    if inp[:2] == 'pi':
        return '3.14' + pi(inp[2:])
    return inp[0] + pi(inp[1:])

def rem(inp, x):    #2
    if len(inp) == 0:
        return ''
    if inp[0] == x:
        return rem(inp[1:], x)
    return inp[0] + rem(inp[1:], x)

def str2int(inp):   #3
    if len(inp) == 0:
        return 0
    return int(inp[-1]) + (str2int(inp[:-1]) * 10)

def star(inp):      #4
    if len(inp) == 0:
        return ''
    if len(inp) == 1:
        return inp
    SmallAns = star(inp[1:])
    if inp[0] == SmallAns[0]:
        return inp[0] + '*' + SmallAns
    return inp[0] + SmallAns

print(pi('piabcpixyzpiuvwpi'))
print(rem('xabcxuvwx', 'x'))
print(str2int('1234'))
print(star('aabcxyzzuvvwpp'))