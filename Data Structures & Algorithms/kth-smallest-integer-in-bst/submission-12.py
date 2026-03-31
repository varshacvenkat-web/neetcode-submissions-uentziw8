# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter=[0]
        result=[None] 
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            counter[0]+=1
            if counter[0]==k:
                result[0]=root.val 
            inorder(root.right)
        inorder(root)
        return result[0] 