"""
17103번을 활용해서 풀었다.
"""

data = []

for i in range(int(input())):
  data.append(int(input()))

m = max(data)
sieve = [i for i in range(1, m + 1)]

sieve[0] = -1

for i in range(1, int(sieve[-1] ** 0.5) + 1):
  if sieve[i] != -1:
    for j in range(i, m, sieve[i]):
      if sieve[j] % sieve[i] == 0 and i != j:
        sieve[j] = -1

pnumber = list(filter(lambda n: n != -1, sieve))

for d in data:
  s = []
  for p in pnumber:
    if d - p - 1 < 0:
      break
    if sieve[d - p - 1] != -1:
      if d - p == p:
        print(min(d - p, p), max(p, d - p))
        s = []
        break
      else:
        s.append((d - p - p, d - p, p))
  if len(s) > 0:
    print(" ".join(map(str, sorted(min(s, key=lambda n: abs(n[0]))[1:3]))))