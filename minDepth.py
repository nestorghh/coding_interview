def minDepth(root):

	if not root:
		return float('inf')

	if not root.left and not root.right:
		return 1
	else:
		return 1 + min(minDepth(root.left), minDepth(root.right))

a=TreeNode(5)
a.left=TreeNode(4)
a.right=TreeNode(8)
a.left.left=TreeNode(11)
a.left.left.left=TreeNode(7)
a.left.left.right=TreeNode(2)
a.right.left=TreeNode(13)
a.right.right=TreeNode(4)
a.right.right.right=TreeNode(1)


