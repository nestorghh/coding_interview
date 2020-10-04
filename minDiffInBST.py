# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        def inOrderTraversal(TreeNode):
            if TreeNode:
                inOrderTraversal(TreeNode.left)
                self.ans = min(self.ans, TreeNode.val -self.prev)
                self.prev = TreeNode.val
                inOrderTraversal(TreeNode.right)
                
        self.prev = float('-inf')
        self.ans = float('inf')
        inOrderTraversal(root)
        
        return self.ans
