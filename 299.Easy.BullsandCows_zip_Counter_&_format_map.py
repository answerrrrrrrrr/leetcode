class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
    # dict
    # 68ms, 71.76%
        d = {}
        bull, cow = 0,0
        for i,s in enumerate(secret):
            if guess[i] == s:
                bull += 1
            else:
                d[s] = d.get(s,0) + 1
        for i,s in enumerate(secret):
            if (guess[i] != s) & (d.get(guess[i],0) != 0):
                cow += 1
                d[guess[i]] -= 1
        return str(bull) + "A" + str(cow) + "B"



    # https://leetcode.com/discuss/67008/java-python-o-n-solutions
    # zip, Counter, &, format
    # 84ms, 44.17%
        bulls = sum(g == s for g, s in zip(guess, secret))
        cows = sum((Counter(guess) & Counter(secret)).values()) - bulls
        return '{0}A{1}B'.format(bulls, cows)



    # https://leetcode.com/discuss/67016/3-lines-in-python
    # map, operator, count
    # 48ms, 98.72%
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(i), guess.count(i)) for i in '1234567890')
        return '%dA%dB' % (bulls, both-bulls)
        # return '%sA%sB' % (bulls, both-bulls)
