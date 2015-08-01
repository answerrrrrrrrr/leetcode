class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str = str.strip()
        digits = '1234567890'
        valid = digits + '-+'
        num = ''
        result = 0
        for i in xrange(len(str)):
            if str[i] not in valid:
                break
            if i < len(str) - 1 and str[i] in '-+' and str[i+1] not in digits:
                break
            if str[i] in digits:
                num += str[i]
                if str[i-1] == '-':
                    num = '-' + num
                if i == len(str) - 1 or str[i+1] not in digits:
                    result = int(num)
                    break

        if  result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result
