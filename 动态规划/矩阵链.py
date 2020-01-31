'''如果A,B分别为p*q, q*r，那么计算C=AB的时间复杂度为pqr'''
def matrix_multiply(A,B): #两个矩阵相乘，AB
    if len(A[0])!=len(B):
        print('Matrix dimension error!')
        raise SystemExit()
    else:
        p = len(A)
        q = len(B)
        r = len(B[0])
        C = [[0 for i in range(p)] for j in range(r)]
        for i in range(p):
            for j in range(r):
                C[i][j] = sum([A[i][k] * B[k][j] for k in range(q)]) # A的第i行，B的第j列
    return C

# 矩阵链乘法问题是求矩阵链如何加括号能够使得总计算量最低
# 令m[i,j]表示第i与第j矩阵之间的链的最少计算量，那么m[1,n]
# 只有O(n^2)个不同的子问题，即m[i,j]，1<=i<j<=n
def max_chain_order(p): #输入矩阵链的维度,有n+1元素
    n = len(p) - 1
    m = [[0 for i in range(n+1)] for j in range(n+1)] # 1..n, 1..n
    s = [[0 for i in range(n+1)] for j in range(n)] # 1..n-1, 2..n
    for l in range(2,n+1): # l是链长度,迭代从链短到长
        for i in range(1,n-l+2): # 遍历所有可能的起始点i，下面讨论m[i,j]的最优括号化
            j = i + l - 1
            m[i][j] = 2**63
            for k in range(i,j): # 矩阵链起止维度为q[i-1],q[j],分割点范围[i,j-1]
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] #分割点k的计算量
                if q < m[i][j]: # 如果当前划分点k更好那么就取这个点的计算量
                    m[i][j] = q
                    s[i][j] = k
    return [m,s] # s[i][j]记录了m[i,j]的最优括号化分割点k

def print_optimal_parens(s,i,j):
    if i==j:
        print('A{}'.format(i), end="")
    else: # 如果矩阵链有多于一个矩阵，那么就打印这个链的最优括号化
        print('(', end="")
        print_optimal_parens(s,i,s[i][j])   # m[i,s[i][j]]，最优分割点左侧
        print_optimal_parens(s,s[i][j]+1,j) # m[s[i][j]+1,j]，右侧
        print(')', end="")
        
p = [30,35,15,5,10,20,25,50,15,20,25,40,15,100,10,50,5,10,10,5,5,15]
[m,s] = max_chain_order(p)
print_optimal_parens(s,1,len(p)-1)