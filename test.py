class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def test(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            print l
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res

def testCases():

    i = [1,1,2,2]
    sol = Solution()
    sol.test(i)

def main():
    testCases()
    

if __name__ == "__main__":
    main()