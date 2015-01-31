def isPrime(num):
	x = 2
	if num == 2:
		return True

	while num/2 >= x:
		if num % x == 0:
			return False
		else:
			x = x + 1
	return True

def isComposite(num):
	if isPrime(num):
		return False
	else:
		return True

def findPrimeFactor(num):
	x = 2
	while(num > x):
		if isPrime(x) and num % x == 0:
			return x
		else:
			x = x + 1
	return x

