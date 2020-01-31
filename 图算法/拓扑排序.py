'''
拓扑排序 
给定一个有向图，要求将图中的元素排序，使得排在后面的节点没有指向前面节点的边

Leetcode 210 课程表II

现在你总共有 n 门课需要选，记为 0 到 n-1。在选修某些课程之前需要一些先修课程。 
例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

'''

import collections

class Solution:
    def findOrder(self, numCourses, prerequisites):
        ''' 拓扑排序 '''
        # 先由边缘列表生成邻接表
        adjacency = dict()
        for i in range(numCourses):
            adjacency[i] = []
        for prerequisite in prerequisites:
            adjacency[prerequisite[1]].append(prerequisite[0])
        
        in_degrees = collections.defaultdict(int) # 每一个有先修课节点的入度
        for u in adjacency:
            for v in adjacency[u]:
                in_degrees[v] += 1
        
        queue = [u for u in adjacency if in_degrees[u] == 0] # 入度为0的节点
        stack = []
        while queue:
            course = queue.pop()
            stack.append(course)
            for v in adjacency[course]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    queue.append(v)

        # 如果能够选上所有课，那么in_degrees现在应该空了，stack长度为总课数
        return stack if len(stack) >= numCourses else []
    
solution = Solution()
print(solution.findOrder(7,[[1,0],[2,0],[3,1],[3,2]]))