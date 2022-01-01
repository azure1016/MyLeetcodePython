class Solution { // the critical point is which one will be left as the last one to be bursted https://leetcode.com/problems/burst-balloons/discuss/1659162/JAVA-or-DP-or-Divide-and-Conquer-or-Sliding-Window-or-Detailed-Explanation-Using-Image
    public int maxCoins(int[] nums) {
        int n = nums.length;
        int[] balloons = new int[n+2];
        balloons[0] = 1;
        balloons[n+1] = 1;
        for (int i = 0; i < n; i++) {
            balloons[i+1] = nums[i];
        }
        
        int[][] memo = new int[n+2][n+2];
        return burstMemo(memo, balloons, 0, n+1);
    }
    
    private int burstMemo(int[][] memo, int[] balloons, int left, int right) {
        if (left + 1 == right)
            return 0; // only 2 numbers
        if (memo[left][right] != 0) 
            return memo[left][right];
        
        int ans = -1;
        for (int i = left + 1; i < right; i++) {
            int leftRes = burstMemo(memo, balloons, left, i);
            int rightRes = burstMemo(memo, balloons, i, right);
            ans = Math.max(ans, balloons[left] * balloons[i] * balloons[right] + leftRes + rightRes);
        }
        memo[left][right] = ans;
        return ans;
    }
}

