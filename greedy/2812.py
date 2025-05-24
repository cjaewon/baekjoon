N, K = map(int, input().split())
stack = []

nums = list(map(int, input()))

for i, n in enumerate(nums):
  while K > 0 and stack and stack[-1] < n:
    stack.pop()
    K -= 1
    
  stack.append(n)

  
if K > 0:
  print("".join(map(str, stack[:-K])))
else:
  print("".join(map(str, stack)))