
"""
Created on Mon May 29 10:34:58 2021

@author: hbc
"""
from collections import defaultdict

# This is a O(N^2) time complexity and O(N) space complexity solution
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # create a dictionary
        # Note that the default value is 0
        map_I = defaultdict(int)
        # get the length of arrays (all are same)
        n = len(nums1)
        # this will be the return value
        total_count = 0
        
        # calculate all possible additions witn the first two arrays
        for i in range(n):
            for j in range(n):
                # increase counter for each value
                map_I[nums1[i]+nums2[j]] += 1
        
        # now we will search the other two arrays if we find values that yields the sum 0
        for i in range(n):
            for j in range(n):
                # if there is a value in the target sum
                if map_I[-nums3[i]-nums4[j]]:
                    # count all possibilities
                    total_count += map_I[-nums3[i]-nums4[j]]
        
        # return number of all possibilities
        return total_count
            
s = Solution()
result = s.fourSumCount([1,2], [-2,-1], [-1,2], [0,2])
print(result)
        

