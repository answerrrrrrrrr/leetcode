class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		d = dict() # use dict to update the latest index of every num
		for i, n in enumerate(nums):
			lastIndex = d.get(n)
			if lastIndex >= 0 and i - lastIndex <= k:
				return True
			d[n] = i
		return False