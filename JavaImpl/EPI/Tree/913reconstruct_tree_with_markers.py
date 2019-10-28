# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Reconstructor:
    def reconstruct_preorder(self, preorder):
        def reconstruct_preorder_helper(preorder_iter):
            subtree_key = next(preorder_iter)
            if subtree_key is None:
                return None

            # note that reconstruct_preorder_helper updates preorder_iter. So the order
            # of following two calls are critical
            left_subtree = reconstruct_preorder_helper(preorder_iter)
            right_subtree = reconstruct_preorder_helper(preorder_iter)
            return TreeNode(subtree_key, left_subtree, right_subtree)
            
        return reconstruct_preorder_helper(iter(preorder))

sol = Reconstructor()
arr = ['H', 'B', 'F', None, None, 'E', 'A', None, None, None, 'C', None, 'D', None, 'G', 'I', None, None, None]
tree = sol.reconstruct_preorder(arr)
print("hello world!")