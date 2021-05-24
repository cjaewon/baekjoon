n = int(input())
data = sorted(map(int, input().split()))

end = len(data) - 1
min = data[0] + data[1] + data[2]
pos = [data[0], data[1], data[2]]

for n in data:
  end = len(data) - 1

  for start in range(len(data)):
    if start >= end:
      break
    
    if data[start] == n:
      continue

    if data[end] == n:
      if end > start + 1:
        end -= 1
      else:
        continue

    if data[start] + data[end] + n == 0:
      pos = [data[start], data[end], n]
      break


    while end > start + 1 and 0 < data[start] + data[end] + n:
      if data[end] != data[start] and data[start] != n and data[end] != n and abs(data[start] + data[end] + n) < abs(min):
        min = data[start] + data[end] + n
        pos = [data[start], data[end], n]
      
      end -= 1

      if data[end] == n and end > start + 1:
        end -= 1

    if data[end] != data[start] and data[start] != n and data[end] != n and abs(data[start] + data[end] + n) < abs(min):
      min = data[start] + data[end] + n
      pos = [data[start], data[end], n]

print(*sorted(pos))