
def prime(limit):
	if not isinstance(limit, (int,float )):
		raise TypeError("the limit has to be a number")
	if limit <= 2:
		raise ValueError("Sorry, the lowest prime number is 2")
	result = []
	if limit is 2:
		return [a]

	#since the only prime even number is 2, we only look at odd numbers
	for number in range(3,limit,2):
	#all odd nummbers bellow 9 are prime
		if limit < 9:
			result.append(number)
	#all odd numbers above 9 must meet these conditions to be prime
		if ((limit//2 != 0)and(limit//3 != 0) and (limit//5 != 0) and (limit//5 != 0) and (limit//7 != 0)):
			result.append(number)
	return result




