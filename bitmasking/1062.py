from collections import deque
from functools import reduce

"""
antic
(1 << ord("a") - ord("a")) | (1 << ord("n") - ord("a")) | (1 << ord("t") - ord("a")) | (1 << ord("i") - ord("a")) | (1 << ord("c") - ord("a")) = 532741
"""

N, K = map(int, input().split())
words = [0 for i in range(N)]

if K < 5:
  print(0)
  exit()

for i in range(N):
  word = input()

  for char in word:
    words[i] |= (1 << (ord(char) - ord('a')))

available_alphabet = reduce(lambda acc, curr: acc | curr, words)

stack = deque([(i, 532741 | (1 << i)) for i in range(26) if available_alphabet & (1 << i)])
max_word_cnt = 0

while stack:
  curr, selected = stack.pop()

  if bin(selected).count("1") == K:
    word_cnt = 0

    for word in words:
      if word & selected == word:
        word_cnt += 1

    max_word_cnt = max(max_word_cnt, word_cnt)

    continue

  for i in range(curr + 1, 26):
    if 532741 & (1 << i):
      continue

    # if available_alphabet & (1 << i):
    stack.append((i, selected | (1 << i)))

print(max_word_cnt)
