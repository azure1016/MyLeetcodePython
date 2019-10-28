import java.util.List;
import java.util.ArrayList;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Arrays;

public class InorderParent {  
    public InorderParent () {}

    public List<Integer> inorder_traverse (TreeNode root) {
        if (root != null) return null;
        List<Integer> result = new ArrayList<Integer>();
        TreeNode node = root, prev = null, next = null;
        while (node != null) {
            if (prev == node.parent) { // going DOWN from prev
               if (node.left != null) next = node.left;
               else {
                   result.add(node.val);
                   next = node.right != null ? node.right : node.parent;
               }
            } else if (node.left == prev) { // going UP from prev
                result.add(node.val);
                next = node.right != null ? node.right : node.parent;
            } else { // done with both childer
                 next = node.parent;
            }

            prev = node;
            node = next;
        }
        return result;
    }

    public TreeNode deserialize (List<Integer> sequence) {
        TreeNode root = new TreeNode(sequence.get(0));
        Deque<TreeNode> queue = new ArrayDeque<TreeNode> ();
        queue.offer(root);
        for (int i = 1; i < sequence.size();) {
           TreeNode cur = queue.poll();
           if (sequence.get(i) != -100){
               cur.left = new TreeNode(sequence.get(i));
               cur.left.parent = cur;
               queue.offer(cur.left);
           }
           if (i+1 < sequence.size() & sequence.get(i+1) != -100) {
               cur.right = new TreeNode(sequence.get(i+1));
               cur.right.parent = cur;
               queue.offer(cur.right);
           }
           i += 2;
        }
        return root;
    }
    public static void main (String[] args) {
        List<Integer> input = new ArrayList<Integer> (Arrays.asList(3, 9, 20, -100, -100, 15, 7));
        
        InorderParent instance = new InorderParent();
        TreeNode root = instance.deserialize(input);
        if (root == null) System.out.println("somthing");
        List<Integer> result = instance.inorder_traverse(root);
       
        for (int i = 0; i < result.size(); i++) {
            System.out.println(" " + result.get(i).toString());
        }
    }
}