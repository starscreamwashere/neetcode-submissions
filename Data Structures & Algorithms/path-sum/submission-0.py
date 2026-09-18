# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.summ = 0
        self.truth = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # Add current node's value to the running total
        self.summ += root.val

        # Check subtrees recursively
        if root.left:
            self.hasPathSum(root.left, targetSum)
        if root.right:
            self.hasPathSum(root.right, targetSum)

        # Leaf node check
        if not root.left and not root.right:
            if self.summ == targetSum:
                self.truth = True

        # Backtrack: subtract value before returning up the tree
        self.summ -= root.val

        return self.truth