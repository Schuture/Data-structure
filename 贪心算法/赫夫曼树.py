class TreeNode():
    def __init__(self, x, letter=None):
        self.key = x            #赫夫曼树这个节点以下的总频数
        self.freq = x           #这个字符出现的频数
        self.letter = letter    # 节点中存储的字母
        self.left = None
        self.right = None
        
def extract_min(Q): #从一个TreeNode集合中取出key最小那个
    ret = TreeNode(2**31)
    for i in range(len(Q)):
        if Q[i].key < ret.key:
            ret = Q[i] #取key最小的TreeNode
    Q.remove(ret)
    return ret

def insert(Q, z): #将节点z插入集合Q中
    Q.append(z)

def huffman(Q):
    n = len(Q)
    for i in range(1,n): #反复提取两个频率最低的节点，将他们合成一个新的节点z替代他们
        z = TreeNode(0)
        z.left = extract_min(Q)
        z.right = extract_min(Q)
        z.key = z.left.key + z.right.key
        insert(Q,z)
    return extract_min(Q) #返回集合中剩下的唯一节点，根节点

class Code_length():
    
    def __init__(self, root):
        self.root = root
        self.length = 0
        
    def find_code_length(self, root, depth): #找到赫夫曼树编码后的总字符长度
        if not root:
            return 0
        if root.letter: #存了字母
            self.length += depth * root.freq
        self.find_code_length(root.left, depth+1)
        self.find_code_length(root.right, depth+1)
        
    def find(self):
        self.find_code_length(self.root, 0) #与普通树不同的是，根节点不放字符所以深度为0
        return self.length
        
# 初始化词频，放在树节点中
Q = [TreeNode(5,'f'), TreeNode(9,'e'), TreeNode(12,'c'), TreeNode(13,'b'),\
     TreeNode(16,'d'), TreeNode(45,'a')]

# 编码
huffman_tree_root = huffman(Q)

# 打印Huffman树总编码长度
print(Code_length(huffman_tree_root).find())




















