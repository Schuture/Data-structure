'''
从n个人中挑选出任意多个人组成一个队伍，并选出一个队长，问有多少种选择方式？
队伍成员不完全相同或队长不同都算是队伍不同。

输入：
一个数字n，0 < n < 1e9
输出：
一个数字，可能非常大，所以需要对1e9+7取模

示例：
输入：2
输出：4
'''
def pow(x, y): # 加速后的幂运算，O(logy)
    if y == 0:
        return 1
    if y == 1:
        return x
    if y % 2 == 0:
        return pow(x*x % 1000000009, y//2)
    else:
        return pow(x*x % 1000000009, (y-1)//2) * x

def selections1(n): # 对比组，验证自定义的pow是正确的，但是仅能通过80%测试用例
    return n * 2**(n-1) % 1000000009 # 先选出一个当队长，再剩下的随便选

def selections2(n): # 这种方法更快，能够通过所有测试用例
    return n * pow(2, n-1) % 1000000009 # 先选出一个当队长，再剩下的随便选

if __name__ == '__main__':
    n = int(input().strip())
    print(selections1(n)) # 当n太大时将这一行注释掉
    print(selections2(n))