class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            binary = bin(i)
            binary = binary[2:]
            counter = 0
            for c in binary:
                if c == "1":
                    counter += 1
            res.append(counter)
        return res