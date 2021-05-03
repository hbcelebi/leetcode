
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

# This is a O(N) computational complexity and O(1) space complexity solution to the problem
from typing import List

### Here starts my code
class Solution(object):
    def moveZeroes(self, nums: List[int]) -> None:
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # initialize the index
        idx = 0
        
        # search through the array and move the nonzeros to the beginning of the array
        for num in nums:
            if(num != 0):
                nums[idx] = num
                idx += 1
        
        # add zeros at the end of the array
        for x in range(idx, len(nums)):
            nums[x] = 0
            
        print([nums])
            
s = Solution()
s.moveZeroes([0, 2, 0, 4, 5, 8, 0, 6])
        
        