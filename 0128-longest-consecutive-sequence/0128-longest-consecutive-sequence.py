class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            nums_set = set(nums) 
            count = 0 

            for num in nums: 
                if num - 1 not in nums_set: 
                    length = 1
                    while num + length in nums_set: 
                        length += 1 
                    
                    count = max(count, length)
            return count
                
