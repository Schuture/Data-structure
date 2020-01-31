import time
import random

n = 1000
m = 1000

class TreeNode():
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.p = None # 父节点

class Binary_Search_Tree():
    
    def __init__(self, A): # 输入一个数组，构建二叉搜索树
        random.shuffle(A)
        self.length = len(A)
        self.root = TreeNode(A[0])
        for i in range(1,len(A)):
            self.insert(TreeNode(A[i]))
        
    def recursive_search(self, k, x): # 递归
        if not x: # 搜索完毕，未找到
            print('{} not found'.format(k))
            return
        elif x.key==k: # 搜索完毕，找到
            print('{} is found'.format(k))
            return x
        
        if k<x.key:
            return self.recursive_search(k, x.left)
        elif k>x.key:
            return self.recursive_search(k, x.right)
        
    def iterative_search(self, k): # 迭代，效率更高
        x = self.root
        while x:
            if k<x.key:
                x = x.left
            elif k>x.key:
                x = x.right
            else:
                print('{} is found'.format(k))
                return x
        
        print('{} not found'.format(k))
        return
    
    def search(self, k, mode='iterative'):
        if mode=='iterative':
            return self.iterative_search(k)
        elif mode=='recursive':
            return self.recursive_search(k, self.root)
        else:
            print('mode must be iterative or recursive')
            return
    
    def minimum(self, x):
        while x.left:
            x = x.left
        print('The minimum of the tree is {}'.format(x.key))
        return x
        
    def maximum(self, x):
        while x.right:
            x = x.right
        print('The maximum of the tree is {}'.format(x.key))
        return x
        
    def successor(self, x): #查找x的后继，即比x.key大的最小节点
        if x==self.maximum(self.root):
            print('This node is the largest')
            return
        if x.right:
            y = self.minimum(x.right)
            print('The successor of this node is {}'.format(y.key))
            return y
        # 没有右子树
        y = x.p
        while y: #如果x是y的左子节点，那y就是x的后继
            if x==y.right: # 这里仅仅判断x是y的右子节点
                x = y
                y = y.p
            else:
                break
        print('The successor of this node is {}'.format(y.key))
        return y
    
    def predecessor(self, x):
        if x==self.minimum(self.root):
            print('This node is the smallest')
            return
        if x.left:
            y = self.maximum(x.left)
            print('The predecessor of this node is {}'.format(y.key))
            return y
        y = x.p
        while y:
            if x==y.left:
                x = y
                y = y.p
            else:
                break
        print('The predecessor of this node is {}'.format(y.key))
        return y
        
    def insert(self, z):
        y = None
        x = self.root
        while x:
            y = x
            if z.key<x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if not y:
            self.root = z
        elif z.key<y.key:
            y.left = z
        else:
            y.right = z
        print('Insertion complete')
        
    def transplant(self, u, v): # 将v换到u的位置来
        if u.p is None:
            self.root = v
        elif u==u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v:
            v.p = u.p
    
    def delete(self, z):
        if z.left:
            self.transplant(z, z.right)
        elif z.right:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.p!=z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
        print('Deletion complete')

def inorder(root):
    if not root:
        return
    inorder(root.left)
    B.append(root.key)
    inorder(root.right)


A = list(range(20))
B = []
random.shuffle(A)
BST = Binary_Search_Tree(A)
inorder(BST.root)
print(B)

##################  不建议执行以下代码，因为会不断打印'插入成功'  #################
# 执行前删除第124行
start = time.time()
for i in range(n):
    A = list(range(m))
    B = []
    random.shuffle(A)
    BST = Binary_Search_Tree(A)
    inorder(BST.root)
end = time.time()
print('BST Sort consumes {} seconds to sort {} lists with length {}'.format(end-start,n,m),'\n',
      'Average {} seconds'.format((end-start)/n))


        
        
        
        
        
        
        
        
        
        