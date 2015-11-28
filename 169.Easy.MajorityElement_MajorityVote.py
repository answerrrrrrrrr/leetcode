class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
    # Majority Vote
        vote = 1
        candidate = num[0]
        for i in num[1:]:
            if vote == 0:
                candidate, vote = i, 1
            elif i == candidate:
                vote += 1
            else:
                vote -= 1
        return candidate



    # sorted
        return sorted(num)[len(num)/2]