class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or all(x == 0 for x in nums):
            return
        last_non_zero_found_at = 0 
        for current in range(n):
            if nums[current] != 0:
                nums[last_non_zero_found_at] = nums[current]
                last_non_zero_found_at += 1
        for i in range(last_non_zero_found_at, n):
            nums[i] = 0