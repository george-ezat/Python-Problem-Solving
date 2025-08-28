# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, p, q):
        if not (p or q):
            return True

        if p and q and p.val == q.val:
            return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
