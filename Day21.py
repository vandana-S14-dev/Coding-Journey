# Day 21 - Symmetric tree
# Platform: LeetCode

# symmetric_tree.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and
                    isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))

        return isMirror(root.left, root.right)


# --- Quick test harness ---
if __name__ == "__main__":
    # Example 1: Symmetric tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root1.right = TreeNode(2, TreeNode(4), TreeNode(3))

    print("Example 1:", Solution().isSymmetric(root1))  # Expected True

    # Example 2: Not symmetric
    root2 = TreeNode(1)
    root2.left = TreeNode(2, None, TreeNode(3))
    root2.right = TreeNode(2, None, TreeNode(3))

    print("Example 2:", Solution().isSymmetric(root2))  # Expected False
