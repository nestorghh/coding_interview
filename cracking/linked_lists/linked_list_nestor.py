class node:
	def __init__(self,data,next):
		self.data=data
		self.next=next

class singlelist:
	head=None
	tail=None

	def append(self,data):
		new_node = node(data,None)
		if self.head is None:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
	
	def show(self):
		x = self.head
		while x is not None:
			print(x.data, end='')
			print('===>', end='')
			x = x.next
		print(None)


	def remove(self, node_value):
		x = self.head
		prev = None

		while x is not None:
			if x.data == node_value:
				if prev is None: #x is the head
					self.head = x.next
				else: # x is not the head
					prev.next = x.next
				break
			prev = x # move prev
			x = x.next # move x

		if x.next is None:  # update tail
			self.tail = x
		if self.head is None: # update head
			self.tail = None
				

	def remove_duplicates(self):
		ele = {}
		x = self.head
		prev = None
		
		while x is not None:
			if x.data in ele:
				prev.next = x.next
			else:
				ele[x.data]=True
				prev = x

			x = x.next
	
	def remove_duplicates_2(self):
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


	def find_k(self,k):
		p1 = self.head
		p2 = self.head
		count=0

		#move p2 k positions ahead		
		while count!=k:
			count += 1
			p2 = p2.next
			#if p2 is None:
			#	return None
		# move both pointers
		while p2.next is not None:
			p1 = p1.next
			p2 = p2.next

		return p1.data

	
	def partition_inplace(self,val):
		prev = None
		x = self.head
		while x:
			if prev and x.data<val:
				prev.next = x.next
				x.next = self.head
				self.head = x
				x = prev.next
			else:
				prev = x
				x = x.next	


def sum_lists_recursevely(h1, h2, carry):
    result = node(0,0)
    if h1 is None and h2 is None and carry == 0:
        return None
    val = carry
    if h1 is not None:
        val += h1.data
        h1 = h1.next
    if h2 is not None:
        val += h2.data
        h2 = h2.next
    carry = val // 10
    result.data = val % 10
    result.next = sum_lists_recursevely(h1, h2, carry)
    return result





#def partition(head,val):
#	prev = None
#	x = head
#	while x:
#		if prev and x.data < val:
#			prev.next = x.next
#			x.next = head
#			head= x
#			x = prev.next
#		else:
#			prev = x
#			x = x.next
#	return head


def print_ll(node):
    while node:
        print(node.data, "-> ", end='')
        node = node.next
    print(None)


	#def partition_nestor(self,val):
	#	x = self.head
	#	t = self.tail
	#	
	#	while x is not None:
	#		n = x.next
	#		if x.data < val:
	#			x.next = self.head
	#			self.head = x
	#		else:
	#			self.tail.next = x
	#			self.tail = x
	#		x = n
	#	self.tail.next = None


	
ll1 = singlelist()
ll1.append(7)
ll1.append(8)
ll1.append(2)
ll2 = singlelist()
ll2.append(4)
ll2.append(3)
ll2.append(8)
print_ll(sum_lists_recursevely(ll1.head, ll2.head, 0))



#ll=singlelist()
#ll.append('N')
#ll.append('E') 
#ll.append('S')
#ll.append('T')
#ll.append('O')
#ll.append('R')
#ll.append('N')
#ll.append('E')

#ll.show()

#ll.remove_duplicates()

#ll=singlelist() 
#ll.append(3)
#ll.append(5)
#ll.append(8)
#ll.append(5)
#ll.append(10)
#ll.append(2)
#ll.append(1)
#print(ll)
#head = partition(ll.head, 5)
#print_ll(head)



#ll.show()
#print('after partition')
#ll.partition_nestor(5)
#ll.show()

