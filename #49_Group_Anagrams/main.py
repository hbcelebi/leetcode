
"""
Created on Mon May 25 10:00:18 2021

@author: hbc
"""

# This is a O(N*M*log(M)) computational complexity and O(N) space complexity solution to the problem
from typing import List

class Solution:
    # this is a simple hashing function can be used for this question
    # it returns the sorted version of the string 
    def calculateHash(self, string):
        return ''.join(sorted(string))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize the list 
        result = []
        # initialize a dictionary
        map_m = {}
        
        # for all strings inside the string array
        for sub_str in strs:
            # calculate the hash value
            idx = self.calculateHash(sub_str)
            # if no same hash has been created in dict, create one, as a list
            if idx not in map_m:
                map_m[idx] = []
            # append the new string 
            map_m[idx].append(sub_str)
            
        # create the list from the values inside the dictionary
        for val in map_m.values():
            result.append(val)
        
        # return the list
        return result
        
s = Solution()
result = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)
        

        