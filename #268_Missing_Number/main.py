
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

# This is a O(N) computational complexity and O(1) space complexity solution to the problem
from typing import List

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #I will first sort the array and then do a binary search
        # initialize the indexes
        left_idx = 0
        right_idx = len(nums) - 1
        mid_idx = 0
        # sort the array
        nums.sort()
        # search the missing number inside a loop
        while(left_idx <= right_idx):
            mid_idx = int((left_idx + right_idx)/2)
            # check if the value at mid_idx is the correct value
            if(nums[mid_idx] == mid_idx):
                left_idx = mid_idx + 1
            else:   
                right_idx = mid_idx - 1
        return left_idx

"""
Just hit to my mind :) There is a faster solution to this porblem: 
    I can calculate the expected sum, which is n*(n+1)*/2
    and the difference between the actual sum of the array and expected sum is the missing value
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n*(n+1)/2
        return expected_sum - sum(nums)
"""
        
            
s = Solution()
result = s.missingNumber([0])
print(result)
        
        