'''字典树'''
class Trie():
    def __init__(self):
        self.root = {}
        
    def insert(self, x):
        p = self.root
        i = 0
        while i < len(x) - 1:
            if x[i] not in p.keys() and x[i] + '!' not in p.keys(): # 没有标识的边，就添加边
                p[x[i]] = {}
            if x[i] in p.keys(): # 有标识的边以后，沿着树枝往下走一个节点
                p = p[x[i]]
            elif x[i] + '!' in p.keys():
                p = p[x[i] + '!']
            i += 1
        p[x[i] + '!'] = {} # 加一个感叹号表示到了一个词的结尾
        print('单词{}插入成功'.format(x))
        
    def search(self, x):
        p = self.root
        for i in range(len(x)-1): # 走到倒数第二步，最后一个字符用于判断是否为终止节点
            if x[i] in p.keys():
                p = p[x[i]]
            elif x[i] + '!' in p.keys():
                p = p[x[i] + '!']
            else:
                print('没找到{}，不存在路径'.format(x))
                return False
        if x[-1] + '!' in p.keys(): # 倒数第二个节点的子节点有以最后一个字符结尾的
            print('找到了{}'.format(x))
            return True
        else:
            print('没找到{}，结尾处不为终止节点'.format(x))
            return False
        
    def startsWith(self, x: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for i in range(len(x)):
            if x[i] in p.keys():
                p = p[x[i]]
            elif x[i] + '!' in p.keys():
                p = p[x[i] + '!']
            else:
                print('没有以{}开头的字符'.format(x))
                return False
        print('找到了以{}开头的字符'.format(x))
        return True
        
trie = Trie()
words = ['ap','app','appl','apple','banana','orange','juice','cyx','ljx']
for word in words:
    trie.insert(word)
trie.search('app')
trie.search('apple')
trie.search('apply')
trie.search('banana')
trie.search('orange')
trie.search('juicc')
trie.search('cyx')
trie.search('ljx')
trie.search('gbiperpwegbiw')
trie.startsWith('ban')