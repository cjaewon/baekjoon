"""
투 포인트로 해결한 문제였다.

처음에는 end -= 1을 해주는 while 문안에 최소 판정하는 코드를 넣지 않고
for 문에만 넣어서 틀려서 while 문에도 추가 후 다시 제출했다.
"""

n = int(input())
data = sorted(map(int, input().split()))

end = len(data) - 1
min = data[0] + data[1]
pos = [data[0], data[1]]

for start in range(len(data)):
  if start >= end:
    break

  if data[start] + data[end] == 0:
    pos = [data[start], data[end]]
    break

  while end > start + 1 and 0 < data[start] + data[end]:
    if abs(data[start] + data[end]) < abs(min):
        min = data[start] + data[end]
        pos = [data[start], data[end]]
    
    end -= 1

  if abs(data[start] + data[end]) < abs(min):
    min = data[start] + data[end]
    pos = [data[start], data[end]]
print(*pos)