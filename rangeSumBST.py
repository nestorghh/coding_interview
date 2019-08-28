#Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
#The binary search tree is guaranteed to have unique values.

class TreeNode():
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None


class Solution():

	def rangeSumBST(self,root, L, R):

		def dfs(node):
			if node is not None:
				if L<= node.val <= R:
					self.total+=node.val
				if L<node.val:
					dfs(node.left)
				if node.val<R:
					dfs(node.right)
		self.total = 0
		dfs(root)	
		return self.total
 	
a=TreeNode(8)
a.left = TreeNode(3)
a.right = TreeNode(10)
a.left.left = TreeNode(1)
a.left.right = TreeNode(6)
a.left.right.left = TreeNode(4) 
a.left.right.right = TreeNode(7)
a.right.right = TreeNode(14)
a.right.right.left = TreeNode(3)



