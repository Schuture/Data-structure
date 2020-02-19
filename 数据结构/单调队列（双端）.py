'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
使用单调队列的方法解题

例如以下返回 [3,3,5,5,6,7]
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
'''

def maxSlidingWindow(snums, k):
    # window为递减队列，存放索引；res为返回的列表
    window ,res = [],[] 
    
    for i in range(len(nums)):
        
        # 不断删除队尾元素直到接下来插入新元素满足单调性
        while window and nums[window[-1]]<nums[i]: 
            window.pop()
            
        # 删除元素后插入新元素在num中索引，插入值必定大于所有删除值，保证了最大值存在性
        window.append(i)
        
        # 最大元素已超出窗口左端，过时了所以丢弃
        if window[0] == i-k: 
            window.pop(0)
            
        #要从第k个数据开始输出答案，前面是冷启动准备阶段
        if i >=k-1:
            res.append(nums[window[0]])
            
    return res

nums = [4,3,2,5,6,7,4,5,9,6,7,3,4,6,5,2,4,3,6,5,7,3,5,4,6,1,3,5,7,4,6,2,3,4]
k = 3

print(maxSlidingWindow(nums, k))