'''
剑指offer 第11题
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

数组中可以有重复元素  
'''

def minArray(numbers):
    ''' 二分查找 '''
    if not numbers:
        return 0
    n = len(numbers)
    left, right = 0, n-1
    if numbers[left] < numbers[right]: # 没有旋转的情况
        return numbers[left]
    
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] < numbers[right]: # 此时最小值在mid左边
            right = mid
        elif numbers[mid] > numbers[right]: # 此时最小值在mid右边
            left = mid + 1
        elif numbers[mid] == numbers[right]: # 例如[2,3,4,1,1,1,1,1]。如果无重复元素，这个分支可舍去
            right -= 1
    
    return numbers[right] # left=right，不可以取numbers[mid]因为最后一次mid来不及更新

print(minArray([3]))                    # 输出3
print(minArray([3,1]))                  # 输出1
print(minArray([3,4,5,1,2]))            # 输出1
print(minArray([2,2,2,0,1]))            # 输出0
print(minArray([2,3,4,2,2,2,2,2,2]))    # 输出2