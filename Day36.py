# Day 36 - excel-sheet-column-title
# Platform: LeetCode

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        while columnNumber > 0:
            columnNumber -= 1  # adjust for 1-indexed system
            remainder = columnNumber % 26
            result.append(chr(ord('A') + remainder))
            columnNumber //= 26
        return ''.join(reversed(result))

s = Solution()
print(s.convertToTitle(1))    # Output: "A"
print(s.convertToTitle(28))   # Output: "AB"
print(s.convertToTitle(701))  # Output: "ZY"
