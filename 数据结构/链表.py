class Node(): # 双向链表节点
    def __init__(self, x):
         self.key = x
         self.prev = None # 只能赋值ListNode()
         self.next = None # 只能赋值ListNode()
         
    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出key
        '''
        return str(self.key)
    
class LinkedList():
    def __init__(self, x):
        if isinstance(x, Node):
            self.head = x # 一定是Node数据, x有.prev, .next属性
        else:
            print('You must input a Node')
        self.length = 1
        
    def isempty(self):
        if not self.head:
            return True
        return False
    
    def append(self, x): # 头节点前增加一个节点
        if not isinstance(x, Node):
            print('You must input a Node')
            return
        
        x.next = self.head # x.prev默认为 None
        if self.head:
            self.head.prev = x
        self.head = x
        
        print('We have added a node at the front with value {}'.format(x.key))
        self.length += 1
            
    def delete(self, x): # 删除 Node x
        if not isinstance(x, Node):
            print('You must input a Node')
            return
            
        if self.isempty():
            print("Linked list is already empty")
            return

        # 当前节点不是头节点，这里x.next可能是None
        if x.prev:
            x.prev.next = x.next
        # 删除头节点的情况
        else:
            self.head = x.next

        # 当前节点不是尾节点
        if x.next:
            x.next.prev = x.prev
        
        print('We have deleted the node with value {}'.format(x.key))
        self.length -= 1
            
    def search(self, k): # 查询值为k的node并打印索引
        if self.isempty():
            print("Linked list is empty, we can't find anything")
            return

        node = self.head
        i = 1 # 索引
        while True:
            if not node:
                print('There is not such a node')
                break
            if node.key!=k:
                node = node.next
                i += 1
            else:
                print('Node with value {} is found'.format(k))
                break
            
        print('The index of the node is {}'.format(i))
        return node
    
    def clear(self): # 清空链表
        self.head = None
            
L = LinkedList(Node(5))
L.isempty()
L.search(5)
L.append(Node(4))
L.append(Node(3))
L.append(Node(2))
L.append(Node(1))
L.delete(L.search(3))
            
            
# 用三个数组表示一个链表, prev[i],val[i],next[i]存储了一个node的所有信息
Head = 6 # 预先说明头节点的index
prev = [0 for i in range(8)] # 节点i前一个节点的index
key = [0 for i in range(8)] # 节点i的值
next = [0 for i in range(8)] # 节点i后一个节点的index
            
# 用一个数组表示一个链表，连续的三个值中cache[i]表示值，cache[i+1]为next，cache[i+2]为prev
Head = 19 # 预先说明头节点的index
cache = [0 for i in range(50)]
            
            
            
            
            
            
            
            
            