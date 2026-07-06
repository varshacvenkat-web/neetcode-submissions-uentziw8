# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSubtreehelper(root,subRoot)
    def check(self,root,subRoot):
        if not root and not subRoot:
            return True 
        if not root or not subRoot:
            return False
        x=self.check(root.left,subRoot.left)
        y=self.check(root.right,subRoot.right)
        return root.val==subRoot.val and x and y
    def isSubtreehelper(self,root,subRoot):
        if not root:
            return False 
        elif self.check(root,subRoot) or self.isSubtreehelper(root.left,subRoot) or self.isSubtreehelper(root.right,subRoot):
            return True 
        else:
            return False 
        

