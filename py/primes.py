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

def findPrimesTill(maximum):
	primes = []
	for i in range(1, maximum + 1):
		if isPrime(i):
			primes.append(i)
	return primes

def findPrimesAmt(maximum):
	primes = []
	i = 1
	counter = 1
	while(counter <= maximum):
		if isPrime(i):
			primes.append(i)
			counter = counter + 1
		i = i +  1
	return primes
