# Day 15 - sqrt(X)
# Platform: LeetCode

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x  # sqrt(0)=0, sqrt(1)=1
        
        left, right = 2, x // 2  # sqrt(x) is always <= x//2 for x >= 2
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # right will be the floor of sqrt(x)


# Output
if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))   # Expected output: 2
    print(sol.mySqrt(8))   # Expected output: 2
    print(sol.mySqrt(15))  # Expected output: 3
    print(sol.mySqrt(1))   # Expected output: 1
    print(sol.mySqrt(0))   # Expected output: 0
