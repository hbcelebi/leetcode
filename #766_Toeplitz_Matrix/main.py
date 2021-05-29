
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

# This is a O(M) computational complexity and O(N) space complexity solution to the problem
from typing import List
import numpy as np

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # check if the first N-1 elements are same with next rows last N-1 elements
        for i in range(len(matrix)-1):
            temp_vec_1 = matrix[i][0:len(matrix[i])-1]
            temp_vec_2 = matrix[i+1][1:len(matrix[i+1])]
            if np.sum(np.abs(np.subtract(temp_vec_1, temp_vec_2))):
                return False
        return True
            
s = Solution()
result = s.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
print(result)
     
result = s.isToeplitzMatrix([[1,2],[2,2]])
print(result)   

result = s.isToeplitzMatrix([[1,2,3,4],[5,2,1,3]])
print(result)   


        