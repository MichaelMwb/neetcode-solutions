class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for ind, num in enumerate(nums):
            goal = target - num
            if goal in mp:
                return [mp[goal],ind]
            else:
                mp[num] = ind
