class Solution:
    def moveZeroes(self, nums):
        zero_index = 0
        n = len(nums)
        for non_zero_index in range(n):
            if nums[zero_index] != 0:
                nums[zero_index] = nums[non_zero_index]
                zero_index += 1
        for i in range(zero_index, n):
            nums[i] = nums[zero_index]
