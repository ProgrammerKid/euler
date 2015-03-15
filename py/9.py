import math

breakout = False

for a in range(1, 1000):
	for b in range(1, 1000):
		c_2 = ((a)**2) + ((b)**2)
		c = math.sqrt(c_2)

		if a + b + c == 1000:
			print("a = %d\nb = %d\nc = %d" % (a, b, c))
			breakout = True

		if breakout:
			break
	
	if breakout:
		break

print(a*b*c)
