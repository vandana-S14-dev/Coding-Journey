# Day 5 - Valid Parenthese
# Platform: LeetCode

class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0

obj = Solution()

print(obj.isValid("()"))        # True
print(obj.isValid("()[]{}"))    # True
print(obj.isValid("(]"))        # False
print(obj.isValid("([])"))      # True
print(obj.isValid("([)]"))      # False