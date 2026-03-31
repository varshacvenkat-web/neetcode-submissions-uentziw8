# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        leftinorder=inorder[:mid]
        rightinorder=inorder[mid+1:]
        leftpreorder=preorder[1:mid+1]
        rightpreorder=preorder[mid+1:]
        root.left=self.buildTree(leftpreorder,leftinorder)
        root.right=self.buildTree(rightpreorder,rightinorder)
        return root 

        
        