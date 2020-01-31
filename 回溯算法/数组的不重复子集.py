''' Leetcode 90 子集II 
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的不重复子集'''
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        n = len(nums)
        nums.sort()
        def helper(idx, tmp):
            res.append(tmp)
            for i in range(idx, n): # 从当前数字遍历到最后一个
                if i > idx and nums[i] == nums[i-1]: # 这个数跟前面的相同，所以选过了
                    continue
                helper(i+1, tmp + [nums[i]]) # 在原来的基础上多选一个数
        helper(0, [])
        return res
    
if __name__ == '__main__':
    A = [0,1,2,2,3]
    solution = Solution()
    print(solution.subsetsWithDup(A))