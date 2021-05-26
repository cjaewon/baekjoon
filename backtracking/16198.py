n = int(input())
w = list(map(int, input().split()))

max = 0

def back(arr, sum):
  global max

  if 2 >= len(arr):
    if max < sum:
      max = sum
    return

  for i in range(1, len(arr) - 1):
    new = []
    for j in range(len(arr)):
      if j != i:
        new.append(arr[j])
    back(new, sum + arr[i - 1] * arr[i + 1])

back(w, 0)
print(max)