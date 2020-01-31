import random
import time

n = 100
m = 1000

def InsertionSort(A):
    for i in range(1,len(A)): # 从第二张牌开始排，假设0...i-1都排好序
        num = A[i]
        j = i - 1
        while j>=0 and A[j]>num:
            A[j+1] = A[j] # 把num的前面的更大的牌一张一张往后放
            j -= 1
        A[j+1] = num
    return A

A = list(range(20))
random.shuffle(A)
InsertionSort(A)
print(A)
start = time.time()
for i in range(n):
    A = list(range(m))
    random.shuffle(A)
    InsertionSort(A)
end = time.time()
print('InsertionSort consumes {} seconds to sort {} lists with length {}'.format(end-start,n,m),'\n',
      'average {} seconds'.format((end-start)/n))