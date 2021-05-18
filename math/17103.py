"""
처음에는 두 소수의 합이 입력받은 숫자가 되기 위해서 3중 for문을 사용했다.
하지만 시간초과가 났기 때문에 배열에 바로 접근하는 방식을 선택해서 2중 for문으로 제출하니깐 해결할 수 있었다. 
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
  count = 0
  for p in pnumber:
    if d - p - 1 < 0:
      break
    if sieve[d - p - 1] != -1:
      if d - p == p:
        count += 2
      else:
        count += 1

  print(count // 2)