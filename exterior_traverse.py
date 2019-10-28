from lc_util import Tree

def exterior_binary_tree(tree):
    def is_leaf(node):
        return not node.right and not node.left
    
    # computes the nodes from the root to the leftmost leaf followed by all the 
    # leaves in subtree
    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree: return []
        return (([subtree.val] if is_boundary or is_leaf(subtree) else []) + 
        left_boundary_and_leaves(subtree.left, is_boundary) +
        left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left))

    # computes the leaves in left-to-right order followed by the rightmost 
    # leaf to the root path in subtree
    def right_boundary_and_leaves(subtree, is_boundary):
        if not subtree: return []
        return (right_boundary_and_leaves(subtree.left, is_boundary and not subtree.right) +
        right_boundary_and_leaves(subtree.right, is_boundary) 
        + ([subtree.val] if is_boundary or is_leaf(subtree) else []))


    return ([tree.val] + left_boundary_and_leaves(tree.left, True) 
    + right_boundary_and_leaves(tree.right, True) if tree else [])

def test(a_list):
    instance = Tree(a_list)
    root = instance.deserialize(test1)
    result = exterior_binary_tree(root)
    print(result)

test1 = [3, 9, 20, 30, 31, None, 21, None, None, None, 32, None, 22, 4, 5, 15]
test(test1)