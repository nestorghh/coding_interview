# P1) Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

class Node(object):
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class singlellist(object):
	head = None
	tail = None

	def show(self):
		x = self.head
		while x is not None:
			print(x.data, end='')
			print(' -> ', end='')
			x = x.next
		print(None)
	
	def append(self,data):
		new_node = Node(data,None)
		if self.head is None:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node #current tail needs to point to new_node
			self.tail = new_node #new_node is the new tail 

	def remove(self,node_value):
		prev = None
		x = self.head
		
		while x is not None:
			if x.data == node_value:
				if prev is not None:
					prev.next = x.next
				else:
					self.head = x.next
				break
			else:
				prev = x
				x = x.next

		if x.next is None:
			self.tail = x
		if self.head is None:
			self.tail = None		
	
	def is_empty(self):
		return self.head is None


	def remove_duplicates_with_buffer(self):
        	letters = {}
        	x = self.head
        	prev = None
        	while x is not None:
            		try:
                		letters[x.data]
                		prev.next = x.next
            		except KeyError:
                		letters[x.data] = True
                		prev = x
            		x = x.next

	def remove_dupli(self):
		ele = {}
		x = self.head
		prev = None
		while x is not None:
			if x.data in ele: #jump if the element is duplicated
				prev.next = x.next
			else:
				ele[x.data]=True # add element to hash table.
				prev = x         # x is the new prev.
			x = x.next 		 # update x 

	def remove_dupli_2(self):
		x = self.head
		runner = x
		while x is not None:
			while runner.next is not None:
				if x.data == runner.next.data:
					runner.next = runner.next.next
				else:
					runner = runner.next
			x = x.next
			runner = x

	



ll = singlellist()
ll.append("F")
ll.append("O")
ll.append("L")
ll.append("L")
ll.append("O")
ll.append("W")
ll.append(" ")
ll.append("U")
ll.append("P")
ll.show()


