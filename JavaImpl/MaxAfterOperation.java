'''
O(m*p+n), p: max(a[i]- b[i])
Input : n = 5 m = 3
        a = 0, b = 1, k = 100
        a = 1, b = 4, k = 100
        a = 2, b = 3, k = 100
Output : 200
Explanation:
Initially array = {0, 0, 0, 0, 0}
After first operation:
array = {100, 100, 0, 0, 0}
After second operation:
array = {100, 200, 100, 100, 100}
After third operation:
array = {100, 200, 200, 200, 100}
Maximum element after m operations 
is 200.

[100, 100, -100, 0, 0, -100]
1.
array[start] += k
array[end + 1] -= k O(1)
prefix1: [100, 100, 0, 0, 0]
prefix2 [100, 200, 100, 100, 100, 0]
etc
2. extend space to avoid 
'''




public class MaxAfterOperation {
    static long findMax(int n, int m, int a[], int b[], int k[]) {
        int[] arr = new int[n+1];

        for (int i = 0; i < m; i++) {
            int lowerBound = a[i];
            int upperBound = b[i];
            arr[lowerBound] += k[i];
            // reduce upper_bound + 1 indexed value by k
            arr[upperBound + 1] -= k[i];
        }

        // find maximum sum possible from all values
        long sum = 0, res = Integer.MIN_VALUE;
        for (int i = 0; i < n; ++i) {
            sum += arr[i];// prefix sum of i+1
            res = Math.max(res, sum);
        }
        return res;
    }

    public static void main (String[] args) {
        int n = 5;
        int m = 3;
        int a[] = {0, 1, 2};
        int b[] = {1, 4, 3};
        int k[] = {100, 100, 100};
        System.out.println("maximum value after " + "m operations is " + findMax(n, m, a, b, k));
    }
}