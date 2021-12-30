class Solution {
    public int smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) return -1; // not possible for even numbers or 5s
        int len = 1, n = 1;
        while (n % k != 0) {
            n = (n * 10 + 1) % k;
            len++;
        }
        return len;
    }
}