# Day 6 - 
# Platform: LeetCode

class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # pointer for next non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# Example usage
if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    solution = Solution()
    k = solution.removeElement(nums, val)

    print("k =", k)          # Output: 5
    print("nums[:k] =", nums[:k])  # Output: [0, 1, 3, 0, 4] (order may vary)
