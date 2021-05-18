"""
처음에는 반복문을 일일히 나누었지만 더 빨리 나누기 위해 에라토스테네스의 체로 코드를 변경해보았다.
에라토스테네스의 체를 사용한 코드의 시간이 더 오래 걸렸는데 그 이유는 소인수분해 같은 경우는 큰 수의 소수로 나누는 일이 많이 없어서 그런 것 같다.
"""

n = int(input())
sieve = [i for i in range(1, n + 1)]

if n == 1:
  exit()

sieve[0] = -1

print(int(sieve[-1] ** 0.5) + 1, 123)
for i in range(1, int(sieve[-1] ** 0.5) + 1):
  if sieve[i] != -1:
    for j in range(i + sieve[i], n, sieve[i]):
      sieve[j] = -1

primes = list(filter(lambda n: n != -1, sieve))
i = 0


while n >= primes[i]:
  if n % primes[i] == 0:
    n = n / primes[i]
    print(primes[i])
    continue

  i += 1
