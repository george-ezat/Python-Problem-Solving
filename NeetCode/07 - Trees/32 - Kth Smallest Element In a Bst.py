# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def inOrder(node):
            if not node:
                return

            inOrder(node.left)
            arr.append(node.val)
            inOrder(node.right)

        inOrder(root)
        return arr[k - 1]


# OR (optimal)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        def inOrder(node):
            nonlocal cnt, res

            if not node:
                return

            inOrder(node.left)

            cnt -= 1
            if cnt == 0:
                res = node.val
                return

            inOrder(node.right)

        inOrder(root)
        return res
