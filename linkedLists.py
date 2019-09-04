class ListNode():
	def __init__(self,data=0,next=None):
		self.data = data
		self.next = next

#search for a key in a linked list:

def search_list(L, key):
	while L and L.data!=key:
		L=L.next
	return L


L=ListNode(3)
L.next=ListNode(45)
L.next.next=ListNode(28)
L.next.next.next=ListNode(11)
L.next.next.next.next=ListNode(20)

#insert a new node after a specified one:

def insert_after(node,newnode):
	newnode.next = node.next
	node.next=newnode


#delete a node past this one. Assume node is not a tail.

def delete_after(node):
	node.next=node.next.next


#Merge two sorted lists
	
def merge_two_sorted_lists(L1,L2):

	prehead = ListNode(-1)

	prev = prehead

	while L1 and L2:
		if L1.data < L2.data:
			prev.next = L1
			L1 = L1.next
		else:
			prev.next = L2
			L2 = L2.next
		prev = prev.next

	prev.next = L1 or L2
	
	return prehead.next
	

# reverse a linked list

def reversed_linked_list(L):
	
	prev = None
	current = L

	while current:
		nexTemp = current.next
		current.next = prev
		prev = current
		current = nexTemp

	return prev
	

# print a linked list
def print_list(L):
	s=''
	while L:
		s=s+str(L.data)+"==>"
		L=L.next
	return s













