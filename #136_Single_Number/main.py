
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

class Solution(object):
    def singleNumber(self, nums):
        # I use the set function, which finds the set of all distinct elements in an array
        return 2*sum(set(nums))-sum(nums)
            
s = Solution()
result = s.singleNumber([1,2,2,1,-5,6,6,9,9])
print(result)
        

