class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return nums
        head = tail = 0
        new = []
        while tail < len(nums) - 1:
            if nums[tail + 1] != nums[tail] + 1:
                new.append(self.getRange(nums[head], nums[tail]))
                head = tail + 1
            tail += 1
        new.append(self.getRange(nums[head], nums[tail]))
        return new
            
    def getRange(self, head, tail):
        if head == tail:
            return str(head)
        else:
            return str(head) + "->" + str(tail)