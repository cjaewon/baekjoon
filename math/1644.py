N = int(input())

is_prime_number = [False, False] + [True] * (N + 1 - 2) # N + 1개, 마지막 index는 N
prime_numbers = []

# 에라토스테네스의 체
for i in range(2, N + 1):
  if is_prime_number[i]:
    prime_numbers.append(i)

    for j in range(i * i, N + 1, i):
      is_prime_number[j] = False

# 슬라이딩 윈도우로 풀자.

count = 0

# O(N^2)의 시간복잡도를 가지는 슬라이딩 윈도우 구현
# for window_size in range(1, len(prime_numbers) + 1):
#   continuous_sum = sum(prime_numbers[0:window_size])
#   if continuous_sum == N:
#     count += 1
#     continue

#   for end in range(window_size, len(prime_numbers) - window_size + 1):
#     continuous_sum += prime_numbers[end]
#     continuous_sum -= prime_numbers[end - window_size]

#     if continuous_sum == N:
#       count += 1
#       break

start = 0
end = 0

if N == 1:
  print(0)
  exit()

continuous_sum = prime_numbers[0]

# 가변 슬라이딩 윈도우
while start < len(prime_numbers):
  if continuous_sum < N:
    if end >= len(prime_numbers) - 1:
      break

    end += 1
    continuous_sum += prime_numbers[end]
  elif continuous_sum == N:
    count += 1
    continuous_sum -= prime_numbers[start]
    start += 1
  else:
    continuous_sum -= prime_numbers[start]
    start += 1

print(count)