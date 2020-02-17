'''
二分查找，三种情况的算法
'''
def binSearch(nums, target): # 找到数组中任意一个target
    left, right = 0, len(nums) - 1 # 左右闭区间
    while left <= right: # 可以取等号是因为当两者相等的时候搜索区间仍不为空
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
            
    return -1 # 没找到

def binSearchLeft(nums, target): # 寻找左侧边界的二分查找
    left, right = 0, len(nums) # 左闭右开区间
    while left < right: # 当两者相等时搜索区间就为空了
        mid = (left + right) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
            
    if left == len(nums): # target大于所有值
        return -1
    return left if nums[left] == target else -1

def binSearchRight(nums, target): # 寻找右侧边界的二分查找
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
            
    if left == 0:
        return -1
    return left - 1 if nums[left-1] == target else -1

nums = [0,0,0,1,1,2,3,4,4,4,5,5,5,5,5,5,6,6,7,8,9,9,9,10,13]
target = 5
print(binSearch(nums, target))
print(binSearchLeft(nums, target))
print(binSearchRight(nums, target))