class Solution:
    def containsDuplicate(self, nums):
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                return True
            m[nums[i]] = True
        return False