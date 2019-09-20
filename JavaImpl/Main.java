// import Solution;
import java.util.*;
import LC315;
public class Main{
    public static void main(String[] args) {
        //LC149
        // Solution so = new Solution();
        // int[][] points = { { 84, 250 }, { 0, 0 }, { 1, 0 }, { 0, -70 }, { 0, -70 }, { 1, -1 }, { 21, 10 }, { 42, 90 },
        //         { -42, -230 } };
        // int result = so.maxPoints(points);

        //LC315
        LC315 so = new LC315();
        int[] nums = {5,2,6,1};
        List<Integer> result = so.countSmaller(nums);
        System.out.println(result);
    }
}