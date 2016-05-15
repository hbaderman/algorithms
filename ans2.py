bmp = [[0,0,0,0,1],[0,0,1,0,1],[0,1,1,0,0],[0,0,0,0,1],[0,0,1,1,1],[0,0,1,1,1],[0,0,0,0,0],[0,0,1,1,1],[0,0,1,0,0]]
(size_x,size_y) = (len(bmp[0])-1,len(bmp)-1)


labelList = set()
curlab = 1
q = []

def printBmp(bmp):
	print(" "+"  ".join([str(x) for x in range(0,size_x+1)]))
	count = 0
	for row in bmp:
		print("{0} {1}".format(row, count))
		count += 1

def getNeighbours(x,y):
	neighbours = []
	for n in [(x,y-1), (x+1,y+1), (x+1, y), (x+1, y-1), (x,y+1), (x-1,y-1), (x-1, y), (x-1, y+1)]:
		if(((n[0] <= size_x and n[1] <= size_y) and (n[0] >= 0 and n[1] >= 0))):
			    neighbours.append(n)
	return neighbours


def checkNeighbours(x,y, curlab):
	neighbours = getNeighbours(x,y)
	for n in neighbours:
		if (bmp[n[1]][n[0]] == 1):
			bmp[n[1]][n[0]] = curlab
			checkNeighbours(n[0],n[1],curlab)



for y in range(0,len(bmp)):
	for x in range(0,len(bmp[y])):
		if (bmp[y][x] == 1 and (x,y) not in labelList):
			curlab += 1
			bmp[y][x] = curlab
			checkNeighbours(x,y, curlab)
print(curlab-1)

largest = [0]*(curlab+1)
for y in range(0,len(bmp)):
	for x in range(0,len(bmp[y])):
		if (bmp[y][x] != 0):
			largest[bmp[y][x]] += 1
for y in range(0,len(bmp)):
	for x in range(0,len(bmp[y])):
		if (bmp[y][x] != 0):
			bmp[y][x] -= 1
		else:
			bmp[y][x] = 0
printBmp(bmp)
print(max(largest))


