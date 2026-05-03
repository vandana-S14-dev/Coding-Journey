# Day 20 - Sample tree
# Platform: LeetCode

# Solution.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


# ---------------------------
# Example usage / test cases
# ---------------------------
if __name__ == "__main__":
    # Example 1: p = [1,2,3], q = [1,2,3]
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)

    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)

    print("Example 1:", Solution().isSameTree(p1, q1))  # True

    # Example 2: p = [1,2], q = [1,null,2]
    p2 = TreeNode(1)
    p2.left = TreeNode(2)

    q2 = TreeNode(1)
    q2.right = TreeNode(2)

    print("Example 2:", Solution().isSameTree(p2, q2))  # False

    # Example 3: p = [1,2,1], q = [1,1,2]
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)

    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)

    print("Example 3:", Solution().isSameTree(p3, q3))  # False
