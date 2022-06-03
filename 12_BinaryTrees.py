class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    queue = [root]
    while len(queue) != 0:
        currNode = queue[0]
        queue.pop(0)

        leftChild = int(input())
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currNode.left = leftNode
            queue.append(leftNode)
        
        rightChild = int(input())
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currNode.right = rightNode
            queue.append(rightNode) 

    return root

def printLevelWise(root):
    queue = [root]
    while len(queue) != 0:
        currNode = queue[0]
        queue.pop(0)
        leftChild, rightChild = -1, -1

        if currNode.left != None:
            leftChild = currNode.left.data
            queue.append(currNode.left)
        
        if currNode.right != None:
            rightChild = currNode.right.data
            queue.append(currNode.right)

        if leftChild != -1 or rightChild != -1:
            print('{}\t: {}\t, {}'.format(currNode.data, leftChild, rightChild))

# root = takeInput()
# printLevelWise(root)

# root = None
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)
root.left.right.left = BinaryTreeNode(9)
root.left.right.right = BinaryTreeNode(10)
root.right.right.right = BinaryTreeNode(11)

# root = BinaryTreeNode(5)
# root.left = BinaryTreeNode(2)
# root.right = BinaryTreeNode(7)
# root.left.left = BinaryTreeNode(1)
# root.left.right = BinaryTreeNode(3)
# root.right.left = BinaryTreeNode(6)
# root.right.right = BinaryTreeNode(8)
# root.left.right.right = BinaryTreeNode(4)
# root.right.right.right = BinaryTreeNode(9)

# printLevelWise(root)
# print(' ')

def findNode(root, x):
    if root != None:
        if root.data == x:
            return True
        if findNode(root.left, x) or findNode(root.right, x):
            return True
    return False

# print(findNode(root, 12))

def height(root):
    # if root == None:
    #     return 0
    # return max(height(root.left), height(root.right)) + 1
    return 0 if root == None else max(height(root.left), height(root.right)) + 1

# print(height(root))

def mirror(root):
    if root == None: return
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)

# mirror(root)
# printLevelWise(root)

def pre(root):
    if root == None: return
    print(root.data, end = ' ')
    pre(root.left)
    pre(root.right)

# pre(root)
# print(' ')

def post(root):
    if root == None: return
    post(root.left)
    post(root.right)
    print(root.data, end = ' ')

# post(root)
# print(' ')

def ino(root):
    if root == None: return
    ino(root.left)
    print(root.data, end = ' ')
    ino(root.right)

# ino(root)

pre = [1, 2, 4, 8, 5, 9, 10, 3, 6, 7, 11]
post =[8, 4, 9, 10, 5, 2, 6, 11, 7, 3, 1]
ino = [8, 4, 2, 9, 5, 10, 1, 6, 3, 7, 11]

def preIno(pre, ino):
    if len(pre) == 0:
        return None
    root = BinaryTreeNode(pre[0])

    nIdxPre = 0
    nIdxIno = ino.index(pre[nIdxPre])
    lIno = ino[:nIdxIno]
    rIno = ino[nIdxIno+1:]
    lPre = pre[1:len(lIno)+1]
    rPre = pre[len(lIno)+1:]

    root.left = preIno(lPre, lIno)
    root.right = preIno(rPre, rIno)
    
    return root

# root = preIno(pre, ino)
# printLevelWise(root)

def postIno(post, ino):
    if len(post) == 0:
        return None

    nIdxPost = -1
    nIdxIno = ino.index(post[nIdxPost])

    lIno = ino[:nIdxIno]
    rIno = ino[nIdxIno+1:]

    lPost = post[:len(lIno)]
    # rPost = post[len(lIno):-2]
    rPost = post[len(lIno):len(lIno)+len(rIno)+1]

    root = BinaryTreeNode(post[-1])
    root.left = postIno(lIno, lPost)
    root.right = postIno(rIno, rPost)

    return root

# root = postIno(post, ino)
# printLevelWise(root)

def minMax(root):
    if root == None:
        return float('inf'), float('-inf')
    lMin, lMax = minMax(root.left)
    rMin, rMax = minMax(root.right)
    return min(root.data, lMin, rMin), max(root.data, lMax, rMax)

# print(minMax(root))

def sumNodes(root):
    if root == None:
        return 0
    return root.data + sumNodes(root.left) + sumNodes(root.right)

# print(sumNodes(root))

def isBalanced(root):
    if root == None:
        return True, 0
    lprop, lheight = isBalanced(root.left)
    rprop, rheight = isBalanced(root.right)

    prop = False
    if lprop and rprop and abs(lheight - rheight) <=1:
        prop = True
    height = max(lheight, rheight) + 1

    return prop, height

# print(isBalanced(root))

def levelTrav(root):
    queue = [root, -1]

    while len(queue) != 0:
        front = queue[0]
        queue.pop(0)

        if front == -1:
            print('')
            if len(queue) != 0:
                queue.append(-1)
        else:
            print(front.data, end = ' ')
            if front.left != None: queue.append(front.left)
            if front.right != None: queue.append(front.right)

# levelTrav(root)

def remLeaves(root):
    if root == None or (root.left == None and root.right == None):
        return None
    root.left = remLeaves(root.left)
    root.right = remLeaves(root.right)
    return root

# root1 = remLeaves(root)
# levelTrav(root1)

def zigzag(root):
    stack1 = [root]
    stack2 = []
    while len(stack1) != 0 or len(stack2) != 0:
        while len(stack1) != 0:
            top = stack1[-1]
            stack1.pop()
            print(top.data, end = " ")
            if top.left != None: stack2.append(top.left)
            if top.right != None: stack2.append(top.right)
        print('')
        while len(stack2) != 0:
            top = stack2[-1]
            stack2.pop()
            print(top.data, end = " ")
            if top.right != None: stack1.append(top.right)
            if top.left != None: stack1.append(top.left)
        print('')

# zigzag(root)

def noSibling(root):
    # if root.left == None and root.right == None:
    #     return root
    # elif root.left != None and root.right != None:
    #     noSibling(root.left)
    #     noSibling(root.right)
    # elif root.right == None:
    #     print(root.left.data)
    #     noSibling(root.left)
    # elif root.left == None:
    #     print(root.right.data)
    #     noSibling(root.right)
    
    if root.left == None:
        if root.right == None:
            return root
        else:
            print(root.right.data)
            noSibling(root.right)
    else:
        if root.right == None:
            print(root.left.data)
            noSibling(root.left)     
        else:
            noSibling(root.left)
            noSibling(root.right) 

# noSibling(root)