# Day 31 -  Single number
# Platform: LeetCode

class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 1]))        # Output: 1
    print(s.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
    print(s.singleNumber([1]))              # Output: 1
