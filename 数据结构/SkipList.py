# coding=utf-8
# 跳表的Python实现

import random

# 最高层数设置为4
MAX_LEVEL = 4


def randomLevel():
    """
    返回随机层数 如果大于最大层数则返回最大层数
    :return: random level
    """
    k = 1
    while random.randint(1, 100) % 2:
        k += 1
    k = k if k < MAX_LEVEL else MAX_LEVEL
    return k


def traversal(skiplist):
    """
    跳表的遍历功能
    对每一层的元素都进行遍历
    :param skiplist: 待遍历的跳表
    :return: None
    """
    level = skiplist.level
    i = level - 1
    while i >= 0:
        level_str = 'header'
        header = skiplist.header
        while header:
            level_str += ' -> %s' % header.key
            header = header.forward[i]
        print(level_str)
        i -= 1
    print('\n')


class Node(object):
    def __init__(self, level, key, value):
        """
        跳表节点初始化
        :param level: 这个节点在小于等于level的层数都出现了
        :param key: 查询关键字
        :param value: 存储的信息
        """
        self.key = key                  # 节点值
        self.value = value              # 这个节点的内容（各种各样）
        self.forward = [None] * level   # 0 ~ level-1层的指针指着这层下一个节点


class Skiplist(object):
    def __init__(self):
        """
        跳表初始化 层数为0 初始化头部节点()
        """
        self.level = 0
        self.header = Node(MAX_LEVEL, 0, 0)

    def insert(self, key, value):
        """
        跳表插入操作
        :param key: 节点索引值
        :param value: 节点内容
        :return: Boolean 用于判断插入成功或失败
        """
        # 更新的最大层数为 MAX_LEVEL 层，update记录每一层的上一个节点
        update = [None] * MAX_LEVEL
        p = self.header
        q = None
        k = self.level
        i = k - 1
        # i from k-1 to 0，记录每一层左边节点都是什么
        while i >= 0:
            q = p.forward[i]
            while q and q.key < key:
                p = q
                q = p.forward[i]
            update[i] = p
            i -= 1
            
        # 保证key的唯一性，如果想要不唯一，删掉这两行即可
        if q and q.key == key: 
            return False
        
        # 这个节点的level
        k = randomLevel()
        if k > self.level:
            i = self.level
            while i < k: # 大于k小于maxlevel的层直接与header相连
                update[i] = self.header
                i += 1
            self.level = k

        q = Node(k, key, value) # 创建新节点
        i = 0
        while i < k: 
            # 这个节点小于k的层与这一层中下一个节点相连
            q.forward[i] = update[i].forward[i]
            # 每一层的上一个节点与新节点相连
            update[i].forward[i] = q
            i += 1

        return True

    def delete(self, key):
        """
        跳表删除操作
        :param key: 查找的关键字
        :return: Boolean 用于判断删除成功或失败
        """
        update = [None] * MAX_LEVEL
        p = self.header
        q = None
        k = self.level
        i = k - 1
        # 跟插入一样 找到要删除的位置
        while i >= 0:
            q = p.forward[i]
            while q and q.key < key:
                p = q
                q = p.forward[i]
            update[i] = p
            i -= 1
        if q and q.key == key:
            i = 0
            while i < self.level:
                if update[i].forward[i] == q:
                    update[i].forward[i] = q.forward[i]
                i += 1
            del q
            i = self.level - 1
            while i >= 0:
                if not self.header.forward[i]:
                    self.level -= 1
                i -= 1
            return True
        else:
            return False

    def search(self, key):
        """
        跳表搜索操作
        :param key: 查找的关键字（节点值）
        :return: 节点的 key & value & 节点所在的层数(最高的层数)
        """
        i = self.level - 1
        while i >= 0: # 一层一层往下层找
            q = self.header.forward[i]
            # 这层这个节点值小于等于key，但是下个节点大于key
            while q and q.key <= key:
                if q.key == key:
                    return q.key, q.value, i # 返回节点值，节点内容，第i层找到的
                q = q.forward[i] # 第i层下一个节点
            i -= 1
        return None


def main():
    number_list = list(range(1,11))
    skiplist = Skiplist()
    for number in number_list:
        skiplist.insert(number, None)

    print('Original skiplist:')
    traversal(skiplist)
    print('Search node 4: index, content, level are: ', end = '')
    print(skiplist.search(4), '\n')
    skiplist.delete(4)
    print('4 has been deleted \n')
    print('Skiplist now:')
    traversal(skiplist)

if __name__ == '__main__':
    main()