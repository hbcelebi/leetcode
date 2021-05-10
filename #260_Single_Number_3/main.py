
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""
from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        # I use the Counter function, which finds the set of all distinct elements in an array with the number of their occurences
        result = []
        # use Counter()
        count_all_elements = Counter(nums)
        # take the occurence times
        values = list(count_all_elements.values())
        # take the values
        keys = list(count_all_elements.keys())
        # find the first value that occured 1 time
        idx = values.index(1)
        result.append(keys[idx])
        # to find the second one, delete the one recently found
        del values[idx]
        # find the second value that occured 1 time and append it
        result.append(keys[values.index(1)+1])
        # return the list
        return result
            
s = Solution()
result = s.singleNumber([0,1,0,0,-2])
print(result)
        

