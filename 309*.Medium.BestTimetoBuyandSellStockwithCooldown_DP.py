class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
# DP
    # https://leetcode.com/discuss/71351/5-lines-python-o-n-time-o-1-space

    # 1. sell[i]      --- sell on Day.i
            # ==> hold[i-1] + price[i]
    # 2. free[i]      --- do nothing on Day.i
            # ==> sell[i-1]      --- cool down by one day
         # or ==> free[i-1]      --- do nothing (only used to handle Day.0)
    # 3. hold[i]      --- hold on Day.i
            # ==> free[i-1] - price[i]      --- buy on Day.i
         # or ==> hold[i-1]                 --- hold (baught a few days ago)

        sell, free, hold = 0, 0, float('-inf')
        for p in prices:
            sell, free, hold = hold + p, max(sell, free), max(free - p, hold)
        return max(sell, free)
