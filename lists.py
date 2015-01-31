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

def addAll(array):
	sums = 0;
	for element in array:
		sums = sums + element
	return sums
