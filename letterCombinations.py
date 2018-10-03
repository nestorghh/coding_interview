#Given a string containing digits from 2-9 inclusive, 
#return all possible letter combinations that the number could represent.

#A mapping of digit to letters (just like on the telephone buttons) 
#is given below. Note that 1 does not map to any letters.


mapa = {'1':[''], '2':['a','b','c'], '3':['d','e','f'], '4': ['g','h','i'], '5':['j','k','l'], 
'6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z'], '0':['']
}


def letterCombinations(digits):
	
	if len(digits)==0:
		return []

	f = digits[0]
	result = mapa[f]

	for f in range(1,len(digits)):
		current_result = []

		for k in range(len(result)):

			for j in mapa[digits[f]]:

				current_result.append(result[k]+j)	

		result = current_result

	return result
				
