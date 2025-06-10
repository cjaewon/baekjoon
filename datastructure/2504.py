string = input()
stack: list[int | str] = []

pair = {
  "[": "]",
  "(": ")",
  ")": "(",
  "]": "[",
}

for char in string:
  if char in ["[", "("]:
    stack.append(char)
  else:
    s = 0

    while stack:
      last: int | str = stack.pop()

      if last not in ["[", "("]:
        s += last
      else:
        if pair[char] == last and last == "[":
          if s == 0:
            stack.append(3)
          else:
            stack.append(s * 3)
        elif pair[char] == last and last == "(":
          if s == 0:
            stack.append(2)
          else:
            stack.append(s * 2)
        else:
          print(0)
          exit()

        break
    else:
      print(0)
      exit()
for val in stack:
  if not isinstance(val, int):
    print(0)
    exit()

print(sum(stack))