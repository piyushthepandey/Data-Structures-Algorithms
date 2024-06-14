class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        total_moves = 0
        previous = nums[0]
        for i in range(1, len(nums)): 
            if nums[i] <= previous: 
                previous += 1 
                total_moves+= previous - nums[i]
                print(total_moves)
            else: 
                previous = nums[i]
        return total_moves