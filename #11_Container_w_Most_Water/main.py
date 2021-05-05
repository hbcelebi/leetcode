
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

# This is a O(N) computational complexity and O(1) space complexity solution to the problem
from typing import List

class Solution(object):
    def maxArea(self, height):
        # Initialize the indexes  
        left_idx = 0
        right_idx = len(height) - 1
        # initialize the temporary estimated volume
        max_estimated_volume = 0
        # inside a loop, we search for the max
        while(left_idx < right_idx):
            max_estimated_volume = max(max_estimated_volume,
                                       (right_idx-left_idx)*min(height[right_idx], height[left_idx]))
            # move the right or left index depending on their values in array
            if(height[left_idx] < height[right_idx]):
                left_idx += 1
            else:
                right_idx -= 1
        # return the max
        return max_estimated_volume
            
s = Solution()
result = s.maxArea([3, 2, 1, 4, 5, 8, 5, 6])
print(result)
        