"""
처음에 리스트에 다녀간 좌표를 추가하는 방식으로 작성하였는데 시간 초과가 발생하여서
배열로 변경해주므로써 해결했다.
"""

n = int(input())
count = 0

used = [[0 for i in range(n)] for i in range(n)]

def back(curr):
  global used, count

  if curr == n:
    count += 1
    return
  
  for i in range(n):
    if used[curr][i] >= 1:
      continue

    for j in range(0, n):
      if curr <= j:
        used[j][i] += 1
      if j + curr < n and j + i < n:
        used[j + curr][j + i] += 1
      if j + curr < n and i - j >= 0:
        used[j + curr][i - j] += 1

    back(curr + 1)

    for j in range(0, n):
      if curr <= j:
        used[j][i] -= 1
      if j + curr < n and j + i < n:
        used[j + curr][j + i] -= 1
      if j + curr < n and i - j >= 0:
        used[j + curr][i - j] -= 1

back(0)

print(count)