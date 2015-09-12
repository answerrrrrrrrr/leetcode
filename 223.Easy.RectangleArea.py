class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        l = max(A, E)
        b = max(B, F)
        r = min(C, G)
        t = min(D, H)
        if l > r or b > t:
            l = b = r = t = 0
        ra = self.rectArea
        return ra(A, B, C, D) + ra(E, F, G, H) - ra(l, b, r, t)
    
    def rectArea(self, l, b, r, t):
        return (r - l) * (t - b)