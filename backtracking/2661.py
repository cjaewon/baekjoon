n = int(input())

def back(text):
  if len(text) == n:
    print(text)
    exit()

  for i in range(1, 4):
    temp = text + str(i)

    if len(temp) == 1:
      back(temp)
    else:
      for j in range(1, len(temp) + 1):
        if abs(-1 * 2 * j) > len(temp): # break가 되지 않을시 항상 작동함
          back(temp)
        else:
          if temp[-j:] == temp[-1 * 2 * j:-j]:  # 중복이 있을 시 break
            break

back("")