class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        res = []
        for num, cnt in count.items():
            if cnt > len(nums) // 3:
                res.append(num)
        
        return res