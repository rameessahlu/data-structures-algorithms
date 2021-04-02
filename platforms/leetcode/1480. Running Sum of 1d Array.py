class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for n in range(0,len(nums)):
            if n == 0:
                continue
            else:
                nums[n] = nums[n]+nums[n-1]
        return nums