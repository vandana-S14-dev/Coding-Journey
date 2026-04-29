# Day 17 - Climbing Stairs
# Platform: LeetCode

class Solution(object):
    def climbStairs(self, n):

        if n <= 2:
            return n

        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


# Output
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))  # Output: 2
    print(sol.climbStairs(3))  # Output: 3
    print(sol.climbStairs(4))  # Output: 5
    print(sol.climbStairs(5))  # Output: 8
