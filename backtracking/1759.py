"""
백트래킹 문제로 가능한 모든 경우를 확인 한 후 
조건 (모음, 자음)에 맞는지 확인한 후 사전 순으로 출력하는 문제였다.

먼저 비밀번호가 정렬 된 형태로 있다고 하므로 사전 순으로 출력하는 부분은 신경을 써 줄 필요가 없었다.
그리고 백트래킹을 수행하는 함수에는 i (최근에 사용 된 문자의 위치), count, ctx (현재 문자열), 자음, 모음를 인자로 받고 실행했다.
"""

l, c = map(int, input().split())
abc = list(sorted(input().split()))

used = [0 for i in range(26)]

def back(i, count, ctx, consonant, vowel):
  if l == count:
    if consonant >= 2 and vowel >= 1:
      print(ctx)
    return

  used[ord(ctx[-1]) - 97] = 1

  for j in range(i, len(abc)):
    if used[ord(abc[j]) - 97] == 1:
      continue

    if abc[j] in ["a", "e", "i", "o", "u"]:
      back(j, count + 1, ctx + abc[j], consonant, vowel + 1)
    else:
      back(j, count + 1, ctx + abc[j], consonant + 1, vowel)
  
  used[ord(ctx[-1]) - 97] = 0

for i in range(len(abc)):
  if abc[i] in ["a", "e", "i", "o", "u"]:
    back(i, 1, abc[i], 0, 1)
  else:
    back(i, 1, abc[i], 1, 0)