# insertion sort

def insert(arr, rightIndex, value):
	for i in reversed(range(0,len(arr[:rightIndex+1]))):
		if (arr[i] > value):
			temp = arr[i]
			arr[i] = value
			arr[i+1] = temp
	return arr

def insertionSort(arr):




array = [3, 5, 7, 11, 13, 2, 9, 6]
test1 = insert(array, 4, 2)
assert(test1 == [2, 3, 5, 7, 11, 13, 9, 6])
test2 = insert(array, 5, 9)
assert(test2 == [2, 3, 5, 7, 9, 11, 13, 6])
test3 = insert(array, 6, 6)
assert(test3 == [2, 3, 5, 6, 7, 9, 11, 13])