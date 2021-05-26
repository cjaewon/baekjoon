n= int(input())
result = []
count = 0

result.append(0)

def back(num):
  global count

  result.append(num)

  for i in range(0, num % 10):
    if len(str(num)) == 0 and i == 0:
      continue
      
    back(num * 10 + i)

for i in range(1, 10):
  back(i)

result = sorted(result)

if len(result) <= n:
  print("-1")
  exit()

print(result[n])

