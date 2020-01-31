# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertsort(self, head, node): # head是已经排好序的链表头，node是要插入的节点，返回插入后的链表
        if node.val <= head.val: # 如果node的值小于等于链表中所有值，就排在开头
            node.next = head
            return node
        
        cache = head # 链表的指针
        while cache.next: 
            # 直到找到cache.val<node.val并且cache.next.val>node.val,或者链表到头了
            if cache.next.val < node.val:
                cache = cache.next
            else:
                break
        node.next = cache.next
        cache.next = node
        return head
    
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        sorted_ = ListNode(head.val)
        while head.next:
            # 这里要把下一个节点单独提取出来，不然会有死循环
            sorted_ = self.insertsort(sorted_, ListNode(head.next.val))
            head = head.next
        return sorted_