import time

p = [0,1,5,8,9,10,17,17,20,24,30,33,34,36,40,43,47,49,55,60,62,80,82,83,83,
     83,83,83,83,85,88,88,88,100,101,120,122,125,128,130,130]
n = 25 #超过25则第一个算法运行时间比较长

################### 2的指数时间复杂度方法#####################
def cut(p,n): #输入长度-价值关系以及钢条长度，返回钢条最大价值
    if n==0:
        return 0
    q = -1
    for i in range(1,n+1): #不能range(n)，这样会使递归树无限重复
        q = max(q,p[i]+cut(p,n-i)) 
    return q

##################### 多项式时间复杂度方法 #####################
# 自顶向下
def memorized_cut(p,n):
    r = [-1] * n # r中存长度i的钢条最多的价值
    return memorized_cut_aux(p,n,r)

def memorized_cut_aux(p,n,r):
    if r[n-1]>=0:   #检查q是否已知，若未知则用普通方法计算q
        return r[n-1]
    if n==0:
        q = 0
    else:
        q = -1
        for i in range(1,n+1):
            q = max(q,p[i]+memorized_cut_aux(p,n-i,r))
    r[n-1] = q
    return q

# 自底向上
def bottom_up_cut(p,n):
    r = [0] * (n+1)
    s = [0] * (n+1)
    for i in range(1,n+1):
        q = -1
        for j in range(1,i+1): #得到长度为i的钢条的最大价值，并将此时长度存起来
            if q<p[j]+r[i-j]:
                q = p[j]+r[i-j] 
                s[i] = j
        r[i] = q
    return [r[n],s]

def print_cut_solution(p,n):
    [r,s] = bottom_up_cut(p,n)
    while n>0:
        print(s[n])
        n = n-s[n]

###########################测试时间消耗##############################
begin = time.time()
print('长度为{}的钢条最大价值为'.format(n),cut(p,n))
end = time.time()
print('普通递归法消耗时间为{}s\n'.format(end-begin))

begin = time.time()
print('长度为{}的钢条最大价值为'.format(n),memorized_cut(p,n))
end = time.time()
print('由顶至下动态规划法消耗时间为{}s\n'.format(end-begin))

begin = time.time()
print('长度为{}的钢条最大价值为'.format(n),bottom_up_cut(p,n)[0])
end = time.time()
print('钢条应该切割成：')
print_cut_solution(p,n)
print('由底至上动态规划法消耗时间为{}s\n'.format(end-begin))




















