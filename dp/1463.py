"""
n - 1, n - 2 .. 을 이용해서 n의 값을 어떻게 만들 수 있는지, 즉 n을 n- 1, n - 2 .. 이용해서 구할수는 없는지 생각해보는게 중요한 것 같다.
"""

n = int(input())
table = []

table.append(0) # 0
table.append(0)
table.append(1)
table.append(1)
table.append(2)
table.append(3)
table.append(2) # 6

i = 7

while True:
  if i > n:
    break

  table.append(
    min(
      table[int(i / 3)] + 1 if i % 3 == 0 else n, 
      table[int(i / 2)] + 1 if i % 2 == 0 else n, 
      table[i - 1] + 1
    )
  )

  i += 1

print(table[n])