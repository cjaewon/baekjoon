N = int(input())
arr = list(sorted(map(int, input().split())))
good_num_count = 0

for i, val in enumerate(arr):
  left = 0
  right = len(arr) - 1

  if right == i:
    right -= 1
  elif left == i:
    left += 1
    
  while left < right:
    if arr[left] + arr[right] > val:
      right -= 1

      if right == i:
        right -= 1
    elif arr[left] + arr[right] < val:
      left += 1

      if left == i:
        left += 1
    else: # arr[left] + arr[right] == val
      good_num_count += 1
      break

print(good_num_count)