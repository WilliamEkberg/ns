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

        def valid(r, left, right):
            if not r:
                return True

            if not (left < r.val < right):
                return False

            return (valid(r.left, left, r.val) and valid(r.right, r.val, right))

        return valid(root, float("-inf"), float("inf"))





            


        