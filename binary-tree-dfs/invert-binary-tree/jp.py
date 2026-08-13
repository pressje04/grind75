from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

class Solution:
        def invertBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
                if not root:
                       return None
                
                left = self.invertBinaryTree(root.left)
                right = self.invertBinaryTree(root.right)

                #Actual invert op.
                root.left = right
                root.right = left

                return root

def test():
      sol = Solution()


if __name__ == "__main__":
       test()
               
                             