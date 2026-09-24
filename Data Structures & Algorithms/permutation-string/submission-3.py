class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        
        for i in range(len(s2) - len(s1) + 1):
            window = s2[i : i + len(s1)]
            curr_count = [0] * 26
            for c in window:
                curr_count[ord(c) - ord('a')] += 1
            match = True
            for i in range(len(s1_count)):
                if s1_count[i] != curr_count[i]:
                    match = False
            if match:
                return True
        return False