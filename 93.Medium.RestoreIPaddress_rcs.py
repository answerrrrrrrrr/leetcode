class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
# https://leetcode.com/discuss/77/restore-ip-addresses?show=11032#a11032
    # rcs
    # 52ms
        res = []
        self.dfs(s, '', 4, res)
        return res

    def valid(self, s):
        if len(s) == 2 and s[0] == '0':
            return False
        if len(s) == 3 and (s[0] == '0' or s > '255'):
            return False
        return True

    def dfs(self, s, ip, subnet, res):
        if subnet == 0:
            if s == '':
                res.append(ip.rstrip('.'))
            return
        else:
            for i in range(1,4):
                if len(s) >= i and self.valid(s[:i]):
                    self.dfs(s[i:], ip + s[:i] + '.', subnet-1, res)