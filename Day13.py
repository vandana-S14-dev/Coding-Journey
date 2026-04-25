# Day 13 - Plus One
# Platform: LeetCode

# plus_one.py

class Solution(object):
    def plusOne(self, digits):
        
        n = len(digits)

        # Traverse from the last digit backwards
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0

        # If all digits were 9, we need an extra 1 at the front
        return [1] + digits


if __name__ == "__main__":
    s = Solution()
    # Test cases
    print(s.plusOne([1, 2, 3]))    # [1, 2, 4]
    print(s.plusOne([4, 3, 2, 1])) # [4, 3, 2, 2]
    print(s.plusOne([9]))          # [1, 0]
    print(s.plusOne([9, 9, 9]))    # [1, 0, 0, 0]
