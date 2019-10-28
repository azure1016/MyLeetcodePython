import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class Bloom {
    int minDaysBloomByDp(int[] roses, int k, int n) {
        int[] windowKmax = new int[roses.length - k + 1];
        fillMax(windowKmax,roses,k);
        int[][] dp = new int[n+1][roses.length + 1];
        for (int i = 1; i <= n; i++) {
            Arrays.fill(dp[i],Integer.MAX_VALUE);
            for (int j = k; j <= roses.length; j++) {
                dp[i][j] = Math.min(dp[i][j - 1], Math.max(dp[i - 1][j - k],windowKmax[j - k]));
            }
        }
        return dp[n][roses.length];
    }
    void fillMax(int[] windowKmax, int[] r, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < r.length; i++) {
            if (i >= k && r[i - k] == dq.peekFirst()) dq.pollFirst();
            while (!dq.isEmpty() && r[i] > dq.peekLast()) dq.pollLast();
            dq.offerLast(r[i]);
            if (i >= k - 1) windowKmax[i - k + 1] = dq.peekFirst();
        }
    }
//BS    
    int minDaysBloomByBS(int[] roses, int k, int n) {
        int min = Integer.MAX_VALUE, max = -1;
        for (int r : roses) {
            max = Math.max(r,max);
            min = Math.min(r,min);
        }
        int[] windowKmax = new int[roses.length - k + 1];
        fillMax(windowKmax,roses,k);
        int s = min, e = max;
        while (s <= e) {
            int mid = (e - s)/2 + s;
            if (search(windowKmax,n,k,mid)) {
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }
        return e + 1;
    }
    
    boolean search(int[] win,int n,int k,int day) {
        for (int i = 0; i < win.length; ) {
            if (day >= win[i]) {
                n--;
                i+=k;
            } else {
                i++;
            }
        }
        return n <= 0;
    }

    public static void main(String[] args) {
        int[] blooms = new int[] { 1, 2, 4, 9, 3, 4, 1 };
        Bloom bl = new Bloom();
        int minDay = bl.minDaysBloomByDp(blooms, 3, 2);
        int minDay2 = bl.minDaysBloomByBS(blooms, 3, 2);
        System.out.println(minDay);
    }

}
