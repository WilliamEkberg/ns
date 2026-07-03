# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Check left
        # Check right

        def valid(root, left_b, right_b):
            if not root:
                return True
            
            if not (root.val < right_b and root.val > left_b):
                return False
            
            return (valid(root.left, left_b, root.val) and valid(root.right, root.val, right_b))
        
        return valid(root, float("-inf"), float("inf"))



            


        