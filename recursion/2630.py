n = int(input())
paper = [list(map(int, input().split())) for i in range(n)]

white = 0
blue = 0

def r(x1, y1, x2, y2, n): # startx, starty, endx, endy
  global white, blue
  s = 0

  # print(x1, y1, x2, y2, "//", white, blue)

  # if x1 == x2 and y1 == y2:
  #   if paper[y1][x1] == 0:
  #     white += 1
  #   else:
  #     blue += 1
  #   return

  for i in range(y1, y2 + 1):
    for j in range(x1, x2 + 1):
      s += paper[i][j] 

  if s == 0:
    white += 1
    return
  elif s == (x2 - x1 + 1) * (y2 - y1 + 1):
    blue += 1
    return

  r(x1, y1, x2 - n // 2, y2 - n // 2, n // 2)
  r(x2 - n // 2 + 1, y2 - n // 2 + 1, x2, y2, n // 2)
  r(x2 - n // 2 + 1, y1, x2, y2 - n // 2, n // 2)
  r(x1, y2 - n // 2 + 1, x2 - n // 2, y2, n // 2)

r(0, 0, n - 1, n - 1, n)

print(white)
print(blue)