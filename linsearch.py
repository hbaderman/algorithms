def doLinSearch(arr,target):
	for i in range(0,len(arr)):
		if(arr[i] == target):
			break

	return i

arr = [1,2,3,4,5,6,7]
target = 4

print(doLinSearch(arr,target))