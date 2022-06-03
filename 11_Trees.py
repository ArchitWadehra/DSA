class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def takeInputLevelWise():
    rootData = int(input('Root : '))
    root = TreeNode(rootData)

    queue = []
    queue.append(root)

    while len(queue) != 0:
        front = queue[0]
        queue.pop(0)

        numChild = int(input('No. children of ' + str(front.data) + ': '))

        for _ in range(numChild):
            childData = int(input('data : '))
            child = TreeNode(childData)
            front.children.append(child)
            queue.append(child)
    
    return root

def printLevelWise(root):
    queue = []
    queue.append(root)
    while len(queue) != 0:
        front = queue[0]
        queue.pop(0)
        print(front.data, end = ' : ')
        for i in range(len(front.children)):
            print(front.children[i].data, end = ' ')
            queue.append(front.children[i])
        print('\n')
            
# root = takeInputLevelWise()

root = TreeNode(1)
root.children = [TreeNode(2),TreeNode(3),TreeNode(4)]
root.children[0].children = [TreeNode(5), TreeNode(6)]
root.children[2].children = [TreeNode(9)]
root.children[0].children[1].children = [TreeNode(7), TreeNode(8)]

root1 = TreeNode(1)
root1.children = [TreeNode(2),TreeNode(3),TreeNode(4)]
root1.children[0].children = [TreeNode(5), TreeNode(6)]
root1.children[2].children = [TreeNode(9)]
root1.children[0].children[1].children = [TreeNode(7), TreeNode(8)]

# printLevelWise(root)

def sumOfNodes(root):
    smallAns = root.data
    for i in range(len(root.children)):
        smallAns += sumOfNodes(root.children[i])
    return smallAns

# print(sumOfNodes(root))

def maxDataNode(root):
    max = root.data
    for i in range(len(root.children)):
        retmax = maxDataNode(root.children[i])
        if max < retmax:
            max = retmax
    return max

# print(maxDataNode(root))

def getHeight(root):
    max = 0
    for i in range(len(root.children)):
        ret = getHeight(root.children[i])
        if max < ret:
            max = ret
    return max + 1

# print(getHeight(root))

def countLeaf(root):
    if len(root.children) == 0:
        return 1
    sum = 0
    for i in range(len(root.children)):
        sum += countLeaf(root.children[i])
    return sum

# print(countLeaf(root))

def postOrder(root):
    for i in range(len(root.children)):
        postOrder(root.children[i])
    print(root.data, end = ' ')

# postOrder(root)

def containsX(root, x):
    if root.data == x:
        return True
    for i in range(len(root.children)):
        if containsX(root.children[i], x):
            return True
    return False

# print(containsX(root, 9))

def countNodes(root):
    sum = 0
    for i in range(len(root.children)):
        sum += countNodes(root.children[i])
    return sum + 1

# print(countNodes(root))

def countNodesLargerX(root, x):
    sum = 1 if root.data > x else 0
    for i in range(len(root.children)):
        sum += countNodesLargerX(root.children[i], x)
    return sum

# print(countNodesLargerX(root, 5))

def sumt(root):
    # if len(root.children) == 0:
    #     return root.data
    csum = 0
    maxv = float('-inf')
    for i in range(len(root.children)):
        csum += root.children[i].data
        retsum = sumt(root.children[i])
        if maxv < retsum:
            maxv = retsum
    return max(maxv, root.data + csum)

# print(sumt(root))

def areIdentical(root, root1):
    if root.data != root1.data or len(root.children) != len(root1.children):
        return False
    for i in range(len(root.children)):
        if areIdentical(root.children[i], root1.children[i]) == False:
            return False
    return True

# print(areIdentical(root, root1))

def nextLarger(root, x):
    ans = root if root.data > x  else None
    for i in range(len(root.children)):
        temp = nextLarger(root.children[i], x)
        if temp == None:
            continue
        elif ans == None or ans.data > temp.data:
            ans = temp
    return ans

# ans = nextLarger(root, 1)
# if ans == None:
#     print('Not found')
# else:
#     print(ans.data)

def get2biggest(lst):
    large = float('-inf')
    slarge = float('-inf')
    for i in lst:
        if i > large:
            large = i
    for i in lst:
        if i > slarge and i != large:
            slarge = i
    return [large, slarge]
    # return sorted(lst, reverse = True)[0:2]    # O(nlogn)

def secLargest(root):
    ans = [root.data, float('-inf')]
    for i in range(len(root.children)):
        ans.extend(secLargest(root.children[i]))
    return get2biggest(ans)

# print(secLargest(root))