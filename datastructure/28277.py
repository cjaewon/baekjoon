import sys

input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
n_set = [set()] + [set(list(map(int, input().split()))[1:]) for _ in range(N)]

for _ in range(Q):
  match list(map(int, input().split())):
    case [1, a, b]:
      if len(n_set[a]) > len(n_set[b]):
        for v in n_set[b]:
          n_set[a].add(v)
      else:
        for v in n_set[a]:
          n_set[b].add(v)
        n_set[a] = n_set[b]

      n_set[b] = set()
    case [2, a]:
      print(len(n_set[a]))
