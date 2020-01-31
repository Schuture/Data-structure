X = ['A','B','C','B','D','A','B']
Y = ['B','D','C','A','B','A']

def LCS_Length(X,Y):
    
    m,n = len(X),len(Y)
    # m+1行n+1列，b[i,j]存着X[i],Y[j]消去的是谁末尾的元素
    b = [[0 for i in range(n+1)] for j in range(m+1)] 
    # c[i][j]存着X[:i],Y[:j]的LCS的长度
    c = [[0 for i in range(n+1)] for j in range(m+1)] 
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]: # X,Y末尾元素可添加到LCS中
                c[i][j] = c[i-1][j-1] + 1 # LCS长度+1
                b[i][j] = 'left upper' # X,Y同时消去一个末尾元素
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j] = c[i-1][j] # c[i,j]等于它上面的元素
                b[i][j] = 'upper' # X消去一个末尾元素，它对LCS无贡献
            else:
                c[i][j] = c[i][j-1] # c[i,j]等于它左边的元素
                b[i][j] = 'left' # Y消去一个末尾元素，它对LCS无贡献
    return [b,c] # c[m,n]存着公共序列总长度，b[i,j]存着这一步消去的是谁的元素

def Print_LCS(b,X,i,j):
    if i==0 or j==0: # X或者Y被完全消除了
        return
    if b[i][j]=='left upper':
        Print_LCS(b,X,i-1,j-1)
        print(X[i-1])
    elif b[i][j]=='upper':
        Print_LCS(b,X,i-1,j)
    else:
        Print_LCS(b,X,i,j-1)
        
[b,c] = LCS_Length(X,Y)
Print_LCS(b,X,len(X),len(Y))