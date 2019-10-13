def binarySearch(array, target):
	l=0
	r=len(array)-1
	while l <= r:
		m = (l+r) // 2
		if array[m] == target:
			return m
		elif array[m] < target:
			l = m+1
		else:
			r = m-1

	return -1
