class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
# https://leetcode.com/discuss/44281/4-lines-o-log-n-c-java-pytho
    # Java version
    # int countDigitOne(int n) {
    #     int ones = 0;
    #     for (long long m = 1; m <= n; m *= 10) {
    #         int a = n/m; //higher digits + current digit
    #         int b = n%m; //lower digits
    #         ones += (a + 8) / 10 * m + (a % 10 == 1) * (b + 1);
    #     }
    #     return ones;
    # }
        ones, m = 0, 1
        while m <= n:
            a, b = n/m, n%m
            ones += (a + 8) / 10 * m  +  (a % 10 == 1) * (b + 1)
            m *= 10
        return ones

# https://leetcode.com/discuss/44302/1-liners-in-python