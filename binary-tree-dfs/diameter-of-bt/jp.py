from typing import Optional

"""
Biggest thing is not to confuse diameter with height. The diameter of a bt node is the height of the left subtree + the right subtree.

You also can't just find the height of the left and height of the right from the root since u may have a path in a subtree with greater diameter that 
doesnt touch the root at all. So you have to be careful abt how you track diameter
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #return => max diameter of the given node
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #global variable to keep track of max diameter found, gets returned at the end
        self.max_diameter = 0

        #function to find the height of diameter given a node, should pass the root into this at first
        def dfs_height(node: Optional[TreeNode]):
            #easy base case
            if not node: 
                return 0

            #Get height of left + right subtrees and use that to get the diameter of the current node.
            left_height = dfs_height(node.left)
            right_height = dfs_height(node.right)

            local_diameter = left_height + right_height

            self.max_diameter = max(self.max_diameter, local_diameter)

            #Pass up HEIGHT, NOT diameter so that nodes further up can also use height to find their diameters
            #diameter is only useful for this specific node and checking if it's the max or not
            return 1 + max(left_height, right_height)
    
        dfs_height(root)
        return self.max_diameter
    
def test():
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(sol.diameterOfBinaryTree(root))

if __name__ == "__main__":
    test()
        
