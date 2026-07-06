# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p,q)
    def check(self,p:[TreeNode],q:[TreeNode]):
        if not p and not q:
            return True 
        if not p or not q:
            return False 
        result=self.check(p.left,q.left)
        result2=self.check(p.right,q.right)
        return p.val==q.val and result and result2
        