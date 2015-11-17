class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    # 52ms, reduce max and min
        if not prices:
            return 0
        lo, res, i = prices[0], 0, 0
        while i+1 < len(prices):
            while i+1 < len(prices) and prices[i] <= prices[i+1]:
                i += 1
            res = max(res, prices[i] - lo)
            while i+1 < len(prices) and prices[i] >= prices[i+1]:
                i += 1
            lo = min(lo, prices[i])
        return res



    # 68ms
        if not prices:
            return 0
        lo, res = prices[0], 0
        for i in xrange(1, len(prices)):
            res = max(res, prices[i] - lo)
            lo = min(lo, prices[i])
        return res