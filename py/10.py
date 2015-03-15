import primes, os

sum = 0
for i in range(0, 2000000):
	if i % 2 == 1 and primes.isPrime(i):
		sum = sum + i
	print(i)

os.system("clear")
print(sum)
