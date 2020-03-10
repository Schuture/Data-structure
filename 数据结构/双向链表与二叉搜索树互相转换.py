class TreeNode:
    '''
    树节点的定义
    '''
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    '''
    双向链表节点的定义
    '''
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None


def buildList(nums): # 由数组构建双向链表
    nums.sort()
    head = ListNode(nums[0])
    node = head
    for i in range(1, len(nums)):
        next_ = ListNode(nums[i])
        node.next = next_
        next_.prev = node
        node = node.next
    tail = node # 此时Node为最后一个节点了
    
    return head, tail


def inorder(head): # 中序遍历并打印二叉搜索树的节点值
    if not head:
        return
    inorder(head.left)
    print(head.val, end = ' ')
    inorder(head.right)

def traverse(nodes): # 遍历并打印一个双向链表的节点值
    if not nodes:
        return
    head = nodes[0]
    while head:
        print(head.val, end = ' ')
        head = head.next

class ConvertLinkedList:
    '''
    将双向链表转化为二叉搜索树，初始化应输入两个链表节点（首，尾）
    得到二叉搜索树则调用toBST函数即可
    '''
    def __init__(self, nodes):
        if isinstance(nodes[0], ListNode): # 如果是双向链表那么就统计出长度
            self.n = 1
            x = nodes[0]
            while x.next:
                self.n += 1
                x = x.next
                
            self.head, self.tail = nodes
        else:
            raise ValueError('应该输入两个链表节点')
            
    def toBST(self): # 从双向链表转换为二叉搜索树，返回根节点
        return self.BST(self.head, self.tail, self.n)
        
    def BST(self, head, tail, n):
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(head.val)
        elif n == 2:
            root = TreeNode(head.val)
            root.right = TreeNode(tail.val)
            return root
        elif n == 3:
            root = TreeNode(head.next.val)
            root.left = TreeNode(head.val)
            root.right = TreeNode(tail.val)
            return root
        
        mid = n // 2
        left_n = n // 2 # 左子树节点数量
        right_n = n - 1 - left_n # 右子树节点数量
        
        mid_node = head 
        for i in range(mid): # 找到链表中间节点
            mid_node = mid_node.next
            
        # 找到左边的尾节点，并断开连接
        left_tail = mid_node.prev
        left_tail.next = None
        mid_node.prev = None
        # 找到右边的尾节点，并断开连接
        right_head = mid_node.next
        right_head.prev = None
        mid_node.next= None
        
        root = TreeNode(mid_node.val)
        root.left = self.BST(head, left_tail, left_n)
        root.right = self.BST(right_head, tail, right_n)
        
        return root
        
        
class ConvertBST:
    '''
    将二叉搜索树转化为有序双向链表，初始化时输入一个树节点（根）
    '''
    def __init__(self, root):
        self.root = root
        
    def toLinkedList(self):
        return self.LinkedList(self.root)
        
    def LinkedList(self, root):
        if not root:
            return (None, None)
        
        cur_node = ListNode(root.val) # 根节点变为中间节点
        if root.left: # 如果根节点有左子节点，则将左边的链表拼接
            left_head, left_tail = self.LinkedList(root.left)
            left_tail.next = cur_node
            cur_node.prev = left_tail
        else: # 如果根节点没有左子节点，则这个中间节点就是最左边的头节点
            left_head = cur_node
            
        if root.right: # 如果根节点有右子节点，则将右边的链表拼接
            right_head, right_tail = self.LinkedList(root.right)
            right_head.prev = cur_node
            cur_node.next = right_head
        else: # 如果根节点没有右子节点，则这个中间节点就是最右边的尾节点
            right_tail = cur_node

        return left_head, right_tail
        
        
if __name__ == '__main__':
    head, tail = buildList([4,3,5,2,6,7,9,1,8,0]) # 构建有序双向链表
    nodes = (head, tail)
    root = ConvertLinkedList(nodes).toBST() # 将有序双向链表转化为二叉搜索树
    print('The inorder traversal of BST is:')
    inorder(root) # 中序遍历，检验二叉搜索树是否正确
    
    head, tail = ConvertBST(root).toLinkedList() # 将刚才的二叉搜索树转化为有序链表
    nodes = (head, tail)
    print('\nThe traversal of double linked list is:')
    traverse(nodes) # 遍历链表，检验是否正确
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        