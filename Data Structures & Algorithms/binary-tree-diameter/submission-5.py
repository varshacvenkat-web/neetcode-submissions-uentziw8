# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_diameter=0
        self.height(root)  #start recursion at root 
        return self.max_diameter
    def height(self,root):
        if not root:
            return 0
        left_height=self.height(root.left) #depth through left root 
        right_height=self.height(root.right) #depth through right root
        diameter=left_height+right_height #calculate total through both-Diameter
        self.max_diameter=max(diameter,self.max_diameter) #find max diameter
        height=1+max(left_height,right_height)
        return height
    
    