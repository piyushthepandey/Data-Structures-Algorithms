class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_sum = sum(set(nums)) * 2
        total_sum = sum(nums)
        return unique_sum - total_sum