class TreeNode():
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

# Recursive solution
def maxDepth(root):
	
	if not root:
		return 0
	else:
		return 1 + max(maxDepth(root.left),maxDepth(root.right))
	


	
	
a=TreeNode(5)
a.left=TreeNode(4)
a.right=TreeNode(8)
a.left.left=TreeNode(11)
a.left.left.left=TreeNode(7)
a.left.left.right=TreeNode(2)
a.right.left=TreeNode(13)
a.right.right=TreeNode(4)
a.right.right.right=TreeNode(1)




