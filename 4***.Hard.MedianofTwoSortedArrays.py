class Solution(object):
    def findMedianSortedArrays(self, a, b):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(a) + len(b)
        fk = self.findKth
        return fk(a,b,l/2) if l%2 == 1 else (fk(a,b,l/2-1) + fk(a,b,l/2))/2.0
    def findKth(self, a, b, k):
        if len(a) > len(b):
            a, b = b, a
        if not a:
            return b[k]
        if k == len(a)+len(b)-1: # eg: [1] & [2,3,4] --> [1] & [2,3] 
            return max(a[-1],b[-1])
        i = len(a)/2
        j = k - i
        if a[i] > b[j]:
            return self.findKth(a[:i], b[j:], k-j)
        else:
            return self.findKth(a[i:], b[:j], k-i)
