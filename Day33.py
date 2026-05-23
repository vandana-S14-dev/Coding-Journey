# Day 33 - Binary Tree Preorder Traversal
# Platform: LeetCode

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def dfs(node):
            if not node:
                return
            # Step 1: Visit root
            result.append(node.val)
            # Step 2: Traverse left
            dfs(node.left)
            # Step 3: Traverse right
            dfs(node.right)

        dfs(root)
        return result

if __name__ == "__main__":
    # Build a sample tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    print("Preorder Traversal:", sol.preorderTraversal(root))
    # Expected output: [1, 2, 4, 5, 3]
