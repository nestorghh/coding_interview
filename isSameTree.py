class TreeNode():
	def __init__(self, x):
		self.value = x
		self.left = None
		self.right = None

def isSameTree(p,q):
	
	# p and q are both None
	if not p and not q:
		return True

	# one of p and q is None
	if not q or not p:
		return False

	if p.value!=q.value:
		return False

	return isSameTree(p.left, q.left) and isSameTree(p.right,q.right)

a=TreeNode(5)
a.left=TreeNode(4)
a.right=TreeNode(8)
a.left.left=TreeNode(11)
a.left.left.left=TreeNode(7)
a.left.left.right=TreeNode(2)
a.right.left=TreeNode(13)
a.right.right=TreeNode(4)
a.right.right.right=TreeNode(1)

b=TreeNode(5)
b.left=TreeNode(4)
b.right=TreeNode(8)
b.left.left=TreeNode(11)
b.left.left.left=TreeNode(7)
b.left.left.right=TreeNode(2)
b.right.left=TreeNode(13)
b.right.right=TreeNode(4)
b.right.right.right=TreeNode(10)



