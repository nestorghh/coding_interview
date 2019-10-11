class Node():
	def __init__(self,val):
		self.val =  val
		self.left = None
		self.right = None

def inOrder(root):
	
	if root:
		inOrder(root.left)
		print(root.val)
		inOrder(root.right)

def preOrder(root):
	
	if root:
		print(root.val)
		preOrder(root.left)
		preOrder(root.right)

def postOrder(root):
	
	if root:
		postOrder(root.left)
		postOrder(root.right)
		print(root.val)
	





