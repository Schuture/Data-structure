import random
import time

n = 1000
m = 1000

#堆排序,父节点下标为parent，那么左孩子下标2*parent+1，右孩子2*parent+2
#子节点下标child，那么父节点下标child-1//2
class Heap(): #最大堆
    def __init__(self,array):
        self.array = array
        self.length = len(array)
        
    def build(self):
        for i in range((self.length-2)//2,-1,-1):
            self.downadjust(i)
    
    def upadjust(self): #最后一个子节点上浮,最大堆大节点上浮
        child = self.length-1
        parent = (child-1)//2
        temp = self.array[child]
        while child>0 and temp>self.array[parent]:
            self.array[child] = self.array[parent]
            child = parent
            parent = (parent-1)//2
        self.array[child] = temp
        
    def downadjust(self,parent,length): #将parent小节点下沉
        temp = self.array[parent]
        child = 2*parent+1
        while child<length:
            if child+1<length and self.array[child+1]>self.array[child]:
                child += 1 #child索引定位到较大的子节点
            if temp >= self.array[child]:
                break
            self.array[parent] = self.array[child]
            parent = child
            child = 2*child+1
        self.array[parent] = temp
        
    def heapsort(self):
        for i in range(self.length//2,-1,-1):
            self.downadjust(i,self.length-1)
        for i in range(self.length-1,0,-1):
            self.array[i],self.array[0] = self.array[0],self.array[i]
            
            self.downadjust(0,i)

A = list(range(20))
random.shuffle(A)
Heap(A).heapsort() 
print(A)
start = time.time()
for i in range(n):
    A = list(range(m))
    random.shuffle(A)
    Heap(A).heapsort()  
end = time.time()
print('HeapSort consumes {} seconds to sort {} lists with length {}'.format(end-start,n,m),'\n',
      'average {} seconds'.format((end-start)/n))