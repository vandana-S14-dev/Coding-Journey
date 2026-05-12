# Day 27 - Path sum
# Platform: LeetCode

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        # Base case: empty tree
        if not root:
            return False
        
        # Leaf node check
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursive check on left and right subtrees
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))


# -------------------------------
# Example usage 
# -------------------------------

if __name__ == "__main__":
    # Build example tree: [5,4,8,11,null,13,4,7,2,null,null,null,1]
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11, TreeNode(7), TreeNode(2))
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4, None, TreeNode(1))

    sol = Solution()
    print(sol.hasPathSum(root, 22))  # Expected output: True
    print(sol.hasPathSum(root, 26))  # Expected output: True (5->8->13