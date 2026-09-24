class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
        s = s.lower()
        newS = ""

        for c in s:
            if c in alphabet:
                newS += c
        
        return newS == newS[::-1]