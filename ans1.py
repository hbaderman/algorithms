
bmp = [[0,0,0,0,1],[0,0,1,0,1],[0,1,1,0,0],[0,0,0,0,1],[0,0,1,1,1],[0,0,1,1,1],[0,0,0,0,0],[0,0,1,1,1],[0,0,1,0,0]]
(size_x,size_y) = (len(bmp[0])-1,len(bmp)-1)

def printBmp(bmp):
	print("  ".join([str(x) for x in range(0,size_x+1)]))
	count = 0
	for row in bmp:
		print("{0} {1}".format(row, count))
		count += 1

printBmp(bmp)

ccCount = list()
num = 2
alreadyVisited = set()

def getNeighbours(x,y):
	neighbours = []
	for n in [(x,y-1), (x+1,y+1), (x+1, y), (x+1, y-1), (x,y+1), (x-1,y-1), (x-1, y), (x-1, y+1)]:
		if(((n[0] <= size_x and n[1] <= size_y) and (n[0] >= 0 and n[1] >= 0))):
			    neighbours.append(n)
	return neighbours

def findCC(x,y,num):
	print("checking connected components at location {0},{1}".format(x,y))
	neighbours = getNeighbours(x,y)
	print("neighbours are {0}".format(neighbours))
	visitedPositiveNeighbours = set()

	for n in [n for n in neighbours if(bmp[n[1]][n[0]] == 1)]:
		print("found a positive neighbour of ({0},{1}) at {2}".format(x,y,(n[0],n[1])))
		visitedPositiveNeighbours.add((n[0],n[1]))
		if ((n[0],n[1]) not in alreadyVisited):
			bmp[n[1]][n[0]] = num
			alreadyVisited.add((n[0],n[1]))

			print("adding {0},{1} to already visited\nvisited {2}".format(n[0],n[1],alreadyVisited))
			return findCC(n[0],n[1],num)


	print("visited positive neighbours: ")
	print(visitedPositiveNeighbours)
	if (visitedPositiveNeighbours.issubset(alreadyVisited)):
		ccCount.append(1)

for y in range(0,len(bmp)):
	for x in range(0,len(bmp[y])):
		if (bmp[y][x] == 1 and (x,y) not in alreadyVisited):
			print("--------------------------------------------------------------------------")
			printBmp(bmp)
			num += 1
			print("connected component system number: {0}".format(num))
			bmp[y][x] = num
			alreadyVisited.add((x,y))
			print("found a positive at {0},{1} \nadding it to list of already visited positives {2}".format(x,y, alreadyVisited))
			findCC(x,y,num)

largest = [0]*(num+1)
for y in range(0,len(bmp)):
	for x in range(0,len(bmp[y])):
		if (bmp[y][x] != 0):
			largest[bmp[y][x]] += 1
printBmp(bmp)

print("largest connected components system: {0}".format(max(largest)))


print("connected components: {0}".format(len(ccCount)))
