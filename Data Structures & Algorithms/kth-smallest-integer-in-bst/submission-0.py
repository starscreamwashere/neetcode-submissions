class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []
        
        def inorder(node):
            if not node:
                return None
            
            # 1. Traverse left
            left_res = inorder(node.left)
            if left_res is not None:
                return left_res
            
            # 2. Process current node
            order.append(node.val)
            if len(order) == k:
                return node.val
            
            # 3. Traverse right
            return inorder(node.right)

        return inorder(root)