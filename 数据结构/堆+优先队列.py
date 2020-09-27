import random

class Heap(): # 最大堆
    def __init__(self, array):
        self.array = array
        self.heapsize = len(array) # 这里堆的插入功能尚未实现
        self.length = len(array) # 长度大于等于heapsize，有不使用的元素
        self.build()
        
    def parent(self, i):
        return (i + 1) // 2 - 1
    
    def left(self, i):
        return 2 * (i + 1) - 1
    
    def right(self, i):
        return 2 * (i + 1)
    
    def max_heapify(self, i): # 假设节点i的左右子树都是最大堆，使可能较小的i逐级下降，维持i以及其子树构成堆
        # 找出索引为i的节点与它的左右子节点哪个最大
        l = self.left(i)
        r = self.right(i)
        if l <= self.heapsize - 1 and self.array[l] > self.array[i]:
            largest = l
        else:
            largest = i
        if r <= self.heapsize - 1 and self.array[r] > self.array[largest]:
            largest = r
            
        if largest != i: # 若不是根节点最大，就将最大值移到根处，小值移到largest处
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.max_heapify(largest) # 现在largest处是小值，将其继续下沉
            
    def min_heapify(self, i): # 维持最小堆性质，根节点必定比子节点小
        l = self.left(i)
        r = self.right(i)
        if l <= self.heapsize - 1 and self.array[l] < self.array[i]:
            smallest = l
        else:
            smallest = i
        if r <= self.heapsize - 1 and self.array[r] < self.array[smallest]:
            smallest = r
            
        if smallest != i: # 若不是根节点最小，就将最小值移到根处，大值移到smallest处
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self.min_heapify(smallest) # 现在smallest处是大值，将其继续下沉
            
    def build(self, max=True):
        self.heapsize = self.length
        # 从树的底部逐渐往上构建，保证每次调用的时候i左右子树都是堆
        if max == True: # 最大堆
            for i in range(self.length//2-1,-1,-1): 
                self.max_heapify(i)
        else: # 最小堆
            for i in range(self.length//2-1,-1,-1): 
                self.min_heapify(i)
            
    def heap_sort(self): #从小到大排序
        self.build()
        for i in range(self.length-1,0,-1):
            self.array[i], self.array[0] = self.array[0], self.array[i] # 首节点不断与最小节点交换
            self.heapsize -= 1 # 将最后节点移出堆
            self.max_heapify(0) # 维护最大堆
            
A = list(range(10))
random.shuffle(A)
Heap(A).heap_sort()
print(A)

# 优先队列用于维护由一组元素构成的集合
# 有四种功能：（以下函数的输入A都是堆）
def heap_maximum(A): # 1 返回具有最大关键字的元素
    return A.array[0]

def heap_extract_max(A): # 2 去掉并返回A中具有最大关键字的元素
    if A.heapsize<1:
        print('heap underflow')
        return
    #把最大值提取出来，用最后一个值填上
    maximum = A.array[0]
    A.array[0] = A.array[A.heapsize-1] 
    del A.array[A.heapsize-1] 
    A.heapsize -= 1
    A.length -= 1
    #将最大值移到根节点处
    A.max_heapify(0) 
    return maximum

def heap_increase_key(A, i, key): # 3 将元素A[i]的值增加到key
    if key < A.array[i]:
        print('new key is smaller than the current key')
    A.array[i] = key
    while i > 0 and A.array[A.parent(i)] < A.array[i]: # 赋更大值后要把原来的第i个元素移到应该在的位置
        A.array[A.parent(i)], A.array[i] = A.array[i], A.array[A.parent(i)] # 不停往上移
        i = A.parent(i)
    
def max_heap_insert(A, key): # 4 把元素x插入到集合A中
    A.length += 1
    A.heapsize += 1
    A.array.append(-float('inf')) # 扩展最大堆
    heap_increase_key(A,A.heapsize-1,key) # 将最小元素赋值为key
    
a = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
A = Heap(a)
print(heap_maximum(A))
print(heap_extract_max(A))
print(heap_increase_key(A, 6, 999))
max_heap_insert(A, 4)
max_heap_insert(A, 44)
max_heap_insert(A, 444)
max_heap_insert(A, 4444)
max_heap_insert(A, 5)
max_heap_insert(A, 55)
max_heap_insert(A, 555)
max_heap_insert(A, 5555)
max_heap_insert(A, 6)
max_heap_insert(A, 66)
max_heap_insert(A, 666)
max_heap_insert(A, 6666)
print(heap_maximum(A))
print(heap_extract_max(A))
print(heap_increase_key(A, 6, 999))