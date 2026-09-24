class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        dupe = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
            dupe[ord(c) - ord('a')] += 1

        for i in range(len(s2) - len(s1) + 1):
            window = s2[i : i + len(s1)]

            for c in window:
                s1_count[ord(c) - ord('a')] -= 1

            if not any(s1_count):
                return True
            else:
                s1_count = dupe.copy()

        return False