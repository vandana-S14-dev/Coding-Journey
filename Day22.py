# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        # Recursively compute depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


# -----------------------------
# Example usage (you can run this in VS Code)
# -----------------------------
if __name__ == "__main__":
    # Build a sample tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    sol = Solution()
    print("Maximum Depth:", sol.maxDepth(root))  # Expected output: 3

    # Another example: [1,null,2]
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    print("Maximum Depth:", sol.maxDepth(root2))  # Expected output: 2
