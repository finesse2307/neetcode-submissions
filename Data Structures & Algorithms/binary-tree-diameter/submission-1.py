# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            hleft = dfs(root.left)
            hright = dfs(root.right)
            res = max(res, hleft + hright)

            return 1 + max(hleft, hright)
        dfs(root)
        return res