n, r, c = map(int, input().split())
# result = [[0 for j in range(2 ** n)] for i in range(2 ** n)]

cnt = 0
def re(x1, y1, x2, y2, k):
  global cnt

  if x1 == x2 and y1 == y2:
    if r == y1 and c == x1:
      print(cnt)
      exit()

    cnt += 1
    return

  # print(x1, y1, x2, y2, "k:", k, "cnt:", cnt)
  if x2 - k // 2 < c or y2 - k // 2 < r:
    cnt += (k // 2) * (k // 2)
  else:
    re(x1, y1, x2 - k // 2, y2 - k // 2, k // 2)

  if c < x2 - k // 2 + 1 or r > y2 - k // 2:
    cnt += (k // 2) * (k // 2)
  else:
    re(x2 - k // 2 + 1, y1, x2, y2 - k // 2, k // 2)

  if c > x2 - k // 2 + 1 or r < y2 - k // 2 + 1:
    cnt += (k // 2) * (k // 2)
  else:
    re(x1, y2 - k // 2 + 1, x2 - k // 2, y2, k // 2)

  re(x2 - k // 2 + 1, y2 - k // 2 + 1, x2, y2, k // 2)

re(0, 0, 2 ** n - 1, 2 ** n - 1, 2 ** n)