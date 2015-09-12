class Solution:
	# @param {string} s
	# @return {integer}
	def lengthOfLastWord(self, s):
		array_s = s.split()
		if array_s:
			return len(array_s[-1])
		else:
			return 0