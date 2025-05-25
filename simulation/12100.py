import copy
import sys

sys.setrecursionlimit(10 ** 5)


class Game:
  grid: list[list[int]]
  N: int
  max_num: int

  def __init__(self, N: int, grid: list[list[int]]):
    self.grid = grid
    self.N = N
    self.max_num = max([v for row in grid for v in row])

  def up(self):
    for i in range(self.N):
      std = None
      new_line = []

      for j in range(self.N):
        if self.grid[j][i] == 0:
          continue

        if std is None:
          std = self.grid[j][i]
        elif std == self.grid[j][i]:
          new_line.append(std + self.grid[j][i])
          std = None
        else:
          new_line.append(std)
          std = self.grid[j][i]

      if std is not None:
        new_line.append(std)

      new_line = new_line + [0] * (self.N - len(new_line))

      for k in range(self.N):
        self.grid[k][i] = new_line[k]
      self.max_num = max(*new_line, self.max_num)
  
  def down(self):
    for i in range(self.N):
      std = None
      new_line = []

      for j in range(self.N - 1, -1, -1):
        if self.grid[j][i] == 0:
          continue

        if std is None:
          std = self.grid[j][i]
        elif std == self.grid[j][i]:
          new_line.append(std + self.grid[j][i])
          std = None
        else:
          new_line.append(std)
          std = self.grid[j][i]

      if std is not None:
        new_line.append(std)

      new_line = new_line + [0] * (self.N - len(new_line))
      new_line.reverse()

      for k in range(self.N):
        self.grid[k][i] = new_line[k]

      self.max_num = max(*new_line, self.max_num)

  def left(self):
    for i in range(self.N):
      std = None
      new_line = []

      for j in range(self.N):
        if self.grid[i][j] == 0:
          continue

        if std is None:
          std = self.grid[i][j]
        elif std == self.grid[i][j]:
          new_line.append(std + self.grid[i][j])
          std = None
        else:
          new_line.append(std)
          std = self.grid[i][j]

      if std is not None:
        new_line.append(std)

      new_line = new_line + [0] * (self.N - len(new_line))
      self.grid[i] = new_line
      self.max_num = max(*new_line, self.max_num)

  def right(self):
    for i in range(self.N):
      std = None
      new_line = []

      for j in range(self.N - 1, -1, -1):
        if self.grid[i][j] == 0:
          continue

        if std is None:
          std = self.grid[i][j]
        elif std == self.grid[i][j]:
          new_line.append(std + self.grid[i][j])
          std = None
        else:
          new_line.append(std)
          std = self.grid[i][j]

      if std is not None:
        new_line.append(std)

      new_line = new_line + [0] * (self.N - len(new_line))
      self.grid[i] = new_line[::-1]
      self.max_num = max(*new_line, self.max_num)

N = int(input())
grid = [list(map(int, input().split())) for i in range(N)]

game = Game(N, grid)
max_num = game.max_num

def backtracking(n: int, game: Game):
  global max_num

  if n == 0:
    max_num = max(game.max_num, max_num)
    return

  for i in range(4):
    copyed_game = copy.deepcopy(game)
    act = [copyed_game.up, copyed_game.down, copyed_game.left, copyed_game.right][i]

    act()
    backtracking(n - 1, copyed_game)


backtracking(5, game)
print(max_num)
