import primes, lists

num = 600851475143
primeFactors = []
currNum = num/primes.findPrimeFactor(num)
primeFactors.append(primes.findPrimeFactor(num))
while primes.isComposite(currNum):
	currNum = currNum/primes.findPrimeFactor(currNum)
	primeFactors.append(primes.findPrimeFactor(currNum))

print primeFactors

print "The largest prime factor is:\n%s" % (primeFactors[len(primeFactors) - 1])
