# implement swap
arr = [22, 11, 99, 88, 9, 7, 42]

def swap(arr, first, second):
	temp = arr[first]
	arr[first] = arr[second]
	arr[second] = temp
	return arr

def findMinimumIndex(arr,startAt):
	minValue = arr[startAt]
	minIndex = startAt
	for i in range(startAt+1, len(arr)):
		if (arr[i] < minValue):
			minIndex = i
			minValue = arr[i]
	return minIndex


def selectionSort(arr):
	for i in range(0, len(arr)-1):
		smallestIndex = findMinimumIndex(arr,i)
		arr = swap(arr,i, smallestIndex)
	return arr





print(arr)
sorted_ = selectionSort(arr)
assert(sorted_ == [7, 9, 11, 22, 42, 88, 99])
print(sorted_)