N, M = map(int, input().split())
height = []

for i in range(M):
  H1, H2 = map(int, input().split())

  height.append((H1, i + 1))
  height.append((H2, i + 1))

height.sort()

print(height[N % (M*2) - 1][1])