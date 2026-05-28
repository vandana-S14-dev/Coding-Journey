# Day 38 - Excel Sheet Column Number
# Platform: LeetCode

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for char in columnTitle:
            # Shift previous result left by one "digit" in base-26
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result

s = Solution()
print(s.titleToNumber("A"))   # Output: 1
print(s.titleToNumber("AB"))  # Output: 28
print(s.titleToNumber("ZY"))  # Output: 701
