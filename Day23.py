# Day 22 - Convert sorterd array to binary search tree 
# Platform: LeetCode

from typing import List, Optional
from collections import deque

# Define TreeNode for local testing
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)

# Utility: print tree in level-order (array style)
def serialize(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

# Example usage
if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    sol = Solution()
    root = sol.sortedArrayToBST(nums)
    print("Serialized BST:", serialize(root))

    nums2 = [1, 3]
    root2 = sol.sortedArrayToBST(nums2)
    print("Serialized BST:", serialize(root2))
