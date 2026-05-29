# Day 39 - Number of 1 Bits
# Platform: LeetCode

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1   # add 1 if the last bit is set
            n >>= 1          # shift right to check next bit
        return count

print(Solution().hammingWeight(11))        # Output: 3
print(Solution().hammingWeight(128))       # Output: 1
print(Solution().hammingWeight(2147483645))# Output: 30
