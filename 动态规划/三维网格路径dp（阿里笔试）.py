'''
题目：小明在一个网格内，希望从起点到达终点。网格包含n行m列，包含S（起点）、
E（终点）、'.'（可以走的部分）、'#'（障碍物）。小明可以往上下左右四个方向
一次走一步，也可以瞬间移动到网格中对称处，即从A(x, y)到A(n+1-x, m+1-y)。
在最多瞬间移动5次的情况下，请问小明最少需要多长时间能够到终点？

输入：
第一行是两个数字n,m，表示网格的两个维度长度，2<= n,m <=500
之后n行是每一行的网格

输出：
输出一个数，即最短时间

***示例1：

输入：
5 8
E#S.....
#######.
........
.#######
........

输出：4

***示例2：

输入：
4 4
....
E#.S
#...
....

输出：2

'''

from functools import lru_cache
import sys
sys.setrecursionlimit(100000) # 递归深度100000，即最多走100000步

@lru_cache(None) # 记忆化
def minTime(i, j, fly): # 从i,j开始，最多飞fly次，最小花费多少时间到达终点
    if [i, j] == end: # 一开始就在终点
        return 0
    if (i, j, fly) in record: # 又回到这个状态，就直接返回无穷大，即不再考虑重走
        return float('inf') # lru_cache并不能代替这个判断，缺少这个判断会导致函数无限循环调用
    
    record.add((i, j, fly)) # 记录下已经经过这个状态
    case = [] # 存储五种走法的最小花费时间
    if i > 0 and grid[i-1][j] != '#':
        case.append(minTime(i-1, j, fly))
    if i < n-1 and grid[i+1][j] != '#':
        case.append(minTime(i+1, j, fly))
    if j > 0 and grid[i][j-1] != '#':
        case.append(minTime(i, j-1, fly))
    if j < m-1 and grid[i][j+1] != '#':
        case.append(minTime(i, j+1, fly))
    if fly > 0 and grid[n-1-i][m-1-j] != '#': # 使用0开始的索引，对称点是n-1-i, m-1-j
        case.append(minTime(n-1-i, m-1-j, fly-1))

    return min(case) + 1

if __name__ == '__main__':
    # 读入数据，并将数据填入列表
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input().strip()))
    
    # 找到起止点
    start = None
    end = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start = [i, j]
            elif grid[i][j] == 'E':
                end = [i, j]
                
    record = set() # 存储状态,如果已经遍历过，就直接返回
    
    result = minTime(start[0], start[1], 5)
    print(result if result < float('inf') else -1) # 填满dp数组

        