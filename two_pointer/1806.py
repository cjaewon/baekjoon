N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0

con_sum = arr[start]
min_len = float("inf")

while start <= end:
  if con_sum < S:
    if end < len(arr) - 1:
      end += 1
      con_sum += arr[end]
    else:
      break
  else: # con_sum >= S:
    min_len = min(min_len, end - start + 1)
    con_sum -= arr[start]
    start += 1

if min_len == float("inf"):
  print(0)
else:
  print(min_len)