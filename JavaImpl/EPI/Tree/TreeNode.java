//package Tree;

public class TreeNode {
    int val;
    TreeNode parent = null;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode() {
    }

    public TreeNode(int x) {
        this.val = x;
        this.parent = null;
        this.left = null;
        this.right = null;
    }

    public TreeNode(int x, TreeNode parent) {
        this.val = x;
        this.parent = parent;
    }

    public TreeNode(int x, TreeNode parent, TreeNode left, TreeNode right) {
        this.val = x;
        this.parent = parent;
        this.left = left;
        this.right = right;
    }
}
