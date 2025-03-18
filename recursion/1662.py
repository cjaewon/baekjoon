S = input()

def unzip(check_str):
  cnt = 0

  first_idx = None
  last_idx = None
  parenthesis = 0

  for i in range(0, len(check_str)):
    if check_str[i] == "(":
      if first_idx == None: first_idx = i
      parenthesis += 1
    elif check_str[i] == ")":
      parenthesis -= 1

      if parenthesis == 0:
        last_idx = i
        cnt += unzip(check_str[first_idx + 1:last_idx]) * int(check_str[first_idx - 1])
        first_idx = None
        last_idx = None
    else:
      if parenthesis == 0:
        if i + 1 < len(check_str) and check_str[i + 1] == "(": continue

        cnt += 1

  return cnt

print(unzip(S))
