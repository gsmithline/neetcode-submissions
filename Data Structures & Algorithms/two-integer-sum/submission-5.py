class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holder = {} #keys value, value is index

        for i in range(len(nums)):
            if holder.get(target - nums[i], None) != None:
                return [holder[target - nums[i]], i]
            else:
                holder[nums[i]] = i

        