class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0 
        high = n - 1

        while low<=high: 
            mid=(low+high)//2 

            if nums[mid] == target: 
                return mid 
            elif target > nums[mid]: 
                low = mid + 1 
            else: 
                high = mid - 1 

        return low


            
          
       

