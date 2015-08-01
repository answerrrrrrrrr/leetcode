class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str = str.strip()
        num = ''
        result = 0
        
        if str and str[0] in '-+':
            num += str[0]
        for i in xrange(1, len(str)):
            if str[i].isdigit():
                num += str[i]
            else:
                break

        if len(num) > 1:
            result = int(num)

        if  result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result
