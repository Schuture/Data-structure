""" 约瑟夫算法
据说著名犹太历史学家 Josephus 有过以下的故事：
在罗马人占领桥塔帕特后，39个犹太人与 Josephus 及他的朋友躲到一个洞中，
39个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，41个人排成一个圆圈，
由第1个人开始报数，每报数到第3人该人就必须自杀，然后再由下一个重新报数，
直到所有人都自杀身亡为止。然而 Josephus 和他的朋友并不想自杀，
问他俩安排的哪两个位置可以逃过这场死亡游戏？
"""
import collections
import functools
def Josephus1(a, b):                        # 使用队列的解法
    d = collections.deque(range(1, a+1))    # 将每个人依次编号，放入到队列中
    while d:
        d.rotate(-b)                        # 队列向左旋转b步
        print(d.pop(), end = ' ')           # 将最右边的删除，即自杀的人

def Josephus2(a, b):                        # 逐个计算的解法
    d = [i for i in range(1, a+1)]
    for i in range(a):
        if i == 0:
            cur = b % a - 1                 # 第一个自杀的人的索引
        else:
            cur = (cur - 1 + b) % a         # 计算当前自杀的人的索引
            
        print(d[cur], end = ' ')
        del d[cur]                          # 将自杀的人删除
        
        a -= 1
        
def Josephus3(a, b):                        # 递归解法
    d = [i for i in range(1, a+1)]
    @functools.lru_cache(999)
    def f(sum_, interval, n):               # 返回第n个自杀的人的索引
        if n == 1:
            return (sum_ + interval - 1) % sum_
        else:
            return (f(sum_ - 1, interval, n-1) + interval) % sum_
        
    for i in range(1, a+1):
        print(d[f(a, b, i)], end = ' ')

if __name__ == '__main__':
    
    # 输出的是自杀的顺序。最后两个是16和31，说明这两个位置可以保证他俩的安全。
    Josephus1(41,3)
    print('\n')
    Josephus2(41,3)
    print('\n')
    Josephus3(41,3)