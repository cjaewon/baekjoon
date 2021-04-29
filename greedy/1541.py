"""
마이너스 기호가 포함되어 있으면 마이너스가 나오기 직전까지 다 괄호를 쳐주면 최소를 구할 수 있다. 마이너스가 나오면 다시 그때부터 괄호를
새로 만들어주면 된다. 이러한 이유는 마이너스 마이너스의 경우 양수가 되기 때문이다.
"""

expression = input()
chunks = []

for i in range(0, len(expression)):
  if expression[i] == "+":
    chunks.append("+")
  elif expression[i] == "-":
    chunks.append("-")
  else:
    if len(chunks) == 0 or chunks[len(chunks) - 1] == "+" or chunks[len(chunks) - 1] == "-":
      chunks.append(expression[i])
    else:
      chunks[len(chunks) - 1] += expression[i]

sum = 0 
is_sub = False # 뺄셈이 사용됬는지
sub_sum = 0

for chunk in chunks:
  if chunk == "-":
    if is_sub:
      sum -= sub_sum
      sub_sum = 0
    else:
      is_sub = True
  elif chunk == "+":
    pass
  else:
    if is_sub:
      sub_sum += int(chunk)
    else:
      sum += int(chunk)

print(sum - sub_sum)