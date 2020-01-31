''' Leetcode 384：打乱一个没有重复元素的数组。

对于一个洗牌算法，我们对它的要求是能够以相等概率生成给定数组的任何一种排列。
即，对于n!种排列，都有相同概率生成。

Fisher-Yates 洗牌算法，渐进最优的洗牌算法，时间复杂度O(n)：
每次以相同的概率弹出一个数组中的任何一个元素，直到没有元素选择为止
或者从第一个元素开始遍历数组，随机选择这个元素或之后的一个元素，与它交换位置
这两种方法都有n!种等概率选择方式，故是一个有效的打乱算法
'''

import random # 我们需要一个能够生成均匀分布的函数
class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.original = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = list(self.original)
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        n = len(self.nums)
        for i in range(n):
            # 均匀概率选择
            pick = random.choice(range(i,len(self.nums))) 
            self.nums[i], self.nums[pick] = self.nums[pick], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
        
solution = Solution([1,2,3,4,5,6,7,8,9,0])
print('Original:')
print(solution.nums, '\n')
for i in range(6):
    print('Reset:')
    print(solution.reset())
    print('Shuffle:')
    print(solution.shuffle(),'\n')