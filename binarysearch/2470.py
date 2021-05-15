n = int(input())
data = map(int, input().split())

data = sorted(data)
near = []

def binarysearch(start, end, d):
  mid = (start + end) // 2

  if start > end:
    return None
  
  if data[mid] == d:
    if data[mid] + d > 0:
      return binarysearch(start, mid - 1, d)
    else:
      return binarysearch(mid + 1, end, d)
  elif data[mid] + d > 0:
    near.append((data[mid], data[mid] + d))
    return binarysearch(start, mid - 1, d)
  elif data[mid] + d < 0:
    near.append((data[mid], data[mid] + d))
    return binarysearch(mid + 1, end, d)
  else:
    print(min(data[mid], d), max(data[mid], d))
    exit()

for d in data:
  binarysearch(0, len(data) - 1, d)

m = min(near, key=lambda n: abs(n[1]))
print(min(m[0], m[1] - m[0]), max(m[0], m[1] - m[0]))