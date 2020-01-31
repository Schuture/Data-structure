class Node(): # 单向链表节点
    def __init__(self):
         self.color = 'white'
         self.d = float('Inf') #与中心点的距离
         self.pi = None # 图中的父节点
         self.next = None # 只能赋值Node()
         
''' 循环队列，调用方式如下：
    Q = Queue()
    Q.enqueue(5) 往队尾加一个元素
    Q.dequeue() 删除队头元素'''
class Queue(): 
    def __init__(self):
        self.queue = [0 for i in range(100)] # 初始化100个队列空位
        self.head = 0
        self.tail = 0 # 所有元素后的第一个空位
        self.length = len(self.queue)
        self.full = False
        self.empty = True
    
    def enqueue(self,x):
        self.empty = False #只要调用这个函数，无论原来队列是否为空，都不再为空
        if self.full==True:
            print('Queue overflow!')
            return

        self.queue[self.tail] = x
        if self.tail==self.length-1:
            self.tail = 0 # 队列末尾被填满
        else:
            self.tail += 1
        
        if self.head==self.tail: # 放完这个元素后队列满了
            self.full = True
    
    def dequeue(self):
        self.full = False # 只要调用这个函数，无论原来队列是否为满，都不再为满
        if self.empty==True:
            print('Queue underflow!')
            return
        
        x = self.queue[self.head]
        if self.head==self.length-1:
            self.head = 0
        else:
            self.head += 1
        if self.head==self.tail: # 取出这个元素后队列空了
            self.empty = True
        
        return x
    
# 无向图中的节点
nodeR = Node()
nodeS = Node()
nodeT = Node()
nodeU = Node()
nodeV = Node()
nodeW = Node()
nodeX = Node()
nodeY = Node()
V = set((nodeR,nodeS,nodeT,nodeU,nodeV,nodeW,nodeX,nodeY)) #所有节点

# 边，表示节点能通向的隔壁节点
adjacentR = [nodeS,nodeV]
adjacentS = [nodeR,nodeW]
adjacentT = [nodeU,nodeW,nodeX]
adjacentU = [nodeT,nodeX,nodeY]
adjacentV = [nodeR]
adjacentW = [nodeS,nodeT,nodeX]
adjacentX = [nodeW,nodeT,nodeU,nodeY]
adjacentY = [nodeX,nodeU]
Adj = {nodeR:adjacentR, nodeS:adjacentS, nodeT:adjacentT, nodeU:adjacentU,
       nodeV:adjacentV, nodeW:adjacentW, nodeX:adjacentX, nodeY:adjacentY}

def BFS(s): # 从点s开始搜索
    for vertex in V-set([s]): # 搜索前先清空之前赋予的属性
        vertex.color = 'white'
        vertex.d = float('Inf')
        vertex.pi = None
    s.color = 'gray'
    s.d = 0
    s.pi = None
    Q = Queue()
    Q.enqueue(s)
    while Q.empty == False:
        u = Q.dequeue() #检查点u的邻点
        print(u.d)
        for v in Adj[u]:
            if v.color == 'white': # 只看仍然没有搜索到的点
                v.color = 'gray'
                v.d = u.d + 1
                v.pi = u
                Q.enqueue(v)
        u.color = 'black'
        
BFS(nodeS)

            
