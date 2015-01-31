def clearRepeats(array):
	used = [0]
	newArray = [0]
	for element in array:
		try:
			if used.index(element) >= 0:
				isUsed = True #placeholder
		except ValueError:
			used.append(element)
			newArray.append(element)
	return newArray

def add(array):
	sums = 0;
	for element in array:
		sums = sums + element
	return sums

def generateFib(till):
	'''
	1, 2, 3, 5, 8, 13
	1  2  3  4  5  6
	'''
	sequence = [1, 2, 3]
	while sequence[len(sequence) - 1] <= till:
		lastNum = sequence[len(sequence) - 1]
		secondToLastNum = sequence[len(sequence) - 2]
		total = lastNum + secondToLastNum
		sequence.append(total)
	#evaluating the sequence
	if sequence[len(sequence) - 1] > till:
		sequence.pop()
	return sequence

def removeOdds(array):
	newArray = []
	for element in array:
		if not element % 2: #if element is even
			newArray.append(element)
	return newArray

def toList(thing):
	thing = str(thing)
	newArray = []
	for char in thing:
		newArray.append(char)
	return newArray

def invertList(array):
	newArray = []
	for thing in array:
		newArray = [thing] + newArray
	return newArray

def numbersInRange(minimum, maximum):
	newArray = []
	counter = minimum
	while counter >= minimum and counter <= maximum:
		newArray.append(counter)
		counter = counter + 1
	return newArray

def sortList(array):
	return sorted(array)
