class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def longestPali(s, l, r):
            while l >= 0 and r >= 0 and l < len(s) and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]
        
        res = ""
        for i in range(len(s)):
            odd = longestPali(s, i, i)
            even = longestPali(s, i, i+1)
            res = max(res, odd, even, key=len)
        return res