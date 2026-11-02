class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result =  nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            result = max(result, current)
        return result