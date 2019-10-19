def isPalindrome(string):
	# # O(n^2) time | O(n) space
	# reversedString = ""
	# for i in reversed(range(len(string))):
	# 	reversedString += string[i]
	# return string == reversedString

	# O(n) time | O(1) space
	leftIdx = 0
	rightIdx = len(string) - 1
	while leftIdx < rightIdx:
		if string[leftIdx] != string[rightIdx]:
			return False
		leftIdx += 1
		rightIdx -= 1
	return True
