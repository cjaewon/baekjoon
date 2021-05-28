"""
문제
- 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

유클리드 호제법을 이용해서 구해야지만 시간안에 풀 수 있는 문제였다.
유클리드 호제법이란 gcd(A, B) = gcd(B, A % B) 을 뜻한다.
A % B = 0 이 될 때까지 반복하는데 0은 모든 수의 약수이므로 최종적인 B가 최대공약수이다.

최대공약수를 g 라고 잡으면
A = ga
B = gb 일 것이다 (단 a, b 는 서로소)

이때 최소공배수는 gab 이므 A * B / g 를 구해주면 최소공배수가 나온다. 
"""

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)


for i in range(int(input())):
  a, b = map(int, input().split())
  result = gcd(a, b)

  print(a * b // result)