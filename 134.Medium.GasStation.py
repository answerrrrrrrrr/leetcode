class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = cur = overall = 0
        for i in range(len(gas)):
            delta = gas[i] - cost[i]
            cur += delta
            overall += delta
            if cur < 0:
                cur, start = 0, i+1
        return -1 if overall < 0 else start
