class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        for i in path.split('/'):
            if i not in ['.','..','']:
                res.append(i)
            if i == '..' and res:
                res.pop()
        return '/' + '/'.join(res)