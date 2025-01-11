# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        if abs(left-right) > 1:
            self.balance = False
        return max(left,right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        self.traverse(root)
        return self.balance