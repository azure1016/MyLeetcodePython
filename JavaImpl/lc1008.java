import java.util.stream.IntStream;
import utils.*;
// class TreeNode {
//     int val;
//     TreeNode left;
//     TreeNode right;

//     TreeNode (int x) {this.val = x;}
// }
public class lc1008 {
    public TreeNode bstFromPreorder(int[] preorder) {
        return helper(preorder, 0, preorder.length - 1);
    }

    private TreeNode helper(int[] preorder, int start, int end) {
        if (start > end)
            return null;
        TreeNode root = new TreeNode(preorder[start]);
        //int index_right = IntStream.range(start, end + 1).filter(i -> preorder[i] > preorder[start]).findFirst().getAsInt();
        int index_right = indexBigger(preorder, start + 1, end, preorder[start]);
        root.left = helper(preorder, start + 1, index_right - 1);
        if (index_right < end + 1)
            root.right = helper(preorder, index_right, end);
        return root;
    }
 
    private int indexBigger(int[] preorder, int start, int end, int target) {
        for (int i = start; i < end; i++) {
            if (preorder[i] > target)
                return i;
        }

        return end;
    }

    public static void main (String[] args) {
        int[] preorder = new int[] {8, 5, 1, 7, 10, 12};
        lc1008 inst = new lc1008();
        TreeNode root = inst.bstFromPreorder(preorder);
        System.out.println(root.left.val);
    }
}