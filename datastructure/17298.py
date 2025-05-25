N = int(input())
As = list(map(int, input().split()))

mstack = []
nge = []

for a in reversed(As):
  while mstack:
    if a >= mstack[-1]:
      mstack.pop()
    else:
      break

  nge.append(mstack[-1] if mstack else -1)
  mstack.append(a)

print(" ".join(map(str, reversed(nge))))