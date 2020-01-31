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