# 用贪心算法求解活动选择问题
s = [0,1,3,0,5,3,5,6,8,8,2,12]      #首尾放0使活动下标从1开始
f = [0,4,5,6,7,9,9,10,11,12,14,16]  # 目的是让第一个活动前面也有一个界

# 递归贪心算法
def recursive_select(s,f,k,n): #返回s[k+1,n]范围内的最大兼容活动的集合，包括k+1,n
    m = None
    for i in range(k+1,n+1): # 找到第一个开始时间在上一个活动结束时间后的
        if s[i]>=f[k]:
            m = i
            break
    if m: #如果找到了第一个在活动k之后的活动
        # 此时第m个活动成为上一个活动，A为它之后能选的所有活动
        A = recursive_select(s,f,m,n) 
        A.add(str(m)) # 将这个活动作为第一个活动，与后面的活动合并
        return A
    else:
        return set()

n = len(s) - 1
# 打印递归贪心算法的选择结果
print(recursive_select(s,f,0,n))

# 迭代贪心算法
A = {'1'}
last = 1
for i in range(2,len(s)):
    if s[i]>=f[last]:
        A.add(str(i))
        last = i
# 打印迭代贪心算法的选择结果
print(A)