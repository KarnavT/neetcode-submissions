class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        while s:
            rem = False
            count = 1
            curr = s[0]
            for i in range(1, len(s)):
                if curr != s[i]:
                    count = 0
                    curr = s[i]
                count += 1
                if count == k:
                    s = s[:i - count + 1] + s[i + 1:]
                    rem = True
                    break

            if not rem:
                break

        return s