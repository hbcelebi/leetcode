
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""
from collections import defaultdict

# This is a O(N) space and time complexity solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a dictionary
        # Note that: The default value is 0
        map_m = defaultdict(int)
        # go through every number inside the array
        for number in nums:
            # if already seen before return True
            if map_m[number]:
                return True
            # otherwise save that value inside the dictionary
            map_m[number] = 1
        # if no duplicate, return False
        return False
            
s = Solution()
result = s.containsDuplicate([1,2,3,4])
print(result)

result = s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(result)
        

