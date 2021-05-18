"""
처음에는 start = 0, end = len(computures) - 1 로 잡았다.
그리고 mid를 computures의 인덱스로 잡았다. 이렇게 하면 예제에서는 잘 작동하지만 (1, 5) 를 넣었을때는 5가 출력된다.
그래서 computures[mid] 를 바탕으로 이분탐색을 하는 것이 아닌 start = 0, end = sum(computures) 로 잡고
mid 또한 분으로 잡았더니 해결할 수 있었다.

python3으로 제출시 시간초과가 나서 PyPy로 다시 제출하니 해결됐다.
"""

n = int(input())
computures = []


for i in range(n):
  computures = computures + list(map(int, input().split(" ")))

computures = sorted(computures)

start = 0
end = computures[-1]
half = sum(computures) / 2
near = []

while start <= end:
  mid = (start + end) // 2
  s = 0

  for i in range(n * n):
    if computures[i] >= mid:
      s += mid * (n * n - i)
      break
    s += computures[i]

  if half > s:
    start = mid + 1
  elif half < s:
    end = mid - 1
    near.append((s, mid))
  else:
    near.append((s, mid))
    break

print(min(near, key=lambda n: n[0])[1])