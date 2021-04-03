class Solution:
    def sumOfNaturalNumbers(self, n):
        return int((n*(n-1))/2)
    
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numbers_and_its_freq = {}
        for n in nums:
            if n not in numbers_and_its_freq:
                numbers_and_its_freq[n] = 1
            else:
                numbers_and_its_freq[n] += 1
        
        result = 0
        for k, v in numbers_and_its_freq.items():
            if v > 1:
                result += self.sumOfNaturalNumbers(v)
        return result