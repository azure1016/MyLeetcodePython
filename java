class Solution {
    public int leastOpsExpressTarget( int x, int target) {
    Map<Integer, Integer> hm = new HashMap<>();

    if (target == 1) {
    // x cannot be 1 or 0
    return 1;
    }

    //needed for recursive call
    if (hm.containsKey (target)){
        return hm.get (target);
    }

    long product = x;
    int count = 0;
    while ((int)product < target) {
        count ++;
        product *= x;
    }

    //two possible ways to get target: x ^ (k+1) - something = target, or x ^ k + something = target
    //one of these two would produce the least number of operators

    //option 1
    int opt1 = Integer.MAX_VALUE;
    if (product ==  target) {
        opt1 = count;
    } else if (product - target < target) {
        opt1 = count + leastOpsExpressTarget (x, (int) (product - target)) + 1;
    }

    //option 2
    int opt2 = Ingeter.MAX_VALUE;

    product /= x;
    //count --;
    opt2 = count + leastOpsExpressTarget (x, (int) (target - product)) + count == 0 ? 2 : count;

    int ans = Math.min (opt1, opt2);
    hm.put (target, ans);
    return ans;
    }
}
