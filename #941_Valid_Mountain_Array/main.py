#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:40:58 2021

@author: hbc
"""
# This is a possible solution to the #941 Valid Mountain Array problem at Leetcode.
# The solution is O(N) computational complexity and O(1) space complexity 

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # First, control if the length of the array is longer than 3
        if(len(arr) < 3):
            return False
        # check if the array is ascending 
        idx = 1
        while(idx < len(arr) and arr[idx] > arr[idx-1]):
            idx += 1
        # if we are at the end of the array already, return False (since it has to descend as well)
        if(idx == 1 or idx == len(arr)):
            return False
        # check if the array is descending
        while(idx < len(arr) and arr[idx] < arr[idx-1]):
            idx += 1
        # return True (It is True if the index is at the end of the array)
        return idx == len(arr)

s = Solution()
result = s.validMountainArray([1,2,3,4,5,6,7,6,5,4,3,1])
print(result)