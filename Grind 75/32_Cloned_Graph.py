python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: 
            return None

        new_to_old = {}

        return self.dfs(node, new_to_old)

    
    def dfs(self, node, new_to_old):
        if node in new_to_old: 
            return new_to_old[node]
        
        copy = Node(node.val)
        new_to_old[node] = copy

        for n in node.neighbors:
            copy.neighbors.append(self.dfs(n, new_to_old))
        
        return copy