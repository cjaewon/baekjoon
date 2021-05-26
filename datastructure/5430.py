from collections import deque

for i in range(int(input())):
  cmd = input()
  input()
  splited = input()[1:-1].split(",")

  q = None

  if splited[0] == "":
    q = deque()
  else:
    q = deque(splited)
    
  front = True
  iserr = False

  for c in cmd:
    if c == "R":
      front = not front
    elif c == "D":
      if not q:
        iserr = True
        break

      if front:
        q.popleft()
      else:
        q.pop()
  
  if iserr:
    print("error")
  elif front:
    print("[" + ",".join(q) + "]")
  else:
    print("[" + ",".join(reversed(q)) + "]")
    