# Day 26 - Minimum depth of binary tree 
# Platform: LeetCode

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # If one child is missing, we must go down the other
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # Both children exist, take the minimum
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


# ---------------------------
# Helper function to build a tree from list input
def build_tree(values):
    """
    Build a binary tree from a list of values (level-order).
    None represents a missing node.
    """
    if not values:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


# ---------------------------
# Example usage 
if __name__ == "__main__":
    # Example 1
    root1 = build_tree([3,9,20,None,None,15,7])
    print("Minimum depth (Example 1):", Solution().minDepth(root1))  # Output: 2

    # Example 2
    root2 = build_tree([2,None,3,None,4,None,5,None,6])
    print("Minimum depth (Example 2):", Solution().minDepth(root2))  # Output: 5
