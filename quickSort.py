# time | space complexity:
# Best: O(nlogn) | O(logn)
# Avg: O(nlog) | O(logn)
# Worst: O(n^2) | O(logn)

def quickSort(array):
	quickSortHelper(array ,0 ,len(array)-1)
	return array

def quickSortHelper(array, startIdx, endIdx):
	if startIdx >= endIdx:
		return
	pivot = startIdx
	leftIdx = startIdx + 1
	rightIdx = endIdx
	while rightIdx >= leftIdx:
		if array[leftIdx] > array[pivot] and array[rightIdx] < array[pivot]:
			swap(leftIdx, rightIdx, array)
		if array[leftIdx] <= array[pivot]:
			leftIdx +=1
		if array[rightIdx] >= array[pivot]:
			rightIdx -=1
	swap(pivot, rightIdx, array)
	isLeftSubArraySmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
	if isLeftSubArraySmaller:
		quickSortHelper(array, startIdx, rightIdx -1)
		quickSortHelper(array, rightIdx + 1, endIdx)
	else:
		quickSortHelper(array, rightIdx + 1, endIdx)
		quickSortHelper(array, startIdx, rightIdx -1)

def swap(a,b, array):
	array[a], array[b] = array[b], array[a]
