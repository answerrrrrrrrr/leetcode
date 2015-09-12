class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin32 = '{:032b}'.format(n)
        reverseBin32 = bin32[::-1]
        return int(reverseBin32, 2)