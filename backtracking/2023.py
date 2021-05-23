n = int(input())

def isprime(k):
  if k == 1:
    return False

  for i in range(2, k):
    if k % i == 0:
      return False
  return True

def back(k, t): # k = 자리 수, t = 전체 수
  if k == n:
    print(t)
    return

  for i in range(1, 10):
    if isprime(t * 10 + i):
      back(k + 1, t * 10 + i)

back(0, 0)