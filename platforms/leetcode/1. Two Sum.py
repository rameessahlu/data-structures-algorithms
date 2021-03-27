class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempArray = []
        for n in range(0,len(nums)):
            if (target-nums[n]) not in tempArray:
                tempArray.append(nums[n])
            else:
                return [n, nums.index((target-nums[n]))]