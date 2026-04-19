# Day 7 - Remove Duplicates From Sorted Array
# Platform: LeetCode

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k


# --- Test code ---
if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [1,1,2]
    k1 = sol.removeDuplicates(nums1)
    print("Output:", k1, ", nums =", nums1[:k1])  # Expected: 2, [1,2]
    
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = sol.removeDuplicates(nums2)
    print("Output:", k2, ", nums =", nums2[:k2])  # Expected: 5, [0,1,2,3,4]
