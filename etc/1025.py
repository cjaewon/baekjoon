import math

N, M = map(int, input().split())
board = [list(map(int, input())) for i in range(N)]
candidates = []

for i in range(N):
  for j in range(M):
    for k in range(-N, N):
      for m in range(-M, M):
        number = 0
        l = 0

        while True:
          if  k == 0 and m == 0:
            number = board[i][j]
            break
          
          if 0 <= i + k * l < N and 0 <= j + m * l < M:
            number = number * 10 + board[i + k * l][j + m * l]

            if number % 4 == 0 or number % 4 == 1:
              if number == math.isqrt(number) ** 2:
                candidates.append(number)
          else:
            break
          
          l += 1


        

if not candidates:
  print(-1)
else:
  print(max(candidates))
