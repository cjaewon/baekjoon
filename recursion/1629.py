def callback(a, b, c):
  if b == 1:
    return a % c

  result = callback(a, int(b / 2), c)
  result = result * result % c

  if b % 2 == 0:
    return result
  else:
    return result * a % c

a, b, c = map(int, input().split())
print(callback(a, b, c) % c)