"""
먼저 이 문제를 풀기위해서는 에라토스테네스의 체를 이용하여 9999까지의 소수들을 모두 구한 후
bfs를 이용하여 가능한 모든 소수들을 탐색하는 도중에 가장 회수가 적은 것을 찾는다.

((prime // 10 ** i) * 10 ** i + int((prime % 10 ** (i - 1)))) + j * 10 ** (i - 1) 이 식을 도출하는 과정이 어려웠는데
이 식은 i = 1 # 치환 할 자릿수 j = 9 # 치환 될 수로 만들었다.

그러다가 j = 0 일때를 고려하지 않아서 틀렸었는데 범위를 수정하고
if i == 4 and j == 0:
  continue 
를 추가하여 해결했다.
"""

from collections import deque

t = int(input())
data = []

for i in range(t):
  a, b = map(int, input().split())
  data.append((a, b))

m = 9999

sieve = [i for i in range(1, m + 1)]
visted = [0 for i in range(m)]
sieve[0] = -1

for i in range(int(m ** 0.5) + 1):
  if sieve[i] != -1:
    for j in range(i + sieve[i], m, sieve[i]):
      sieve[j] = -1

primes = list(filter(lambda n: n != -1, sieve))

def solve(a, b):
  global visted

  q = deque()

  q.append((a, 0))

  while q:
    prime, cost = q.popleft()
    
    if prime == b:
      return cost

    for i in range(1, 5): # 3 -> 1
      for j in range(0, 10): # 1 -> 9
        if i == 4 and j == 0:
          continue

        result = ((prime // 10 ** i) * 10 ** i + int((prime % 10 ** (i - 1)))) + j * 10 ** (i - 1)

        if sieve[result - 1] != -1 and result != prime and not visted[result - 1]:
          q.append((result, cost + 1))
          visted[result - 1] = 1
  return "Impossible"

for d in data:
  print(solve(d[0], d[1]))
  visted = [0 for i in range(m)]