import lists

def part1():
	numbers = lists.numbersInRange(1, 100)
	sums = 0
	for num in numbers:
		sums = sums + num ** 2
	return sums

def part2():
	sums = lists.add(lists.numbersInRange(1, 100))
	sums = sums ** 2
	return sums

print part2() - part1()
