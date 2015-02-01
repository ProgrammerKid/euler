import lists

divisors = lists.numbersInRange(1, 20)
testing = 2520

while 1:
	numberWorks = True
	for num in divisors:
		if testing % num != 0 and numberWorks:
			numberWorks = False

		print str(testing) + "\t" + str(num)
	if numberWorks:
		break
	else:
		testing = testing + 1

print testing
