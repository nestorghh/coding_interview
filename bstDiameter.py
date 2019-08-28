#Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. 

class Node():
	def __init__(self,val):
		self.val=val
		self.left=None
		self.right=None


maxi=0
def bstDiameter(root):
	def depth(node):
		global maxi
		if not node:
			return 0
		L = depth(node.left)
		R = depth(node.right)
		maxi = max(maxi,L+R)
		return 1+max(L,R)

	depth(root)
	return maxi

def bstDiameter2(root):

	def height(root):
		if not root:
			return 0
		return 1 + max(height(root.left),height(root.right))
		
	if not root:
		return 0

	# this is the case where the root is part of the longest path
	lheight = height(root.left)
	rheight = height(root.right)

	# this is the case where the root is not part of the longest path
	ldiameter = bstDiameter2(root.left)
	rdiameter = bstDiameter2(root.right)

	# compute the maximum between the two options
	return max(1+lheight+rheight, max(ldiameter,rdiameter))


a=Node(1)
a.left=Node(2)
a.right=Node(3)
a.left.left=Node(4)
a.left.right=Node(5)		



