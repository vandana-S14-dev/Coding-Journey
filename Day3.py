# Day 3 - Palindrome Number 
# Platform: LeetCode

class Solution(object):
    def isPalindrome(self, x):
        # Negative or ending with 0 (but not 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10
        
        return x == reversed_half or x == reversed_half // 10


# Taking input from user
x = int(input("Enter a number: "))

# Creating object and calling function
obj = Solution()
result = obj.isPalindrome(x)

# Printing result
print("Is Palindrome:", result)