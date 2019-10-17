def getNthFib(n):
    # Write your code here.
	lastTwo = [0 , 1]
	counter = 3
	while counter <= n:
		nextFib = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextFib
		counter += 1
	return lastTwo[1] if n > 1 else 0


# def getNthFib(n, memorize = {1: 0, 2: 1}):
	# if n in memorize:
	# 	return memorize[n]
	# else:
	# 	memorize[n] = getNthFib(n -1, memorize) + getNthFib(n-2, memorize)
	# 	return memorize[n]


	# if n == 0:
	# 	return False
	# if n == 1:
	# 	return 0
	# if n == 2:
	# 	return 1
	# else:
	# 	return getNthFib(n-1) + getNthFib(n-2)
