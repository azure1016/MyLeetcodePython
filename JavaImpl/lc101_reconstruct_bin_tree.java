import java.util.stream.IntStream;
import utils.*;
// class TreeNode {
//     int val;
//     TreeNode left;
//     TreeNode right;

//     TreeNode (int x) {this.val = x;}
// }
public class lc101_reconstruct_bin_tree {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildHelper(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
    }

    private TreeNode buildHelper(int[] preorder, int pre_start, int pre_end, int[] inorder, int in_start, int in_end) {
        if (pre_start > pre_end | in_start > in_end)
            return null;
        TreeNode root = new TreeNode(preorder[pre_start]);
        int index_root = IntStream.range(in_start, in_end + 1).filter(i -> root.val == inorder[i]).findFirst().getAsInt();
        //int index_root = indexOf(inorder, in_start, in_end, root.val);
        int left_length = index_root - in_start;
        int right_length = in_end - index_root;
        root.left = buildHelper(preorder, pre_start + 1, pre_start + left_length, inorder, in_start, index_root - 1);
        root.right = buildHelper(preorder, pre_end - right_length + 1, pre_end, inorder, index_root + 1, in_end);
        return root;
    }

    private int indexOf(int[] array, int start, int end, int target) {
        for (int i = start; i <= end; i++) {
            if (array[i] == target) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] preorder = new int[] {1, 2, 4, 5, 6, 3, 7, 8, 9};
        int[] inorder = new int[] {4, 2, 6, 5, 1, 3, 7, 9, 8};
        lc101_reconstruct_bin_tree instance = new lc101_reconstruct_bin_tree();
        TreeNode root = instance.buildTree(preorder, inorder);
        System.out.println(root.val);
    }
}