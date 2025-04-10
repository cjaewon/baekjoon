content = input()
boom = input()

lst = []

for char in content:
  lst.append(char)

  if len(lst) >= len(boom) and "".join(lst[-len(boom):]) == boom:
    for j in range(len(boom)):
      lst.pop()


if len(lst) == 0:
  print("FRULA")
else:
  print("".join(lst))