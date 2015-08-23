class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
    # 60ms+
        # if num <= 0:
        #     return False
        # while num%2 == 0:
        #     num /= 2
        # while num%3 == 0:
        #     num /=3
        # while num%5 == 0:
        #     num /= 5
        # if num == 1:
        #     return True
        # return False
    
    # Simplified
        if num <= 0:
            return False
        for p in 2,3,5:
            while num%p == 0:
                num /= p
        return num == 1
