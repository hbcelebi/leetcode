#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 11:14:51 2021

@author: hbc
"""

# This is a O(N) computational complexity and O(1) space complexity solution to the problem
from typing import List

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        idx = 0
        if m == 0:
            return True
        # loop over the long string and check if the value is in the substring
        for value in t:
            if value == s[idx]:
                idx += 1
            # if we are already at the end of the substring return True
            if idx == m:
                return True
        # return True if we reach the end of substring
        return idx == m
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        map_words = dict()
        
        # This solution is not feasible since the loop runs for every unique string in the list
        for string in words:
            # check if the string has already been analyzed
            if string not in map_words:
                # if not, then check if it is a substring
                map_words[string] = 0
                if self.isSubsequence(string, s):
                    map_words[string] += 1
            # otherwise just what has been done before 
            # if it is higher than 0, it means that the string is a substring, then increase +1
            else:
                if map_words[string] > 0:
                    map_words[string] += 1
        
        return sum(map_words.values())
            
s = Solution()
array = "abcde"
sequences = ["a","bb","acd","ace","ace","ace","ace","ace","ace","ace"] 
print(s.numMatchingSubseq(array, sequences))

array = "dsahjpjauf"
sequences = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
print(s.numMatchingSubseq(array, sequences))