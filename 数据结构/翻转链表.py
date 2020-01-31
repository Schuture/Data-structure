''' Leetcode25.K个一组翻转链表 '''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse1(self, head):  # 循环的方法反转链表
        if head is None or head.next is None:
            return head
        pre = None
        cur = head
        h = head
        while cur:
            h = cur
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return [h, head] # 翻转后的首尾
    
    def reverse2(self, head): # 递归翻转链表
        if not head.next:
            return head, head
        next = head.next
        head.next = None
        head_, tail_ = self.reverse2(next)
        tail_.next = head
        return head_, head # 翻转后尾巴节点是原来的头节点
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k == 1:
            return head
        
        n = 1 # 总节点数量
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        
        parts = [head]
        i = 1
        while head.next:
            if i % k == 0:
                next = head.next
                head.next = None
                parts.append(next)
                head = next
                i += 1
            else:
                head = head.next
                i += 1
                
        if n%k == 0: # 最后一个节点也要翻转
            parts[-1] = self.reverse2(parts[-1])
        else:
            parts[-1] = [parts[-1]]
        for i in range(len(parts)-1):
            parts[i] = self.reverse2(parts[i])
            
        head = parts[0][0]
        for i in range(len(parts)-1):
            parts[i][1].next = parts[i+1][0]
        
        return head

n = 10
head = ListNode(1)
p = head
for i in range(2, n+1):
    p.next = ListNode(i)
    p = p.next
solution = Solution()
new_head = solution.reverseKGroup(head, 5)

for i in range(n):
    print(str(new_head.val) + ' ', end = '')
    new_head = new_head.next
    
    
    
    
    
    
    
    