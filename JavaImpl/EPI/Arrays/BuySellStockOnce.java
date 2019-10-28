// EPI 5.8 buy and sell stock once

public class BuySellStockOnce {
    public int buySellStockOnce (int[] prices) {
        int cur_sum = 0, max_sum = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] - prices[i-1] + cur_sum <= 0) {
                cur_sum = 0;
            }
            else {
                cur_sum += prices[i] - prices[i-1];
            }
            max_sum = Math.max(max_sum, cur_sum);
        }
        return max_sum;
    }

    public static void main (String[] args) {
        int[] prices = {310, 315, 275, 295, 260, 270, 290, 230, 255, 250};
        BuySellStockOnce instance = new BuySellStockOnce();
        int max_profit = instance.buySellStockOnce(prices);
        System.out.println(max_profit);
    } 
}