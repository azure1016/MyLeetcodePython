def inorder_traversal(tree):
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            # We came down to tree from parent
            if tree.left: # Keep going left
                next = tree.left
            else:
                result.append(tree.data)
                # Done with left, so go right if right is not empty
                # Otherwise, go up.
                # The reason why we need to go right is because the tree itself not only 
                # serves as the leftmost node, but also a parent of its right children (no left
                # children according to the condition)
                next = tree.right or tree.parent
        elif tree.left is prev:
            # we came up to tree from its left child
            result.append(tree.data)
            # Done with left, so go right if right is not empty. Otherwise, go up
            next = tree.right or tree.parent
        else: # Done with both children, so move up
            next = tree.parent
        prev, tree = tree, next
    return result