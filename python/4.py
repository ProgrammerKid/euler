import palindromes, lists

set1 = lists.numbersInRange(100, 999)
set2 = set1
palindromeList = []
for num1 in set1:
	for num2 in set2:
		if palindromes.isPalindrome(num1 * num2):
			palindromeList.append(num1 * num2)
palindromeList = lists.clearRepeats(palindromeList)
palindromeList = lists.sortList(palindromeList)
print palindromeList[len(palindromeList) - 1]
