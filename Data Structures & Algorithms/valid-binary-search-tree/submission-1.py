# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node,low,high):
            if not node:
                return True  
            elif low<node.val<high:
                return True and helper(node.left,low=low,high=node.val)and helper(node.right,low=node.val,high=high)
            else:
                return False 
        return helper(root,float('-inf'),float('inf'))



    



        