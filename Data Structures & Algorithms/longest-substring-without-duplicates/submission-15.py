class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        curLet = set()
        res = 0

        while r < len(s):
            if s[r] not in curLet:
                curLet.add(s[r])
                res = max(res, len(curLet))
                r += 1
            else:
                curLet.remove(s[l])
                l += 1

        return res