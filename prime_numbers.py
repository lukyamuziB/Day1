
def prime(a):
	if not isinstance(a, (int,float )):
		raise TypeError("the limit has to be a number")
	if a < 2:
		raise ValueError("Sorry, the lowest prime number is 2")
	result = []
	if a is 2:
		return [a]

	#since the prime even number is 2, we only look at odd numbers
	for number in range(3,a,2):
		if a < 9:
			result.append(number)
		if ((a//2 != 0)and(a//3 != 0) and (a//5 != 0) and (a//5 != 0) and (a//7 != 0)):
			result.append(number)
	return result
