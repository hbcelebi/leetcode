
"""
Created on Mon May 21 23:20:28 2021

@author: hbc
"""

### Here starts my code w dynamic programming
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # if the total length is less than 2 then return the original string
        if(n<2):
            return s
        # set the inititla indexes
        left = 0
        right = 0
        
        # intitialize a 2D array
        palindrome = [[0]*n for _ in range(n)]
        
        # 
        for j in range(1,n):
            for i in range(0,j):
                # check if the inner substring is palindrome
                innerIsPalindrome = palindrome[i+1][j-1] or j-i<=2
                if(s[i] == s[j] and innerIsPalindrome):
                    palindrome[i][j] = True
                    if(j-i>right-left):
                        left = i
                        right = j

        return s[left:right+1] 
            
s = Solution()
result = s.longestPalindrome("aacabdkacaa")
print(result)
        
result = s.longestPalindrome("aaaabaaa")
print(result)

        