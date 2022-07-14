# 1

# import random
# random.seed(42)
# random_matrix = [[random.randint(1,10) for _ in range(10)] for _ in range(12)]
# print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in random_matrix]))
# print(len(random_matrix[0]), 'x', len(random_matrix), 'matrix')

# def minPath(matrix):
#     matrix = ([-1] * len(matrix[0])) * len(matrix)

# matrix = ([-1] * len(random_matrix[0])) * len(random_matrix)
# # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
# print(matrix)

import copy
import numpy as np
np.random.seed(42)
random_matrix = np.random.randint(1, 10, (10,12))
# print(random_matrix)
# print(random_matrix.shape)

# matrix = np.ones((random_matrix.shape[0],random_matrix.shape[1])) * np.NINF
# print(matrix[0])

def minPath(matrix):
    # cost = np.ones((matrix.shape[0], matrix.shape[1])) * np.inf
    cost = copy.deepcopy(matrix)
    # cost[0][0] = matrix[0][0]
    for i in range(1, cost.shape[0]): cost[i][0] += cost[i-1][0]
    for j in range(1, cost.shape[1]): cost[0][j] += cost[0][j-1]
    for i in range(1, cost.shape[0]):
        for j in range(1, cost.shape[1]):
            cost[i][j] += min(cost[i-1][j], cost[i-1,j-1], cost[i,j-1])
    print(cost)
    return cost[-1][-1]

# print(minPath(random_matrix))

# 1.5
def LCS(s, t):
    cost = np.zeros((len(t)+1, len(s)+1)).astype(int)
    for i in range(1, cost.shape[0]):
        for j in range(1, cost.shape[1]):
            if t[i-1] == s[j-1]: cost[i][j] = cost[i-1][j-1] + 1
            else: cost[i][j] = max(cost[i][j-1], cost[i-1][j])
    print(cost)
    print(cost[-1][-1])

# LCS('Hippopotomonstrosesquipedaliophobic', 'Floccinaucinihilipilification')

#2
def editDist(s, t):
    if len(s) == 0 or len(t) == 0:
        return max(len(s), len(t))
    if s[0] == t[0]:
        return editDist(s[1:], t[1:])
    else:
        case1 = editDist(s, t[1:])      # Delete
        case2 = editDist(s[1:], t[1:])  # Replace
        case3 = editDist(s[1:], t)      # Insert
        return min(case1, case2, case3) + 1

# print(editDist('abc', 'dcb'))

def editDist(s, t, matrix):
    for i in range(matrix.shape[0]): matrix[i][0] = i
    for j in range(matrix.shape[1]): matrix[0][j] = j
    for i in range(1, matrix.shape[0]):
        for j in range(1, matrix.shape[1]):
            if s[i-1] == t[j-1]: 
                matrix[i][j] = matrix[i-1][j-1]
            else: 
                matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
    print(matrix)
    return matrix[-1][-1]

def helper(s, t):
    return editDist(s, t, (np.zeros((len(s)+1, len(t)+1))).astype(int))

# print(helper('abc', 'dcbedf'))

# 4
def knapsack(weights, values, W):
    if len(weights) == 0:
        return 0
    case1 = float('-inf')
    if W - weights[0] >= 0:                                                     # Take
        case1 = knapsack(weights[1:], values[1:], W - weights[0]) + values[0] 
    case2 = knapsack(weights[1:], values[1:], W)                                # Leave
    return max(case1, case2)

# print(knapsack([1,10,4,2,10], [6,120,20,3,6], 13))

# 5
def knapsack(weights, values, W, matrix):
    for i in range(1, matrix.shape[0]):
        for j in range(1, matrix.shape[1]):
            case1 = float('-inf')       
            if j >= weights[i-1]:           # Take
                case1 = values[i-1] + matrix[i-1][j-weights[i-1]]
            case2 = matrix[i-1][j]          # Leave
            matrix[i][j] = max(case1, case2)
    print(matrix.shape[0], matrix.shape[1])
    return matrix

def helper(weights, values, W):
    matrix = np.zeros((len(weights) + 1, W + 1)).astype(int)
    return knapsack(weights, values, W, matrix)

# print(helper([1,10,4,2,10], [6,120,20,3,6], 13))

# 6
def loothouses(input, output):
    output[1] = input[0]
    for i in range(2, len(output)):
        case1 = output[i-1]
        case2 = output[i-2] + input[i-1]
        output[i] = max(case1, case2)
    return output[-1]

def helper(input):
    if len(input) == 0: return 0
    return loothouses(input, [0]*(len(input)+1))

# print(helper([6,120,20,3,6]))

#7
def LIS(input):
    if len(input) == 0: 
        return 0
    currList = [-1]*len(input)
    totList = [-1]*len(input)
    currList[0], totList[0] = 1, 1

    for i in range(1, len(input)): 
        if input[i] > input[i-1]:
            currList[i] = currList[i-1] + 1
        else:
            currList[i] = 1
        totList[i] = max(totList[i-1], currList[i])
    
    # print(currList, totList)
    return totList[-1]

# print(LIS([5,6,1,2,3,4,1,2,1]))

# 9
def coins(coin, max):
    matrix = np.zeros((len(coin) + 1, max + 1)).astype(int)
    for i in range(matrix.shape[0]):
        matrix[i][0] = 1
    for i in range(1, matrix.shape[0]):
        for j in range(1, matrix.shape[1]):
            ans = matrix[i-1][j]
            if j >= coin[i-1]: ans += matrix[i][j - coin[i-1]]
            matrix[i][j] = ans
    print(matrix)
    return matrix[-1][-1]

# print(coins([1,2,5], 5))

# 11
def coinTower(N, X, Y):
    if N == 0: return False
    if N < 0: return True

    case1 = coinTower(N - 1, X, Y)
    case2 = coinTower(N - X, X, Y)
    case3 = coinTower(N - Y, X, Y)

    if case1 == True and case2 == True and case3 == True: return False
    else: return True

# if coinTower(10, 3, 5) == True:
#     print('Beerus Wins')
# else: print('Whis Wins')

def coinTowerMem(N, X, Y, output):
    if N == 0: return False
    if N < 0: return True

    if output[N] != -1: return output[N]

    case1 = coinTowerMem(N - 1, X, Y, output)
    case2 = coinTowerMem(N - X, X, Y, output)
    case3 = coinTowerMem(N - Y, X, Y, output)

    if case1 == True and case2 == True and case3 == True: output[N] = False
    else: output[N] = True

    # print(output)
    return output[N]

def helperMem(N, X, Y):
    output = [-1] * (N + 1)
    return coinTowerMem(N, X, Y, output)

# if helperMem(25, 4, 8) == True:
#     print('Beerus Wins')
# else: print('Whis Wins')

def coinTowerDP(N, X, Y):
    output = [-1] * (N + 1)
    output[0] = False
    
    for i in range(1, len(output)):
        case1 = output[i - 1]
        case2 = True
        if i >= X: case2 = output[i - X]
        case3 = True
        if i >= Y: case3 = output[i - Y]

        if case1 == True and case2 == True and case3 == True: output[i] = False
        else: output[i] = True
    
    print(output)
    return output[-1]

# if coinTowerDP(25, 4, 8) == True:
#     print('Beerus Wins')
# else: print('Whis Wins')

# 12

def maxSubSquare(input):
    output = np.zeros((input.shape[0] + 1, input.shape[1] + 1)).astype(int)

    # if input[0][0] == 0: output[0][0] = 1
    # else: output[0][0] = 0

    # for i in range(1, output.shape[0]):
    #     if input[i][0] == 0 or output[i-1][0] == 1: output[i][0] = 1
    #     else: output[i][0] = 0
    
    # for j in range(1, output.shape[1]):
    #     if input[0][j] == 0 or output[0][j-1] == 1: output[0][j] = 1
    #     else: output[0][j] = 0

    # for i in range(output.shape[0]):
    #     for j in range((output.shape[1])):
    #         if input[i-1][j] == 0 and input[i][j-1] == 0 and input[i-1][j-1] == 0 and output[i-1][j] == output[i][j-1] == output[i-1][j-1]:
    #             output[i][j] = max(output[i-1][j], output[i][j-1], output[i-1][j-1]) + 1
    #         else: output[i][j] = max(output[i-1][j], output[i][j-1], output[i-1][j-1])

    maxSub = 0

    for i in range(1, output.shape[0]):
        for j in range(1, output.shape[1]):
            if input[i-1][j-1] == 1: output[i][j] = 0
            else: output[i][j] = min(output[i-1][j], output[i][j-1], output[i-1][j-1]) + 1
            if output[i][j] > maxSub: maxSub = output[i][j]

    print(output)
    return maxSub

np.random.seed(42)
a = np.hstack((np.ones(100), np.zeros(775))).astype(int)
np.random.shuffle(a)
a = np.reshape(a, (25,35))
print(a, end = '\n\n')

print(maxSubSquare(a))