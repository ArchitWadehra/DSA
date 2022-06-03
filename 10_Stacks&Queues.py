# Stack
class StackArray(): 
    def __init__(self, size):
        self._stack = []
        self._size = size
    
    def push(self, item):
        if len(self._stack) < self._size:
            self._stack.append(item)
        else:
            print('Overflow')
    
    def pop(self):
        if not self.is_empty():
            tope = self.top()
            self._stack.pop()
            return tope
        else:
            return 'Underflow'
        
    def top(self):
        if not self.is_empty():
            return self._stack[-1]
        else:
            return 'None'
    
    def is_empty(self):
        return len(self._stack) == 0
    
    def __len__(self):
        return len(self._stack)

# if __name__ == '__main__':
#     lst = [10,20,30,40]
#     S1 = StackArray(3)

#     print('Pushing : \n')
#     for i in lst:
#         S1.push(i)
#         print(S1.top())
#         print(len(S1), S1.is_empty(), '\n')
    
#     print('popping : \n')
#     for i in lst:
#         print(S1.pop())
#         print(S1.top())
#         print(len(S1), S1.is_empty(), '\n')

# Queue
class ArrayQueue():
    def __init__(self, size):
        self._queue = [0]*size
        self._first = -1
        self._last = -1
    
    def is_empty(self):
        return self._first == -1
    
    def __len__(self):
        if self.is_empty():
            return 0
        else:
            leng = self._last - self._first + 1
            if leng > 0:
                return leng
            else:
                return len(self._queue) + leng
    
    def first(self):
        if self.is_empty():
            return 'Empty'
        return self._queue[self._first]
    
    def enqueue(self, item):
        if len(self) < len(self._queue):
            self._last = (self._last + 1) % len(self._queue)
            self._queue[self._last] = item
            if self._first == -1:
                self._first = 0
        else:
            print('   Overflow')
    
    def dequeue(self):
        if self.is_empty():
            return '   Underflow'
        else:
            ret = self._queue[self._first]

            if self._first == self._last:
                self._first = -1
                self._last = -1
            else:
                self._first = (self._first + 1) % len(self._queue)

            return ret

    def printq(self):
        style = [' ']
        for i in range(len(self._queue)):
            if i == self._first and i == self._last:
                style.append('fl' + str(len(str(self._queue[i])) * ' '))            
            elif i == self._first:
                style.append('f ' + str(len(str(self._queue[i])) * ' '))
            elif i == self._last:
                style.append('l ' + str(len(str(self._queue[i])) * ' '))
            else:
                style.append('  ' + str(len(str(self._queue[i])) * ' '))
        
        print('  ', self._queue)
        if self.is_empty():
            print('fl', ''.join(style))
        else:
            print('  ', ''.join(style))

# if __name__ == '__main__':
#     lst = [1000,2000,3000,4000]
#     Q1 = ArrayQueue(3)

#     Q1.printq()

#     print('\nEnqueue : \n')
#     for i in lst:
#         Q1.enqueue(i)
#         Q1.printq()
    
#     print('\nDequeue : \n')
#     for i in lst:
#         print(Q1.dequeue())
#         Q1.printq() 

import copy

# 2
def para(stri):
    S = StackArray(100)

    for i in stri:
        if i in '{[(':
            S.push(i)
        elif i in '}])':
            if(S.is_empty()):
                return False
            elif (S.top() == '{' and i == '}') or (S.top() == '[' and i == ']') or (S.top() == '(' and i == ')'):
                S.pop()
            else:
                return False
    
    return S.is_empty()

print(para("{{[()]}}"))

# 4
def rev(S1):
    S = copy.deepcopy(S1)   #To preserve original
    new = StackArray(100)
    for _ in range(len(S)):
        new.push(S.pop())
    return new

S1 = StackArray(100)
S1.push(10)
S1.push(20)
S1.push(30)

S2 = rev(S1)

while not S2.is_empty():
    print(S2.pop())

# 5
def revq(Q1):
    if Q1.is_empty():
        return

    fir = Q1.dequeue()
    revq(Q1)
    Q1.enqueue(fir)

Q1 = ArrayQueue(3)
Q1.enqueue(1)
Q1.enqueue(2)
# Q1.enqueue(3)
Q1.printq()

revq(Q1)
Q1.printq()

# 6 
def red(inp):
    S = StackArray(100)
    for i in inp:
        if i != ')':
            S.push(i)
        else:
            count = 0
            while S.pop() != '(':
                count += 1
            if count == 0:
                return True
    return False

print(red('(((a+b)))'))
    
# 7 
def span(stock):
    ans = []
    S = StackArray(len(stock))
    for i in stock:
        span = 1
        while not S.is_empty() and S.top()[0] < i:
            print('yes')
            span += S.top()[1]
            S.pop()
        S.push([i, span])
        ans.append(span)
    return ans

span = span([100, 80, 60, 70, 60, 75, 85])
print(span)

# 8 
def brev(inp):
    S = StackArray(len(inp))
    for i in inp:
        if i == '}' and S.top() == '{':
            S.pop()
        else:
            S.push(i)
    if len(S) % 2 == 0:
        return int(len(S)/2)
    else:
        return -1

print(brev('}}{{{{'))