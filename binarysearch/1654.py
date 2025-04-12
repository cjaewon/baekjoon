K, N = map(int, input().split())
LANs = [int(input()) for _ in range(K)]

start = 0
end = max(LANs)

max_length = None

while start <= end:
  mid = (start + end) // 2

  if mid == 0:
    max_length = 1
    break

  cable_count = sum(map(lambda lan: lan // mid, LANs))

  if cable_count < N:
    end = mid - 1
  elif cable_count >= N:
    start = mid + 1
    max_length = mid

print(max_length)