class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        # v1, v2 = map(int, version1.split('.')), map(int, version2.split('.'))
        # while len(v1) != 0 and len(v2) != 0:
        #     if v1[0] > v2[0]:
        #         return 1
        #     elif v1[0] < v2[0]:
        #         return -1
        #     else:
        #         v1, v2 = v1[1:], v2[1:]

        # if v1 and v1[0]:
        #     return 1
        # elif v2 and v2[0]:
        #     return -1
        # else:
        #     return 0
        
        v1, v2 = map(int, version1.split('.')), map(int, version2.split('.'))
        v1 += [0] * (len(v2) - len(v1))
        v2 += [0] * (len(v1) - len(v2))
        return cmp(v1, v2)