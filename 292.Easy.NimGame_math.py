class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # strategy: the one with 4 remaining must loose
        # A, B players
        # if n == 4k, then at each round B can make A+B both take 4, 
        # eventually leave 4 to A, A lose
        # if n == 4k + i (i <= 3), then A can always take i first and B will
        # finanly lose as he faces above scenario like A

        return n%4 != 0



        return bool(n%4)



        return bool(n&3)