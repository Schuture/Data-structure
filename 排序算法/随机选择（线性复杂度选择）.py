import random
import time

n = 1000000

class Selection(): # 线性时间复杂度选择算法
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
        
    def partition1(self, p, r): # A[p,r]包含首尾
        x = self.nums[r] # 最右边那个数
        i = p # 将j指针第一次遇到的小于x的数字搬到这里
        for j in range(p,r): # 希望A[j]比x大，所以遇到比x小的就往最左边没搬过的位置搬
            if self.nums[j]<x:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                i += 1 # i记录下一次要搬的位置
        self.nums[i], self.nums[r] = self.nums[r], self.nums[i] # 此时i指着第一个大于等于x的数的位置
        return i
    
    def partition2(self, p, r): # i，j对向
        x = self.nums[p]
        i, j = p+1, r
        while True:
            while self.nums[i] < x:
                i += 1
                if i > r:
                    break
            while self.nums[j] > x:
                j -= 1
                if j < p+1:
                    break
            if i < j:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            else:
                self.nums[j], self.nums[p] = self.nums[p], self.nums[j]
                return j
    
    def select(self, p, r, i): # 找出第i小的
        if p == r:
            return self.nums[p]
        q = self.partition2(p, r) # 这里可以是partition1/partition2
        k = q - p + 1
        if i == k: # 选出来的q就是目标数字
            return self.nums[q]
        elif i < k:
            return self.select(p, q-1, i)
        else:
            return self.select(q+1, r, i-k)
    
    def findKthLargest(self): # 找到nums中第K大的数字
        n = len(self.nums)
        return self.select(0, n-1, n-self.k+1) # 第i大就是第n-i+1小
    
A = list(range(n))
random.shuffle(A)
start = time.time()
print(Selection(A,int(n/2)).findKthLargest())
print('Randomized seletion of {} numbers takes {} seconds'.format(n,time.time()-start))