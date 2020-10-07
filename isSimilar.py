# check if two binary trees have the same structure.

# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isSimilar(a,b):

    if a is None or b is None:
        return a is None and b is None

    return isSimilar(a.left,b.left) and isSimilar(a.right,b.right)






