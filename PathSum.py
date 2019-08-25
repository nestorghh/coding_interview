class TreeNode():
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None


def PathSum(root,suma):
	
	if not root:
		return False


	suma-= root.val
	
	if not root.left and not root.right:
		return suma == 0

	return PathSum(root.left,suma) or PathSum(root.right,suma)


def PathSum2(root,suma):

	#if not root:
	#	False	

	stack=[(root,suma-root.val)]

	while len(stack)!=0:
		
		node, value = stack.pop()

		if not node.left and not node.right and value==0:
			return True
		
		if node.left:
			stack.append((node.left,value-node.left.val))
		
		if node.right:
			stack.append((node.right,value - node.right.val))
	return False
			

a=TreeNode(5)
a.left=TreeNode(4)
a.right=TreeNode(8)
a.left.left=TreeNode(11)
a.left.left.left=TreeNode(7)
a.left.left.right=TreeNode(2)
a.right.left=TreeNode(13)
a.right.right=TreeNode(4)
a.right.right.right=TreeNode(1)



