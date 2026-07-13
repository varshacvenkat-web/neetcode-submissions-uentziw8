# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best=float('-inf')
        def helper(root):
            nonlocal best
            if not root:
                return 0
            else:
                left_contribution=max(0, helper(root.left))
                right_contribution=max(0,helper(root.right))
                twosided=root.val+left_contribution+right_contribution
                best=max(best,twosided)
                return root.val+max(left_contribution,right_contribution)
        helper(root)
        return best 
        