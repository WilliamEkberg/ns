# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Save roots as the last level
        if not root:
            return []
        roots = [[root]]
        vals = [[root.val]]

        def get_level(r):
            roots2 = []
            vals2 = []
            for i in r:
                if i.left:
                    roots2.append(i.left)
                    vals2.append(i.left.val)
                if i.right:
                    roots2.append(i.right)
                    vals2.append(i.right.val)
            return roots2, vals2

        while len(roots[-1]) != 0:
            roots2, vals2 = get_level(roots[-1])
            if roots2:
                roots.append(roots2)
                vals.append(vals2)
            else:
                break
        return vals
    


            