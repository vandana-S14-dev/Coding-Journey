# Day 11 - Length Of Last Word
# Platform: LeetCode

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Trim trailing spaces
        s = s.rstrip()
        length = 0
        # Scan backwards until a space is found
        for char in reversed(s):
            if char == " ":
                break
            length += 1
        return length


# Output
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))              # Output: 5
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
    print(sol.lengthOfLastWord("luffy is still joyboy"))    # Output: 6
