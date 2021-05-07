
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

# This is a O(N) computational complexity and O(1) space complexity solution to the problem
from typing import List

### Here starts my code
class Solution(object):
    def lengthOfLongestSubstring(self, string):
        # Initialize the variables
        sub_string = {}
        left_idx = 0
        right_idx = 0
        max_val = 0
        n = len(string)
        # search for the longest substring inside a loop
        while(left_idx < n and right_idx < n):
            # get the new character
            new_char = string[right_idx]
            # set the new substring
            sub_string = string[left_idx:right_idx]
            # check if the new character is in the substring
            if(new_char in sub_string):
                # if yes, set the left index to the right
                left_idx += sub_string.find(new_char) + 1
            # set the max
            max_val = max(max_val, right_idx - left_idx + 1)
            # increase the right index
            right_idx += 1
        return max_val
            
s = Solution()
result = s.lengthOfLongestSubstring('abcabcbb')
print(result)
        
        