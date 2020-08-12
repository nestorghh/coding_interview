# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        from collections import Counter
        def count(node):
            counter[node.val]+=1
            if node.left: 
                count(node.left)
            if node.right:
                count(node.right)

        if not root:
            return[]
        
        counter = Counter()
        count(root)
        maxi = max(counter.values())
        
        return [key for key,value in counter.items() if value==maxi]
