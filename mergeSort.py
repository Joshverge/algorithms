# O(nlogn) time | O(nlogn) space

def mergeSort(array):
    # Write your code here.
	if len(array) == 1:
		return array
	middleIdx = len(array) // 2
	lh = array[:middleIdx]
	rh = array[middleIdx:]
	return mergeSortA(mergeSort(lh), mergeSort(rh))

def mergeSortA(lh, rh):
	sArray = [None]*(len(lh) + len(rh))
	k = i = j = 0
	while i < len(lh) and j < len(rh):
		if lh[i] <= rh[j]:
			sArray[k] = lh[i]
			i += 1
		else:
			sArray[k] = rh[j]
			j += 1
		k +=1
	while i < len(lh):
		sArray[k] = lh[i]
		i +=1
		k +=1
	while j < len(rh):
		sArray[k] = rh[j]
		j += 1
		k += 1
	return sArray
