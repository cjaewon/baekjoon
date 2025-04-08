A, B = map(int, input().split())
is_prime_number = [False, False] + [True] * (10 ** 7 + 1 - 2)

count = 0

for i in range(2, int((10 ** 7)) + 1):
  if is_prime_number[i]:
    k = 2

    while i ** k <= 10 ** 14 and i ** k <= B:
      if i ** k >= A:
        count += 1
      k += 1
    
    for j in range(i * i, 10 ** 7 + 1, i):
      is_prime_number[j] = False

print(count)