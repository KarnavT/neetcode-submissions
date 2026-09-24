class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] % 2 == 1:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r -= 1
            elif nums[r] % 2 == 0:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                l += 1
            else:
                l += 1
                r -= 1
        return nums