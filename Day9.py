# Day 9 - Find The Index Of The First Occurance In A String
# Platform: LeetCode

class Solution(object):
    def strStr(self, haystack, needle):
        # Edge case: if needle is empty, return 0
        if not needle:
            return 0

        n, m = len(haystack), len(needle)

        # Loop through haystack up to the point where needle can fit
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        # If not found, return -1
        return -1


# Example usage in VS Code
if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))     # Output: 0
    print(sol.strStr("leetcode", "leeto"))    # Output: -1
