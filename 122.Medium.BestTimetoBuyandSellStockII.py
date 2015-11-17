class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    # 48ms
        if not prices:
            return 0
        lo, res, i = prices[0], 0, 0
        while i+1 < len(prices):
            while i+1 < len(prices) and prices[i] >= prices[i+1]:
                i += 1
            lo = prices[i]
            while i+1 < len(prices) and prices[i] <= prices[i+1]:
                i += 1
            res += prices[i] - lo
        return res



    # 56ms
        return sum(max(prices[i+1] - prices[i], 0) for i in xrange(len(prices) - 1))