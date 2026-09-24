class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)

        l, r = 0, 1

        firstNum = fruits[0]
        secondNum = fruits[1]
        res = 2

        while r < len(fruits):
            if fruits[r] != firstNum and fruits[r] != secondNum:
                res = max(res, r - l)

                l = r - 1
                while l > 0 and fruits[l - 1] == fruits[r - 1]:
                    l -= 1

                firstNum = fruits[r - 1]
                secondNum = fruits[r]

            r += 1

        res = max(res, r - l)
        return res