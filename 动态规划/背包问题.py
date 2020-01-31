'''
有限多维背包问题 LeetCode 474
在计算机界中，我们总是追求用有限的资源获取最大的收益。
现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。
每个 0 和 1 至多被使用一次。

示例
输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
输出: 4

解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
'''
def findMaxForm(strs, m, n):
    zeros = [s.count('0') for s in strs]
    ones = [s.count('1') for s in strs]
    # 多维背包问题，dp[i][j]表示最多能放i个0、j个1的背包最多放下的字符串数量
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    for k in range(len(strs)): # 第k个字符串（物品）
        # 注意由于每个字符串只能使用一次（即有限背包），因此在更新 dp(i, j) 时，
        # i 和 j 都需要从大到小进行枚举。这样可以保证大背包选择了第k件物品，小背包必定是没有这个选项的
        for i in range(m,-1,-1): # 这里要倒序遍历
            for j in range(n,-1,-1):
                if i >= zeros[k] and j >= ones[k]: # 这个背包可以选择是否放第k个字符串
                    # 如果不放，就保持原来的字符串数量，放就找容量更小的背包放下的字符串数量+1
                    dp[i][j] = max(dp[i][j], dp[i-zeros[k]][j-ones[k]] + 1)
    return dp[m][n]

print(findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))


'''
01背包问题
有若干件物品，它们的重量和价值分别为Wi, Vi，一个固定大小的背包，最多能装某重量的物品
要求装的物品的最大价值

示例：W = [2,3,4,5,9], V = [3,4,5,8,10], capacity = 20
输出：
'''
def pack(W, V, capacity):
    n = len(W)
	# dp[i][j]表示现有容量i，有j样物品时的最大价值
	# 边界条件是没有容量、没有物品时的最大价值，都为0
    dp = [[0 for j in range(n+1)] for i in range(capacity+1)]
    for i in range(1, capacity+1):
        for j in range(1, n+1):
            if i-W[j-1] >= 0:
                dp[i][j] = max(dp[i-W[j-1]][j-1]+V[j-1], dp[i][j-1]) # 选第j件与不选
            else:
                dp[i][j] = dp[i][j-1] # 这一件物品超过了容量，没法选
    return dp[-1][-1]

W = [2, 2, 3, 1, 5, 2] 
V = [2, 3, 1, 5, 4, 3]
capacity = 10
print(pack(W, V, capacity))