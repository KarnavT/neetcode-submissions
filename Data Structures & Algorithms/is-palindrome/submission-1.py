class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = set("abcdefghijklmnopqrstuvwxyz1234567890")
        s = s.lower()
        chars = []

        for c in s:
            if c in alphabet:
                chars.append(c)

        newS = "".join(chars)
        return newS == newS[::-1]