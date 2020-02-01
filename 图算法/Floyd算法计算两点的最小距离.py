# edges[i]表示[起点，终点，距离]，边是双向的
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
n = 5 # 地点数量

# 初始化距离矩阵
distances = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            distances[i][j] = 0
        else:
            distances[i][j] = float('inf')

# 读入边
for edge in edges:
    from_ = edge[0]
    to_ = edge[1]
    weight = edge[2]
    distances[from_][to_] = weight
    distances[to_][from_] = weight

# 计算最短距离
for k in range(n):
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][k] + distances[k][j]:
                distances[i][j] = distances[i][k] + distances[k][j]
                
# 输出最短距离
for i in range(n):
    for j in range(n):
        print('点{}到点{}的最短距离为{}'.format(i, j, distances[i][j]))