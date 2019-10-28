//package Tree;

//import Tree.TreeNode;
public class TreeBuilder {
    int val_;
    TreeNode parent_ = null;
    TreeNode left_ = null;
    TreeNode right_ = null;

    public TreeNode buildTree() {
        return new TreeNode(this.val_, this.parent_, this.left_, this.right_);
    }

    TreeBuilder setVal(int x) {
        this.val_ = x;
        return this;
    }

    TreeBuilder setParent(TreeNode parent) {
        this.parent_ = parent;
        return this;
    }

    TreeBuilder setLeft(TreeNode left) {
        this.left_ = left;
        return this;
    }

    TreeBuilder setRight(TreeNode right) {
        this.right_ = right;
        return this;
    }
}