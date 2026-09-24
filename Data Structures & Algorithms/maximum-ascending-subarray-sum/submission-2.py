class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l, r = 0, 1
        maxSum = nums[l]
        runningSum = nums[l]
        runningMax = nums[l]

        while r < len(nums):
            if nums[r] > nums[l] and nums[r] > runningMax:
                runningSum += nums[r]
                runningMax = nums[r]
                maxSum = max(maxSum, runningSum)
            else:
                l = r
                runningMax = nums[l]
                runningSum = nums[l]
            r += 1
        return maxSum