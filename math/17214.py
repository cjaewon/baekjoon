
expression = input()
expression = expression[0] + expression[1:].replace("-", "+-")

splited = expression.split("+")

# px + q
# p//2xx + qx + w

if len(splited) == 2:
  coefficient = int(splited[0].removesuffix("x"))
  constant = int(splited[1])

  if coefficient // 2 == 1:
    print("xx", end="")
  elif coefficient // 2 == -1:
    print("-xx", end="")
  else:
    print(f"{coefficient // 2}xx", end="")

  if constant == 1:
    print("+x", end="")
  elif constant == -1:
    print("-x", end="")
  else:
    if constant > 0:
      print(f"+{constant}x", end="")
    elif constant == 0:
      print("W")
      exit()
    else: # constant < 0:
      print(f"{constant}x", end="")
else: # len(splited) == 1: (문제 조건 상 len(splited)는 0이 될 수 없음)
  if "x" in splited[0]:
    coefficient = int(splited[0].removesuffix("x"))

    if coefficient // 2 == 1:
      print("xx", end="")
    elif coefficient // 2 == -1:
      print("-xx", end="")
    else:
      print(f"{coefficient // 2}xx", end="")
  else:
    constant = int(splited[0])

    if constant == 1:
      print("x", end="")
    elif constant == -1:
      print("-x", end="")
    else:
      if constant > 0:
        print(f"{constant}x", end="")
      elif constant == 0:
        print("W")
        exit()
        pass
      else: # constant < 0: (문제 조건 상 constant는 0이 될 수 없음)
        print(f"{constant}x", end="")

print("+W")