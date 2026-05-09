# Day 24 - Pascal's Triangle    
# Platform: LeetCode

class Solution(object):
    def generate(self, numRows):
        triangle = []

        for row in range(numRows):
            # Each row starts with 1s
            new_row = [1] * (row + 1)

            # Fill in the middle values
            for j in range(1, row):
                new_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]

            triangle.append(new_row)

        return triangle


# Example usage:
sol = Solution()
print(sol.generate(5))  # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(sol.generate(1))  # [[1]]
