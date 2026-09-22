from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs_height(node: Optional[TreeNode]) -> int:
            if not node: 
                return 0

            #To get the max depth, we take the max of the depth of the left + right subtrees
            left_depth = dfs_height(node.left)
            right_depth = dfs_height(node.right)

            #pass up the height so that parent nodes can use it to calculate depth
            return 1 + max(left_depth, right_depth)
        
        return dfs_height(root)

def test():
    sol = Solution()
    
    #Set up BT
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(sol.maxDepth(root))

if __name__ == "__main__":
    test()
