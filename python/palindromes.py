import lists
def isPalindrome(num):
	num = str(num)
	length = len(num)
	
	if length % 2 == 0: #if the length of the number is even
		half = length/2 + 1
		half1 = num[0:half - 1]
		half2 = num[half - 1:length]
	elif length % 2 == 1:
		half = ((length - 1)/2)
		half1 = num[0:half]
		half2 = num[half + 1:length]
	half1 = lists.toList(half1)
	half2 = lists.toList(half2)
	
	half2 = lists.invertList(half2)
	if half1 == half2:
		return True
	else:
		return False
