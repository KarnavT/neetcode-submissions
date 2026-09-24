class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            odd = self.longest_pali(s, i, i)
            even = self.longest_pali(s, i, i + 1)
            longest = max(odd, even, key=len)
            if len(longest) > len(res):
                res = longest
        return res


    
    def longest_pali(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]


