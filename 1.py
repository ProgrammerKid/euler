currNum = 1
sums = 0

while currNum < 1000:
	if not currNum % 3 or not currNum % 5:
		sums = sums + currNum;
	currNum = currNum + 1

print sums
