from collections import deque

n, k = map(int, input().split(" "))
checked = {}
q = deque()

q.append((n, 0))

while True:
  cur = q.popleft()

  if cur[0] == k:
    print(cur[1])
    break

  if cur[0] >= 200000:
    continue

  if not (cur[0] + 1 in checked):
    q.append((cur[0] + 1, cur[1] + 1))

  if not (cur[0] - 1 in checked):
    q.append((cur[0] - 1, cur[1] + 1))

  if not (cur[0] * 2 in checked):
    q.append((cur[0] * 2, cur[1] + 1))

  checked[cur[0] + 1] = True
  checked[cur[0] - 1] = True
  checked[cur[0] * 2] = True