# Day 34 - Binary Tree Postorder Traversal
# Platform: LeetCode

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)   # Visit left subtree
            dfs(node.right)  # Visit right subtree
            result.append(node.val)  # Visit root
        
        dfs(root)
        return result

if __name__ == "__main__":
    # Build tree: [1,null,2,3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    sol = Solution()
    print(sol.postorderTraversal(root))  # Output: [3,2,1]
