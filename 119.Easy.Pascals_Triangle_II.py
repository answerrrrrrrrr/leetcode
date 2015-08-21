class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        # retRow = [1]
        # for i in xrange(rowIndex):
        #     retRow = [0] + retRow + [0]
        #     retRow = [retRow[j] + retRow[j+1] for j in xrange(i+2)]
        # return retRow


        
        retRow = [1]
        for i in xrange(rowIndex):
            retRow = map(lambda x, y: x+y, [0]+retRow, retRow+[0])
        return retRow