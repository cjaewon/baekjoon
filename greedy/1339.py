"""
처음에 글자 길이를 보고 가장 큰 글자 길이를 바탕으로 숫자들을 알파벳에 대응시켜주었지만 길이가 작은 알파벳도 여러개가 있을 시
큰 글자의 길이를 넘을수도 있어서 틀렸다. 그래서 자릿값에 따라서 10의 n 승을 더해줘서 알파벳들을 대응 시키는 걸로 바꾸었다.
"""

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