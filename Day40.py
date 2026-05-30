# Day 40 - Reverse Bits
# Platform: LeetCode

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for _ in range(32):                  # loop through all 32 bits
            result = (result << 1) | (n & 1) # shift result left, add last bit of n
            n >>= 1                          # shift n right to process next bit
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(43261596))   # Expected: 964176192
    print(sol.reverseBits(2147483644)) # Expected: 1073741822
