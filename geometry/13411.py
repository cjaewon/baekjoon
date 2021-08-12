n = int(input())
arr = []

for i in range(n):
  x, y, v = map(int, input().split())
  arr.append((((x ** 2 + y ** 2) ** 0.5 / v), i + 1))

arr = sorted(arr)

for v in arr:
  print(v[1])