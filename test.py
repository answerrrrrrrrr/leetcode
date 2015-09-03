class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
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

def testCases():

    nums = [-4,-2,0,1,2,4]
    # Input:
    # [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    # Output:
    # [[-4,-2,6],[-4,0,4],[-2,-2,4],[-4,1,3],[-2,0,2]]
    # Expected:
    # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]


    sol = Solution()
    sol.threeSum(nums)

def main():
    testCases()
    

if __name__ == "__main__":
    main()