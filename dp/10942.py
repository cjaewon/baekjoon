import sys

sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().rstrip()
print = sys.stdout.write

N = int(input())
nums = [0] + list(map(int, input().split()))
M = int(input())

memo = [[False for j in range(2001)]for i in range(2001)]

def palindrome(S, E):
  if memo[S][E]:
    return memo[S][E]
  
  if S == E:
    return True
  elif S + 1 == E and nums[S] == nums[E]:
    return True
  else:
    if nums[S] != nums[E]:
      memo[S][E] = False
      return memo[S][E]
    else:
      memo[S][E] = palindrome(S + 1, E - 1)
      return memo[S][E]

for i in range(M):
  S, E = map(int, input().split())
  
  print("1\n" if palindrome(S, E) else "0\n")