# Day 19 - Binary tree node
# Platform: LeetCode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
       
        result, stack = [], []
        current = root
        
        while current or stack:
            while current:              # Go to the leftmost node
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)  # Visit node
            current = current.right     # Move to right subtree
        
        return result

# Example usage

if __name__ == "__main__":
  
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    sol = Solution()
    print(sol.inorderTraversal(root))  # Output: [1, 3, 2]
