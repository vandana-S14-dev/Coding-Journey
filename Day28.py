# Day 28 - Pascals-triangle-ii
# Platform: LeetCode

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]  # First element is always 1
        prev = 1
        for i in range(1, rowIndex + 1):
            # Compute next value using the relation:
            # C(rowIndex, i) = C(rowIndex, i-1) * (rowIndex - i + 1) / i
            curr = prev * (rowIndex - i + 1) // i
            row.append(curr)
            prev = curr
        return row

# Example usage:
sol = Solution()
print(sol.getRow(3))  # Output: [1, 3, 3, 1]
print(sol.getRow(0))  # Output: [1]
print(sol.getRow(1))  # Output: [1, 1]
