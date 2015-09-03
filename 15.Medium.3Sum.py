class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
# https://leetcode.com/discuss/1760/any-solution-which-is-better-than-o-n-2-exists?show=1770#a1770
# The best time complexity is O(n^2)



# https://leetcode.com/discuss/32455/a-simply-python-version-based-on-2sum-o-n-2
    # Based on 2Sum
    # 500ms+
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            pairs = self.twoSum(nums[i+1:], -nums[i])
            if pairs:
                for pair in pairs:
                    triplet = [nums[i]] + pair 
                    if triplet not in res:
                        res.append(triplet)
        return res
    def twoSum(self, nums, target):
        showed, res = {}, []
        for i in nums:
            if target - i in showed:
                res.append([target - i, i])
            showed[i] = 1
        return res



    # 3 pointers
    # 280ms+
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    k -= 1; j += 1
                    print res
        return list(set(res)) # too slow

    # Faster on avoiding duplication
    # 200ms
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            # Avoid duplicates with i-1 had been computed
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    k -= 1; j += 1
        return res




























