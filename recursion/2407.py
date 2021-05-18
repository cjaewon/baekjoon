"""
나눠주고 int로 변환해주면 실수오차가 발생하기 때문에
// 를 사용하여 int 알아내야한다.
"""

n, m = map(int, input().split())

def factorialwithcount(start, n, count):
  if count == n:
      return start

  return start * factorialwithcount(start - 1, n, count + 1)

up = factorialwithcount(n, m, 1)
down = factorialwithcount(m, m, 1)

if up % down == 0:
  print(up // down)
else:
  print(up // down)
