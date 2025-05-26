"""
1 ~ N번까지 원을 이루고 앉았을 때 K번째를 계속해서 제거해나간 후 제거된 순서를 차례대로 출력해야함.
"""

from collections import deque

N, K = map(int, input().split())

q = deque([i for i in range(1, N + 1)])
rst = []

while q:
  q.rotate(-K)
  rst.append(q.pop())

print(f"<{", ".join(map(str, rst))}>")
