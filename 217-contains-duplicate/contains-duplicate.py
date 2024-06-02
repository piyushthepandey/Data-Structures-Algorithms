class Solution(object):
    def containsDuplicate(self, nums):
        ele = set()
        for element in nums: 
            if element not in ele:
                ele.add(element)
            else: 
                return True
        return False