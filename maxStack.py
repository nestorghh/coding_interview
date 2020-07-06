class minStack:
	def __init__(self):
		self.items=[]
		self.aux=[]
	
	def push(self,x):
		self.items.append(x)
		#update aux stack
		self.getMinPush()

	def pop(self):
		e = self.items.pop()
		#update aux stack
		self.getMinPop(e)
		return e

	def size(self):
		return len(self.items)

	def getMinPush(self):
		if len(self.items)==1 and len(self.aux)==0:
			self.aux.append(self.items[-1])
		if self.items[-1]<self.aux[-1]:
			self.aux.append(self.items[-1])	
			
	def getMinPop(self,e):
		if e == self.aux[-1]:
			self.aux.pop()

	def getMin(self):
		if len(self.items)!=0:
			return self.aux[-1]
		else:
			return []


	def __repr__(self):
		return str(self.items)


class maxStack:
    def __init__(self):
        self.items=[]
        self.aux=[]
    
    def push(self,e):
        self.items.append(e)
        #update aux stack accordingly
        self.getMaxPush()

    def pop(self):
        e = self.items.pop()
        #update aux stack accordingly
        self.getMaxPop(e)

    def size(self):
        return len(self.items)
        
    def getMaxPush(self):
        if len(self.items)==1 and len(self.aux)==0:
            self.aux.append(self.items[-1])
        if self.items[-1] > self.aux[-1]:
            self.aux.append(self.items[-1])

    def getMaxPop(self,e):
        if e == self.aux[-1]:
            self.aux.pop()

    def getMax(self):
        if len(self.items)==0:
            return []
        else:
            return self.aux[-1]

    def __repr__(self):
        return str(self.items)
    

