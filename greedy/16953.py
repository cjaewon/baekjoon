"""
A -> B 로 가는게 아닌 B -> A 로 가게하여 B 에서 1을 빼꺼나 2을 나누는 방식으로 진행한다.
B -> A 가 불가능 한 경우 혹은 a > b 일 경우에는 -1 을 출력하면 된다.
"""

a, b = map(int, input().split())
count = 0

while True:
  if a == b or a > b:
    if a > b:
      count = -1
    break

  if b % 2 == 0:
    b /= 2
  elif b % 10 == 1:
    b = b // 10
  else:
    count = -1
    break
  count += 1

print(-1 if count == -1 else count + 1)