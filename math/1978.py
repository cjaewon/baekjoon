import math

n = int(input())
data = list(map(int, input().split()))

sieve = [i for i in range(1, max(data) + 1)]
sieve[0] = -1

for i in range(1, int(math.sqrt(len(sieve)))):
  if sieve[i] == -1:
    continue
  for j in range(i + 1, len(sieve)):
    if sieve[j] % sieve[i] == 0:
      sieve[j] = -1


print(len(list(filter(lambda n: sieve[n - 1] != -1, data))))


