def multOf(number, lessThan):
	currNumber = number
	multiples = []
	while(currNumber < lessThan):
		multiples.append(currNumber)
		currNumber = currNumber + number
	return multiples
