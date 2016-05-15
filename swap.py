# implement swap
arr = [4,9,7,10,4,3,5,129,23]

def findSmallest(arr):
	smallest = arr[0]
	for i in range(0,len(arr)):
		if ( arr[i] < smallest):
			smallest = arr[i]
	return smallest
def selectionSort(arr):
	smallest = findSmallest(arr)
	secondSmallest = secondSmallest(arr,smallest)


_sorted = selectionSort(arr)
print(_sorted)