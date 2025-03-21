cache = {}

def dp(M, i, coin_types):
  if i == 0:
    if M % coin_types[i] == 0:
      return 1
    else:
      return 0
  if M < coin_types[i]:
    if (M, i - 1) not in cache: 
      cache[(M, i - 1)] = dp(M, i - 1, coin_types)

    return cache[(M, i - 1)]
  
  if (M - coin_types[i], i) not in cache:
    cache[(M - coin_types[i], i)] = dp(M - coin_types[i], i, coin_types)

  if (M, i - 1) not in cache:
    cache[(M, i - 1)] = dp(M, i - 1, coin_types)
  return cache[(M - coin_types[i], i)] + cache[(M, i - 1)]

T = int(input()) # T: testcase

for i in range(T):
  N = int(input())
  coin_types = list(map(int, input().split()))
  M = int(input())

  print(dp(M, N - 1, coin_types))

  cache = {}

"""
점화식에 대해 고민해보자

1 5 10 50 100 500

f(M, N) = N원 이하의 동전으로 M원을 만들 수 있는 경우의 수
f(M, N) = f(M - N, N) + f(M, N - 1)

N을 인덱스로 나타내자.

22,1(7) = 15, 0 + 22, 0
15,0(5) = 3 


"""
