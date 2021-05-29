#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 19:03:51 2021

@author: hbc
"""

class Solution:
    def decodeString(self, s: str) -> str:
        str_decoded = ""
        i = 0
        while(i < len(s)):
            iter_number = ""
            # if there is a number inside the string get the number of repeats
            if s[i].isnumeric():
                iter_number += s[i]
                if s[i+1].isnumeric():
                    iter_number += s[i+1]
                    i += 1
                    if s[i+1].isnumeric(): # repeat number can be up to 3 digits
                        iter_number += s[i+1]
                        i += 1
                # check if there is an additional repeat seq inside the brackets
                # if there is, copy paste the current string and continue
                if s.find('[',i+2) > 0 and s.find('[',i+2) < s.find(']',i+2):
                    str_decoded += iter_number
                    i += 1
                    continue;
                # if there is repeat seq inside the brackets, do the repeating
                idx_start = i+2
                idx_end = s.find(']',i+1)
                str_decoded += int(iter_number)*s[idx_start:idx_end]
                i = idx_end+1
            # nothing to do, only copy the character
            else:
                str_decoded += s[i]
                i += 1
            # if we finish the string but if there is still brackets inside the string
            # go back and do the repeatings
            if i == len(s) and str_decoded.find('[') > 0:
                s = str_decoded
                str_decoded = ""
                i = 0
        # return
        return str_decoded
    
s = Solution()

solution = s.decodeString("13[a2[c4[x]]]")
print(solution)

