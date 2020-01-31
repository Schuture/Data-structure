''' Leetcode337. 打家劫舍III '''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root): # 返回一棵树最多得到的钱
        if not root:
            return [0,0]
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        
        # 第二层开始获得的最多的钱/根节点的钱加上第三层开始获得的最多的钱
        return [max(l) + max(r), root.val + l[0] + r[0]]
    
    def rob(self, root: TreeNode) -> int:
        '''对于每一个节点，都只有选和不选两种情况。我们每次考虑一棵子树，那么根只有两种情况，选和不选            (我们让dp[0]表示不选,dp[1]表示选)。
            对于选择了根,那么我们就不能选它的儿子了
            如果没有选根，我们就可以在它的子树中任意选了
            然后我们做一次dfs即可'''
        return max(self.dfs(root))
    
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

A = [3,2,3,None,3,None,1]
tree = buildTree(A)
solution = Solution()
print(solution.rob(tree))










