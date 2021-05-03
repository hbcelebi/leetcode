#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

from typing import List

class Solution(object):
    def moveZeroes(self, nums: List[int]) -> None:
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for num in nums:
            if(num != 0):
                nums[j] = num
                j += 1

        for x in range(j, len(nums)):
            nums[x] = 0
            
        print([nums])
            
s = Solution()
s.moveZeroes([0, 2, 0, 4, 5, 8, 0, 6])
        
        