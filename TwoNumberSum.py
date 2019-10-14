def twoNumberSum(array, targetSum):

# Solution 1
"""
def twoNumberSum(array, targetSum):
	for i in range(len(array) - 1):
		for j in range(i + 1, len(array)):
			firstNum = array[i]
			secondNum = array[j]
			currentSum = firstNum + secondNum
			if currentSum == targetSum:
				return sorted([firstNum, secondNum])
	return []
"""
# Solution 2

def twoNumberSum(array, targetSum):
	Nums = {}
	for Num in array:
		potentialSum = targetSum - Num
		if potentialSum in Nums:
			return sorted([Num, potentialSum])
		else:
			Nums[Num] = True
	return []


# Solution 3
"""
def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array)-1
	while left <= right:
		currentSum = array[left] + array[right]
		if currentSum == targetSum:
			return [array[left], array[right]]
		elif currentSum < targetSum:
			left +=1
		else:
			right-=1
	return []

"""

# Naive first solution
"""
def twoNumberSum(array, targetSum):
    # Write your code here.
	for p in range(0,len(array)):
		for q in range(0,len(array)):
			if p != q:
				i = array[p]
				j = array[q]
				if i+j == targetSum:
					a = 0
					b = 0
					if i > j:
						a = j
						b = i
					else:
						a = i
						b = j

					return [a, b]
	return []
"""
