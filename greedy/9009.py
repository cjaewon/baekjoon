data = []
table = [0, 1]

for i in range(int(input())):
  data.append(int(input()))

m = max(data)
i = 2

while m > table[-1]:
  table.append(table[i - 1] + table[i - 2])
  i += 1

for num in data:
  used = []
  s = 0

  for fibo in reversed(table):
    if fibo == 0:
      pass
    elif fibo <= num and s + fibo <= num:
      s += fibo
      used.append(str(fibo))

      if s == num:
        break
  print(" ".join(reversed(used)))
    
    
