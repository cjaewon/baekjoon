"""
range(start, stop, step)
- start : list 시작
- stop : list 끝
- step : 증가값

을 의미한다. 증가값을 넣어주어야지 시간초과가 뜨지 않는다.
"""

m, n = map(int, input().split())
sieve = [i for i in range(1, n + 1)]

sieve[0] = -1

for i in range(1, int(n ** 0.5) + 1):
  if sieve[i] != -1:
    for j in range(i, n, sieve[i]):
      if sieve[j] % sieve[i] == 0 and i != j:
        sieve[j] = -1

for i in filter(lambda k: m <= k <= n, sieve):
  print(i)