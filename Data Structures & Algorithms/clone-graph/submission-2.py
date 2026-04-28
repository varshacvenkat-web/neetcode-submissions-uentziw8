"""
 Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==None:
            return None 
        hashmap={}
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            clone=Node(node.val) #is the value 
            hashmap[node]=clone # clone: clone.neighbors but currently that is empty 
            for i in node.neighbors:
                clone.neighbors.append(dfs(i))
            return clone 
        return dfs(node)
