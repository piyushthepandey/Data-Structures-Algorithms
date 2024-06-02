class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {} 
        for i in range(len(nums)):
            if nums[i] not in my_dict: 
                my_dict[nums[i]]=i 
            else:
                if abs(i - my_dict[nums[i]]<=k):
                    return True
                my_dict[nums[i]]=i 
        return False
