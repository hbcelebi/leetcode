
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

# This is a O(N) computational complexity and O(1) space complexity solution to the problem
from typing import List

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_x = 0
        move_y = 0
        # this is a relatively simple solution 
        for move in moves:
            if move == 'U':
                move_y += 1
            elif move == 'D':
                move_y -= 1
            elif move == 'R':
                move_x += 1
            elif move == 'L':
                move_x -= 1
        # return True if move_x and  move_y are both zero
        return not(bool(move_x) or bool(move_y))
        
            
s = Solution()
result = s.judgeCircle("LDRRLRUULR")
print(result)
        
result = s.judgeCircle("LL")
print(result)
        