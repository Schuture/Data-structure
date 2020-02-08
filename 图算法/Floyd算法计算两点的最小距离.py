# edges[i]表示[起点，终点，距离]，边是双向的
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
n = 5 # 地点数量


def initDistances(edges, n):
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
        
    return distances


def floyd(distances, n): 
    # 计算两两地点最短距离
    for k in range(n): # 将点k加入可以通过的点的集合中
        for i in range(n): # 遍历点对ij，更新其能够通过点k时，两者最小距离
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    
    return distances
                

def shortestPathFloyd(distances, n):
    # 计算两两地点最短距离以及两两的路径
    Paths = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if distances[i][j] < float('inf') and i != j: # 如果ij之间直接有路径相连
                Paths[i][j] = i # j的前驱为i
            else:
                Paths[i][j] = -1 # j的前驱为-1
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    Paths[i][j] = Paths[k][j] # 更改点j的前驱为k
                    
    return distances, Paths


def findPath(i, j, Paths):
    # 找到i,j两点间的最短路径
    print('\n从点{}到点{}的最短路径为：'.format(i, j), end = '')
    path = []
    while Paths[i][j] != -1:
        path.append(j)
        j = Paths[i][j] # 求前驱的前驱，一直循环直到到达i点
    path.append(i)
    path = path[::-1]
    print(path)
    
    return path


# 找到最短距离
distances = floyd(initDistances(edges, n), n)
for i in range(n):
    for j in range(n):
        print('点{}到点{}的最短距离为{}'.format(i, j, distances[i][j]))
        
        
# 找到最短路径
distances = initDistances(edges, n)
distances, Paths = shortestPathFloyd(distances, n)
path = findPath(3, 0, Paths)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        