class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(A):
    '''
    A: a list with values of the tree
    return the root of tree
    '''
    val = A.pop(0)
    root = TreeNode(val)
    queue = [root]
    while A:
        leftval = A.pop(0)
        if not leftval:
            left = None
        else:
            left = TreeNode(leftval)
        if len(A) > 0:
            rightval = A.pop(0)
            if not rightval:
                right = None
            else:
                right = TreeNode(rightval)
        
        node = queue.pop(0)
        while not node:
            node = queue.pop(0)
        node.left = left
        node.right = right
        queue.append(left)
        queue.append(right)
    return root

def preorderRecursion(root):
    if not root:
        return
    print(root.val, end = ' ')
    preorderRecursion(root.left)
    preorderRecursion(root.right)
    
def inorderRecursion(root):
    if not root:
        return
    inorderRecursion(root.left)
    print(root.val, end = ' ')
    inorderRecursion(root.right)
    
def postorderRecursion(root):
    if not root:
        return
    postorderRecursion(root.left)
    postorderRecursion(root.right)
    print(root.val, end = ' ')
    
def preorderIteration(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end = ' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def inorderIteration(root):
    if not root:
        return
    stack = []
    node = root
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val, end = ' ')
            node = node.right

def postorderIteration(root):
    if not root:
        return
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node.val)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    for i in range(len(stack2)-1, -1, -1):
        print(stack2[i], end = ' ')
        

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
tree = buildTree(A)
print('preorder recursion:')
preorderRecursion(tree)
print('\ninorder recursion:')
inorderRecursion(tree)
print('\npostorder recursion:')
postorderRecursion(tree)
print('\npreorder iteration:')
preorderIteration(tree)
print('\ninorder iteration:')
inorderIteration(tree)
print('\npostorder iteration:')
postorderIteration(tree)








