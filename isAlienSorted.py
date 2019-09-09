def isAlienSorted(words,order):

	orderMap = {c:i for i,c in enumerate(order)}

	for w1, w2 in zip(words,words[1:]):
		if len(w1) > len(w2) and w1[:len(w2)]==w2:
			return False
		for c1, c2 in zip(w1,w2):
			print(c1,c2)
			if orderMap[c1]>orderMap[c2]:
				print('here')
				print(c1,c2)
				return False
			elif orderMap[c1] < orderMap[c2]:
				print('there')
				print(c1,c2)
				break
	return True	
