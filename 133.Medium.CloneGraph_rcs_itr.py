# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
    # itr
    # 88ms
        if not node:
            return
        root = UndirectedGraphNode(node.label)
        visited = {}
        visited[node.label] = root
        stack = [node]
        while stack:
            oriNode = stack.pop(0) # same result as stack.pop()
            cloneNode = visited[oriNode.label]
            for n in oriNode.neighbors:
                if n.label not in visited:
                    stack.append(n)
                    visited[n.label] = UndirectedGraphNode(n.label)
                cloneNode.neighbors.append(visited[n.label])
        return root



    
    # rcs
    # 104ms
        if not node:
            return
        root = UndirectedGraphNode(node.label)
        self.visited[node.label] = root
        for n in node.neighbors:
            if n.label in self.visited:
                root.neighbors.append(self.visited[n.label])
            else:
                root.neighbors.append(self.cloneGraph(n))
        return root
    def __init__(self):
        self.visited = {}



# https://leetcode.com/discuss/45217/4-7-lines-python-7-lines-c-java
    # rcs
    # logic symplified
    # 112ms
        memo = {}
        def clone(node):
            if node not in memo:
                cloneNode = memo[node] = UndirectedGraphNode(node.label)
                cloneNode.neighbors = map(clone, node.neighbors)
            return memo[node]
        return node and clone(node)

    # rcs
    # bad