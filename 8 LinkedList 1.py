class Node():
    def __init__(self, data = None):
        self._data = data
        self._next = None

head = Node(10)
N2 = Node(20)
N3 = Node(30)
N4 = Node(40)

head._next = N2
N2._next = N3    
N3._next = N4

def printl(head):
    while head != None:
        print(head._data)
        head = head._next

def count(head):        #1
    if head._data == None:
        return 0
    count = 0
    while head != None:
        count += 1
        head = head._next
    return count

print(count(head))

def ith(head, i):       #2
    count = 0
    while head != None:
        if i == count:
            return head._data
        head = head._next
        count += 1
    return 'Out of bounds'

print(ith(head, 2))

def delete(head, i):        #3
    temp = head
    if i == 0:
        head = head._next
        return head
    else:
        count = 0
        while head._next != None and count < i - 1:
            head = head._next
            count += 1
        if head._next != None:
            head._next = head._next._next
        return temp

nh = delete(head, 4)
printl(nh)

def lenr(head):             #4
    if head == None:
        return 0
    return lenr(head._next) + 1

print(lenr(head))

def insr(head, i, data):        # 5
    if head == None:
        return head

    ret = insr(head._next, i-1, data)
    newnode = Node(data)

    if i == 0:
        newnode._next = ret
        head = newnode
    elif i == 1:
        head._next = newnode
        newnode._next = ret
    else:
        head._next = ret

    return head

nh = insr(head, 1, 50)
printl(nh)

def find(head, n):          # 7
    count = 0
    while head != None:
        if head._data == n:
            return count
        head = head._next
        count += 1
    return 'Not found'

print(find(head, 20))

def appendn(head, n):       # 8
    if n == 0 or n == count(head) or head == None:
        return head

    temp = head
    tailidx = count(head) - n - 1
    idx = 0
    while head != None and idx < tailidx:   # New tail
        head = head.next
        idx += 1
    newtail = head
    newhead = newtail._next

    while head._next != None:                # old tail
        head = head._next
    oldtail = head
    
    newtail._next = None
    oldtail._next = temp
    return newhead

nh = appendn(head, 4)
printl(nh)