'''买卖股票系列题目'''
import numpy as np

class Buy_and_Sell():
    '''下面的函数都是动态规划的思想，dp[i][k][hold]的值表示第i天买卖了k次股票，
    手上有/没有股票时的最大盈利
		通用的状态转移方程:
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
    其中以下只有两个函数考虑最多买卖k次股票，其他都是无限次买卖'''
    def __init__(self, prices):
        self.prices = prices
        
    def maxProfit1(self): # 无限次买卖，无手续费
        n = len(self.prices)
        dp_i_0, dp_i_1 = 0, -float('inf') # 第零天
        for i in range(n):
            temp = dp_i_0 # 为了不被下面求今天的dp_i_0影响，保存起来
            dp_i_0 = max(dp_i_0, dp_i_1 + self.prices[i])
            dp_i_1 = max(dp_i_1, temp - self.prices[i])
        return dp_i_0
    
    def maxProfit2(self): # 只能买卖一次，无手续费
        n = len(self.prices)
        dp_i_0, dp_i_1 = 0, -float('inf') # 第零天
        for i in range(n):
            # 今天手上没股票，之前没买过或者之前买了今天卖掉
            dp_i_0 = max(dp_i_0, dp_i_1 + self.prices[i]) 
            # 今天手上有股票，要么是之前买的，要么是今天买的
            dp_i_1 = max(dp_i_1, - self.prices[i]) 
        return dp_i_0
    
    def maxProfit3(self): # 买卖不限，无手续费，但是卖出后要等一天才能再买
        # 问题可以看作，前天手上没了股票，今天才能买
        n = len(self.prices)
        dp_i_0, dp_i_1 = 0, -float('inf') # 第零天
        dp_pre_0 = 0 # 代表 dp[i-2][0]
        for i in range(n):
            temp = dp_i_0 # 昨天如果手上没股票的盈利
            # 今天手上没股票，之前没买过或者之前买了今天卖掉
            dp_i_0 = max(dp_i_0, dp_i_1 + self.prices[i]) 
            # 今天手上有股票，要么是之前买的，要么是今天买的
            dp_i_1 = max(dp_i_1, dp_pre_0 - self.prices[i]) 
            dp_pre_0 = temp # 作为明天的前天手上没股票的最大盈利
        return dp_i_0

    def maxProfit4(self, fee): # 买卖不限，有手续费
        cash, hold = 0, -self.prices[0] # 第一天把一开始有的钱拿在手上与买了第一天的股票，手上的钱
        for i in range(1, len(self.prices)):
            # 之前没买，之前买了今天卖掉。都是今天手上没有股票。
            cash = max(cash, hold + self.prices[i] - fee) 
            # 之前买了股票，之前没买股票今天买。都是今天手上有股票
            hold = max(hold, cash - self.prices[i]) 
        return cash # 最后一天手上必定是没有股票的
    
    def maxProfit5(self, k = 2): # 买卖限制k次，无手续费
        n = len(self.prices)
        if k > n/2: # 如果限制的次数大于理论上可能买卖的最多次数，就相当于没有限制
            return self.maxProfit1()
        
        dp = [[[0 for i in range(2)] for j in range(k+1)] for q in range(n)]
        for i in range(n):
            for j in range(k,0,-1):
                if i == 0: # 第一天的初始情况
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                    continue
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + self.prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - self.prices[i])
        # 穷举了 n × max_k × 2 个状态，正确。
        return dp[n-1][k][0] 


x = np.linspace(1,1000,1000)
prices = np.exp(x/1000) + 5 + 0.3 * np.random.randn(1000)

scheme = Buy_and_Sell(prices)
print(scheme.maxProfit1()) # 无限买卖
print(scheme.maxProfit2()) # 买卖一次
print(scheme.maxProfit3()) # 卖出后一天冷却
print(scheme.maxProfit4(4)) # 一次卖出交4块钱手续费，超过最大涨幅了
print(scheme.maxProfit4(0.05)) # 一次卖出只交五分钱手续费
print(scheme.maxProfit5(200)) # 限制最多卖出200次
