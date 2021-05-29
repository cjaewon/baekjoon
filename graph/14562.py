from collections import deque

def solve(s, t):
  q = deque()
  q.append((s, t, 0))
    
  while q:
    curr, nt, cost = q.popleft()
      
    if curr == nt:
      print(cost)
      break
    
    if curr * 2 <= nt + 3:
      q.append((curr * 2, nt + 3, cost + 1))
    if curr + 1 <= nt:
      q.append((curr + 1, nt, cost + 1))
        
for i in range(int(input())):
  s, t = map(int, input().split())
  solve(s, t)
    