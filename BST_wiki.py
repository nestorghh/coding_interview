class BSTNode():
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None

	def __str__(self):
		return "key: %s \n left: %s \n right: %s" % (self.key, self.left, self.right)

a=BSTNode(8)
a.left = BSTNode(3)
a.right = BSTNode(10)
a.left.left = BSTNode(1)
a.left.right = BSTNode(6)
a.left.right.left = BSTNode(4) 
a.left.right.right = BSTNode(7)
a.right.right = BSTNode(14)
a.right.right.left = BSTNode(3)

# Searching 
def recursive_search(node,key):
	if not node or key==node.key:
		return node
	if key<node.key:
		return recursive_search(node.left,key)
	if key>node.key:
		return recursive_search(node.right,key)

def iterative_search(node,key):
	current_node = node

	while current_node is not None:
		if key == node.key:
			return node
		if key<node.key:
			current_node = node.left
		if key>node.key:
			current_node = node.right
	return current_node
	
#Because in the worst case this algorithm must search from the root of the tree to the leaf farthest from the root, the search operation takes time proportional to the tree's height. On average, binary search trees with n nodes have O(log n) height.




