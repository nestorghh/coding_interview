class MedianFinder(object):
	def __init__(self):
		self.arr = []
		self.freq = {}
		self.ordered = False
		self.maxi = -1

	def addNum(self,num):
		self.ordered = False
		try:
			self.freq[num] += 1
		except:
			self.freq[num] = 1	

	def dummy():

		if len(self.arr) == 0:
			self.arr += [num]
			return
		count = 0
		for i in self.arr:
			if i < num:
				count += 1
				continue
			else:
				break
		self.arr = self.arr[:count] + [num] + self.arr[count:]
	
	def findMedian(self):

		if self.ordered:
			r = len(self.arr)
			if r == 1:
				return self.arr[0]
			if r == 2:
				return (self.arr[0] + self.arr[1] ) / 2 

			if r % 2 == 0:
				return (self.arr[r//2-1] + self.arr[r//2])/2
			else:
				return self.arr[r//2]
		
		count = 0
		self.arr = []
		for key in sorted(self.freq):
			self.arr += [key]*self.freq[key]
		self.ordered = True

		return self.findMedian()



