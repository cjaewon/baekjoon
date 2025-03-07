import sys

sys.setrecursionlimit(99999999)

# n: n번째 피보나치 수를 구해서 1000000으로 나눈 값을 출력한다.
n = int(input())
memo = {}

# 피사노 주기와 fast doubling을 모두 써야하는 문제인듯

def fib(m): # m은 양의 정수
  if m == 0:
    return 0
  elif m == 1:
    return 1
  elif m == 2:
    return 1
  elif m in memo:
    return memo[m]
  
  if m % 2 == 0: # 짝수
    memo[m] = fib(m // 2) * (2 * fib(m // 2 + 1) - fib(m // 2))
    return memo[m]
  else: # 홀수
    memo[m] = fib(m // 2 + 1) ** 2 + fib(m // 2) ** 2
    return memo[m]
  

print(fib(n % 1500000) % 1000000)