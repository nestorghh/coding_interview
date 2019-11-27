def FizzBuzz():
	for n in range(101):
		if n%15==0:
			print('FizzBuzz\n')
		elif n%3==0:
			print('Fizz\n')
		elif n%5==0:
			print('Buzz\n')
		else:
			print(str(n)+'\n')


