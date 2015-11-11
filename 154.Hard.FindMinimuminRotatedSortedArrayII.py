class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # O(n)
        for i in xrange(1, len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
        return nums[0]



    # O(logn)
        l, r = 0, len(nums)-1
        while l < r:
            while l < r and nums[l] == nums[l+1]:
                l += 1
            m = (l + r)/2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

    # O(logn)
        start, end = 0, len(nums)-1
        while start < end:
            mid =(start +end)/2
            if nums[mid]> nums[end]:
                start =mid+1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -=1
        return nums[end]
