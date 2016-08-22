class Solution(object):
    def findMedianSortedArrays(self, a, b):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

# https://discuss.leetcode.com/topic/22406/python-o-log-min-m-n-solution/7
        l = len(a) + len(b)
        fk = self.findKth
        return fk(a, b, l / 2) if l % 2 == 1 else (fk(a, b, l / 2 - 1) + fk(a, b, l / 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = min(len(A) - 1, k / 2)  # In case of 'out of range', eg: [1,2,3] [4,5,6,7] k=5.
        j = k - i
        if A[i] < B[j]:
            # Unfortunately, get slice is O(k) in Python, so it's not a O(log(m+n)) solution.
            return self.findKth(A[i:], B[:j], k - i)
        else:
            return self.findKth(A[:i], B[j:], k - j)



# A real O(log(m+n)) solution using index instead of slice
        m, n = len(A), len(B)
        l = m + n
        if l & 1 == 1:
            return self.findKth(A, B, l/2, 0, m, 0, n)
        else:
            return (self.findKth(A, B, l/2-1, 0, m, 0, n) + self.findKth(A, B, l/2, 0, m, 0, n)) / 2.0

    def findKth(self, A, B, k, a1, a2, b1, b2):
        if a2-a1 > b2-b1:
            A, a1, a2, B, b1, b2 = B, b1, b2, A, a1, a2
        if a1 >= a2:
            return B[b1 + k]
        if b1 >= b2:
            return A[a1 + k]
        if a2-a1 + b2-b1 - 1 == k:
            return max(A[a2-1], B[b2-1])
        i = min(a2-a1 - 1, k / 2)
        j = k - i
        if A[a1 + i] < B[b1 + j]:
            return self.findKth(A, B, k-i, a1+i, a2, b1, b1+j)
        else:
            return self.findKth(A, B, k-j, a1, a1+i, b1+j, b2)



# Another O(log(m+n)) solution
# https://discuss.leetcode.com/topic/6947/intuitive-python-o-log-m-n-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms/9
