
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

class Solution(object):
    def singleNumber(self, nums):
        # I use the set function, which finds the set of all distinct elements in an array
        return (3*sum(set(nums))-sum(nums))/2
            
s = Solution()
result = s.singleNumber([0,1,0,1,0,1,99])
print(result)
        

