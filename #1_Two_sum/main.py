
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

# This is a O(N) space and time complexity solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # I solve this problem with mapping
        map_m = {}
        for number in range(0,len(nums)):
            goal = target - nums[number]
            if goal in map_m:
                return [map_m[goal], number]
            map_m[nums[number]] = number
        return
            
s = Solution()
result = s.twoSum([2,7,11,15,], 9)
print(result)
        

