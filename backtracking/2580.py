graph = [list(map(int, input().split())) for i in range(9)]
points = []
index = 0

for i in range(9):
  for j in range(9):
    if graph[i][j] == 0:
      points.append((i, j))

def print_graph():
  for i in range(9):
    for j in range(9):
      print(graph[i][j], end=" ")
    print()

def back():
  global index

  if index >= len(points):
    print_graph()    
    exit()

  
  isused = [0 for i in range(10)]

  for i in range(9):
    if graph[points[index][0]][i] != 0:
      isused[graph[points[index][0]][i] ] = 1
  
  for i in range(9):
    if graph[i][points[index][1]] != 0:
      isused[graph[i][points[index][1]]] = 1

  starty = points[index][0] // 3 * 3 
  startx = points[index][1] // 3 * 3

  for i in range(3):
    for j in range(3):
      if graph[starty + i][startx + j] != 0:
        isused[graph[starty + i][startx + j]] = 1    

  for i in range(1, 10):
    if not isused[i]:
      graph[points[index][0]][points[index][1]] = i
      index += 1
      back()
      index -= 1
      graph[points[index][0]][points[index][1]] = 0

back()