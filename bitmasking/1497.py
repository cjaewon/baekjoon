from collections import deque

N, M = map(int, input().split()) # N: 기타의 개수, M: 곡의 개수
guitar = [0 for i in range(N)]


for i in range(N):
  _, available = input().split()
  available_bit = 0

  for j, yes_or_no in enumerate(reversed(available)):
    if yes_or_no == "Y":
      available_bit += 2 ** j
    else:
      pass
    
  guitar[i] = available_bit


stack = deque([(i, 0, 0, 0) for i in range(N)]) 
max_cnt = 0
min_cnt = 2e9

while stack:
  curr = stack.pop()
  i, context, visited, cnt = curr

  context |= guitar[i]
  
  if max_cnt <= bin(context).count('1') and context != 0:
    if max_cnt == bin(context).count('1'):
      min_cnt = min(min_cnt, cnt + 1)
    else:
      max_cnt = bin(context).count('1')
      min_cnt = cnt + 1

  for j in range(N):
    if not (visited & (1 << N-1-j)):
      visited |= 1 << N-1-j
      stack.append((j, context, visited, cnt + 1))

print(min_cnt if min_cnt != 2e9 else -1)


  