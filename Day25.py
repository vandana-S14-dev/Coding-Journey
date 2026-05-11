# Day 25 - Balenced Binary Tree  
# Platform: LeetCode

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0  # height of empty tree is 0
            
            left_height = check(node.left)
            if left_height == -1:  # left subtree not balanced
                return -1
            
            right_height = check(node.right)
            if right_height == -1:  # right subtree not balanced
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1  # current node not balanced
            
            return max(left_height, right_height) + 1
        
        return check(root) != -1


# ---------------------------
# Example usage in VS Code
# ---------------------------
if __name__ == "__main__":
    # Example 1: Balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(Solution().isBalanced(root1))  # True

    # Example 2: Unbalanced tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    print(Solution().isBalanced(root2))  # False

    # Example 3: Empty tree
    root3 = None
    print(Solution().isBalanced(root3))  # True
