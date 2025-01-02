class Solution:
    def missingNumber(self, nums):
        currentSum = sum(nums)
        n = len(nums)
        intendedSum = n*(n+1)/2
        return int(intendedSum - currentSum)