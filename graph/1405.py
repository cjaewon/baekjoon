N, *poss = map(int, input().split())

# poss : [동, 서, 남, 북]
poss = [p / 100 for p in poss] 

def dfs(n: int, pos: tuple[int, int], rec_visited:set[tuple[int, int]]=set()):
  rec_visited.add(pos)
  y, x = pos

  s = 0

  if n == 0:
    rec_visited.remove(pos)
    return 1

  for i, (dy, dx) in enumerate([(0, 1), (0, -1), (-1, 0), (1, 0)]):
    if (y + dy, x + dx) not in rec_visited:
      s += dfs(n - 1, (y + dy, x + dx), rec_visited=rec_visited) * poss[i]

  rec_visited.remove(pos)

  return s

print(dfs(N, pos=(0, 0)))