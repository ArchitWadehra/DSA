class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = BinaryTreeNode(5)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(7)
root.left.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(3)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(8)
root.left.right.right = BinaryTreeNode(4)
root.right.right.right = BinaryTreeNode(9)

# root = BinaryTreeNode(1)
# root.left = BinaryTreeNode(2)
# root.right = BinaryTreeNode(3)
# root.left.left = BinaryTreeNode(4)
# root.left.right = BinaryTreeNode(5)
# root.right.left = BinaryTreeNode(6)
# root.right.right = BinaryTreeNode(7)
# root.left.left.left = BinaryTreeNode(8)
# root.left.right.left = BinaryTreeNode(9)
# root.left.right.right = BinaryTreeNode(10)
# root.right.right.right = BinaryTreeNode(11)

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

# printLevelWise(root)

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

def search(root, x):
    if root == None:
        return False
    # print(root.data)
    if root.data == x:
        return True
    elif root.data > x:
        return search(root.left, x)
    else:
        return search(root.right, x)

# print(search(root, 8))

def printRange(root, start, end):
    if root == None:
        return
    if end < root.data:
        printRange(root.left, start, end)
    elif start > root.data:
        printRange(root.right, start ,end)
    else:
        printRange(root.left, start, end)
        print(root.data, end = " ")
        printRange(root.right, start ,end)

# printRange(root, 6, 20)

# def checkBST(root):
#     if root == None:
#         return True
#     if root.left != None:
#         if root.left.data >= root.data:
#             return False
#     if root.right != None:
#         if root.right.data <= root.data:
#             return False
#     return checkBST(root.left) and checkBST(root.right)

def checkBST(root):
    if root == None:
        return float('inf'), float('-inf'), True
    lmin, lmax, lprop = checkBST(root.left)
    rmin, rmax, rprop = checkBST(root.right)

    nmin = min(root.data, lmin, rmin)
    nmax = max(root.data, rmax, lmax)

    # print(nmin, nmax, lprop and rprop and lmax < root.data and rmin > root.data)
    return nmin, nmax, lprop and rprop and lmax < root.data and rmin > root.data

# print(checkBST(root))

def BSTfromList(lst):
    if len(lst) == 0:
        return None
    rootidx = len(lst)//2
    llst = lst[:rootidx]
    rlst = lst[rootidx+1:]

    root = BinaryTreeNode(lst[rootidx])
    root.left = BSTfromList(llst)
    root.right = BSTfromList(rlst)

    return root

# root1 = BSTfromList([1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18])
# printLevelWise(root1)
# print(checkBST(root1))

# 6
def path(root, k):
    if root == None:
        return []
    elif root.data == k:
        return [k]
    elif root.data > k:
        pathl = path(root.left, k)
        if len(pathl) == 0: return []
        else: return [root.data] + pathl
    else:
        pathr = path(root.right, k)
        if len(pathr) == 0: return []
        else: return [root.data] + pathr

# print(path(root, 4))

# 8
import copy
def insDupli(root):
    if root == None:
        return
    
    insDupli(root.left)
    insDupli(root.right)

    newNode = BinaryTreeNode(root.data)
    newNode.left = root.left
    root.left = newNode


# printLevelWise(root)
# insDupli(root)
# print()
# printLevelWise(root)

# def pairSum(froot, root, n):
#     if root == None:
#         return

#     if search(froot, n - root.data):
#         print(root.data, n - root.data)
    
#     pairSum(froot, root.left, n)
#     pairSum(froot, root.right, n)
# pairSum(root, root, 10)

# 9
def treeToList(root):
    if root == None:
        return []
    return treeToList(root.left) + [root.data] + treeToList(root.right)

def pairSum(root, n):
    lst = treeToList(root)
    # print(lst)

    i, j = 0, len(lst)-1
    while j>i:
        if lst[i] + lst[j] == n:
            print(lst[i], lst[j])
            i,j = i+1, j-1
        elif lst[i] + lst[j] < n:
            i += 1
        else:
            j -= 1

# pairSum(root, 10)

# 10
def getLCA(root, a, b):
    if root == None:
        return -1
    if root.data == a or root.data == b:
        return  root.data

    leftAns = getLCA(root.left, a, b)
    rightAns = getLCA(root.right, a, b)

    if leftAns == -1 and rightAns == -1:
        return -1
    if leftAns != -1 and rightAns != -1:
        return root.data
    if leftAns != -1:
        return leftAns
    if rightAns != -1:
        return rightAns
    
# print(getLCA(root, 5, 10))

# 11
def getLCA(root, a, b):
    if root == None:
        return -1
    if root.data == a or root.data == b:
        return  root.data

    # leftAns = getLCA(root.left, a, b)
    # rightAns = getLCA(root.right, a, b)

    leftAns = -1
    rightAns = -1
    if root.data > a and root.data > b:
        leftAns = getLCA(root.left, a, b)
    elif root.data < a and root.data < b:
        rightAns = getLCA(root.right, a, b)
    else:
        leftAns = getLCA(root.left, a, b)
        rightAns = getLCA(root.right, a, b)

    if leftAns == -1 and rightAns == -1:
        return -1
    if leftAns != -1 and rightAns != -1:
        return root.data
    if leftAns != -1:
        return leftAns
    if rightAns != -1:
        return rightAns
    
# print(getLCA(root, 4, 2))