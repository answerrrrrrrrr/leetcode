class Solution:
    # @param {integer[]} digits
    # @param {integer[]}
    def plusOne(self, digits):
        # # carry = 1
        # # for i in range(len(digits)-1, -1, -1):
        # #     carry, digits = divmod(digits[i]+carry, 10)
        # #     if carry == 0:
        # #         break
        # # if carry:
        # #     digits.insert(0, carry)
        # # return digits
        # for i in range(len(digits)-1, -1, -1):
        #     digits[i] = (digits+1) % 10
        #     if digits[i]:
        #         break
        # else:
        #     digits.insert(0,1)
        # return digits



        # create a new list
        return map(int, list(str(reduce(lambda x, y: 10*x+y, digits)+1)))
