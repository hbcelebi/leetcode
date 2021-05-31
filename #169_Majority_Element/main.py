
"""
Created on Mon May 23 18:03:48 2021

@author: hbc
"""

from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # create a dictionary
        # Note that: The default value is 0
        map_m = defaultdict(int)
        # map elements 
        for number in nums:
            map_m[number] += 1
        # search the max value inside the dictionary, return the key
        max_key_value = max(map_m, key=map_m.get)
        return max_key_value
            
s = Solution()
result = s.majorityElement([2,2,1,1,1,2,2])
print(result)

result = s.majorityElement([3,2,3])
print(result)

        
        