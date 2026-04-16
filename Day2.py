# Day 2 - Two Sum 
# Platform: LeetCode

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]  
                
# Calling the function
s = Solution()
print(s.twoSum([2,7,11,15], 9)) # Returns index positions of numbers that add up to target


