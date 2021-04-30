expressions = []
table = {}
table2 = {}

for i in range(int(input())):
  expressions.append(input())


for expression in expressions:
  for i in range(0, len(expression)):
    if not expression[i] in table:
      table[expression[i]] = 0

    if len(expression) - i == 1:
      table[expression[i]] += 1
    else:
      table[expression[i]] += pow(10, len(expression) - i - 1)

sort = sorted(table.items(), key=lambda n: n[1] ,reverse=True)
table2 = { sort[i][0] : 9 - i for i in range(0, len(sort)) }

result = 0

for expression in expressions:
  s = ""
  for chunk in expression:
    s += str(table2[chunk]) 

  result += int(s)

print(result)