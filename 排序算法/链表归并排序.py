import time
import random

n = 10
m = 10000

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedListSort():
    def merge(self, A, B): # 给两段排好序的链表，将其合并
        if A.val < B.val:
            head = A
            A = A.next
        else:
            head = B
            B = B.next
        cache = head # 用来保存头节点的指针
        while A and B: # A, B都没到尾巴
            if A.val < B.val:
                head.next = A
                head = head.next
                A = A.next
            else:
                head.next = B
                head = head.next
                B = B.next
        if A: # B过了尾巴，A没过
            head.next = A
        else:
            head.next = B

        return cache
    
    def mergesort(self, head):
        if not head:
            return
        if not head.next: # 如果输入的链表长度为1，只有头节点，就不用排序直接输出
            return head
        
        i = 0 # 链表长度
        cache = head # 保存头节点的指针
        while head:
            i += 1
            head = head.next
        linkedlist1 = cache # 整个链表的头节点赋给链表1
        for i in range(int(i/2)-1):
            cache = cache.next
        linkedlist2 = cache.next # 链表的中间节点赋值给链表2
        cache.next = None # 切断链表1，2，把链表等分成两份
        
        linkedlist1 = self.mergesort(linkedlist1)
        linkedlist2 = self.mergesort(linkedlist2)
        mergedhead = self.merge(linkedlist1, linkedlist2)
        return mergedhead
    
start = time.time()
for i in range(n):
    A = list(range(m))
    random.shuffle(A)
    head = ListNode(A[0])
    cache = head
    for i in range(1,m):
        head.next = ListNode(A[i])
        head = head.next
    sorted_linked_list = LinkedListSort().mergesort(cache)
end = time.time()
print('MergeSort of linked list consumes {} seconds to sort {} lists with length {}'.format(end-start,n,m),'\n',
      'Average {} seconds'.format((end-start)/n))










