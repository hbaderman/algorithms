def printBmp(bmp):
	for row in bmp:
		print(row)

bmp = [[0,0,0,0,1],[0,0,1,0,1],[0,1,1,0,0],[0,0,0,0,1],[0,0,1,1,1],[0,0,1,1,1],[0,0,0,0,0],[0,0,1,1,1],[0,0,1,0,0]]

printBmp(bmp)


size_x = 4
size_y = 8

ccCount = list()

alreadyVisited = set()

def getNeighbours(x,y):
	neighbours = []
	for n in [(x,y+1), (x+1,y+1), (x+1, y), (x+1, y-1), (x,y-1), (x-1,y-1), (x-1, y), (x-1, y+1)]:
		if(((n[0] <= size_x and n[1] <= size_y) and (n[0] >= 0 and n[1] >= 0))):
			    neighbours.append(n)
	return neighbours

def findCC(x,y):
	neighbours = getNeighbours(x,y)
	visitedPositiveNeighbours = set()
	for n in neighbours:
		if (bmp[n[1]][n[0]] == 1):
			visitedPositiveNeighbours.add((n[0],n[1]))
			if ((n[0],n[1]) not in alreadyVisited):
				alreadyVisited.add((n[0],n[1]))
				return findCC(n[0],n[1])
	if (visitedPositiveNeighbours.issubset(alreadyVisited)):
		ccCount.append(1)

for y in range(0,len(bmp)):
	for x in range(0,len(bmp[y])):
		if (bmp[y][x] == 1 and (x,y) not in alreadyVisited):
			alreadyVisited.add((x,y))
			findCC(x,y)


print("connected components: {0}".format(len(ccCount)))
