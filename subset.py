#Given a set of distinct integers, nums, return all possible subsets (the power set).

def power_set_2(set_):
    subsets = [[]]
    for element in set_:
	print('this is element '+ element)
        for ind in xrange(len(subsets)):
		 print(xrange(len(subsets)))
		 subsets.append(subsets[ind] + [element])
		 print(subsets)
    return subsets

print(power_set_2(['a','b','c']))



