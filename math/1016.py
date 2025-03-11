min_num, max_num = map(int, input().split())
square_check = {}

i = 2

while i ** 2 <= max_num:
  k = min_num // (i ** 2)

  while (i ** 2) * k <= max_num:
    if min_num <= (i ** 2) * k:
      square_check[(i ** 2) * k] = True
    
    k += 1
  i += 1

print(max_num - min_num + 1 - len(square_check))