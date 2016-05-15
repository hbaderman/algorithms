# binary search

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

num = 73

def binarySearch(arr,num):
	_min = 0
	_max = len(arr) - 1
	guess = (_min + _max) // 2
	if (arr[guess] == num):
		return guess
	else:
		while ( arr[guess] != num ):
			if (arr[guess] < num):
				_min += 1
			else:
				_max = guess - 1
			guess = (_min + _max) // 2
		return guess



print("location of num ({0}) is position {1} in array".format(num, binarySearch(primes,num)))