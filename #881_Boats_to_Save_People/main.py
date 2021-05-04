
"""
Created on Tue May  4 09:14:54 2021

@author: hbc
"""

# This is a possible solution to the #881 Boats to Save People problem at Leetcode.
# The solution is O(N) computational complexity and O(1) space complexity 
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # first, sort the people array
        people.sort()
        
        # initialize the indexes
        left_idx = 0
        right_idx = len(people)-1
        
        # initiliaze the number of boats
        boats_number = 0
        
        # in a loop, match one person from left with someone on the right
        while(left_idx <= right_idx):
            # the indexes are met, we need to break the loop 
            if(left_idx == right_idx):
                boats_number += 1
                break
            # if one from right and one from left are less htna the threshold
            if(people[left_idx] + people[right_idx] <= limit):
                left_idx += 1
                right_idx -= 1
                boats_number += 1
            # else, only carry a heavy man
            else:
                right_idx -= 1
                boats_number += 1
        # return the totla number of boats
        return boats_number

s = Solution()
result = s.numRescueBoats([1, 2, 1, 4, 5, 8, 4, 6], 8)
print(result)
