#find the average length of word in sentence

def average_length_word(sentence):
	words=sentence.split()
	return sum([len(w) for w in words])/len(words)


print(average_length_word('Hi my name is Nestor Gabriel and I leetcode all the way'))

