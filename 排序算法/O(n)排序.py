import random
import time

n = 10
m = 10000

#计数排序
def CountSort(A):
    k = max(A) #假设A元素范围为[0,k]
    C = [0 for i in range(k+1)] #装每个数字出现的个数,从0到k
    B = [0 for i in range(len(A))] #返回的排好序的新数组
    for i in range(len(A)):
        C[A[i]] += 1 #统计A中每个数字出现的个数,例如C[5]放5的个数
    for i in range(1,k+1): #C[i]为小于等于i的元素个数
        C[i] += C[i-1]
    for i in range(len(A)-1,-1,-1):
        B[C[A[i]]-1] = A[i] #把A中的每个元素放在B中正确位置上，C[A[i]]为小于等于A[i]的元素个数
        C[A[i]] -= 1 #这两句按照A[i]中元素的顺序进行排序，保持相同元素相对位置不变
    return B

#桶排序
def BucketSort(A):
    ret = []
    n = len(A)
    maximum = max(A)
    minimum = min(A)
    B = [[] for i in range(n)] #有n个桶子用来放n个区间的数
    for num in A:
        B[(num-minimum)*(n-1)//(maximum-minimum)].append(num)
    for i in range(n):
        ret.extend(sorted(B[i]))
    return ret

#基数排序
def RadixSort(A):
    n = len(str(max(A)))
    for i in range(n): #分别取个，十，百...位
        bucket = [[] for i in range(10)] #桶子包含十个数组用来放该位0-9的数
        for j in range(len(A)):
            bucket[(A[j]%(10**(i+1)))//(10**i)].append(A[j])
        A = []
        for j in range(10):
            A.extend(bucket[j])
    return A

print(BucketSort([3,5,2,3,7,8,6,4,5,8,6,0,9,2,3,1,5,6,7,4,54,33,7,12,32,15,44,21,25,26,16]))
start = time.time()
for i in range(n):
    A = list(range(m))
    random.shuffle(A)
    sortedA = RadixSort(A)
end = time.time()
print('Consume {} seconds to sort {} lists with length {}'.format(end-start,n,m),'\n',
      'average {} seconds'.format((end-start)/n))