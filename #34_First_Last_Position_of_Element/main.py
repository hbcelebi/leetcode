
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

# This is a O(N) computational complexity and O(1) space complexity solution to the problem
from typing import List

### Here starts my code
class Solution(object):
    def searchRange(self, nums, target):
        # The algorithm first finds the initial position of the target, then the last position
        # Initialize the variables
        left_idx = 0
        right_idx = len(nums) - 1
        first_position = -1
        # let's do binary search to find the first location
        while(left_idx <= right_idx):
            # set the middle index inbetween the two indexes
            mid_idx = int((left_idx + right_idx)/2)
            # if we already found the target check if it is the first location
            if nums[mid_idx] == target:
                if mid_idx == 0 or nums[mid_idx-1] != target:
                    first_position = mid_idx
                right_idx = mid_idx - 1
            elif nums[mid_idx] < target:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1
        
        # if there is no first_position then there is no target value inside the array 
        if first_position == -1:
            return [-1, -1]
        
        # Initialize the variables for the second loop
        left_idx = 0
        right_idx = len(nums) - 1
        # let's do binary search to find the last location
        while(left_idx <= right_idx):
            # set the middle index inbetween the two indexes
            mid_idx = int((left_idx + right_idx)/2)
            # if we already found the target check if it is the last position
            if nums[mid_idx] == target:
                if mid_idx == len(nums) - 1 or nums[mid_idx+1] != target:
                    last_position = mid_idx
                left_idx = mid_idx + 1
            elif nums[mid_idx] < target:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1
        
        # return the positions
        return [first_position, last_position]
        
            
s = Solution()
result = s.searchRange([10, 11, 11, 11, 14, 15], 11)
print(result)
        
        