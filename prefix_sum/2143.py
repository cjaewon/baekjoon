import sys
from itertools import accumulate
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

n = int(input())
As = list(map(int, input().split()))

m = int(input())
Bs = list(map(int, input().split()))

prefix_A = [0] + list(accumulate(As))
prefix_B = [0] + list(accumulate(Bs))

sub_arr_sum_A = []
sub_arr_sum_B = []

for i in range(n):
  for j in range(i + 1, n + 1):
    sub_arr_sum_A.append(prefix_A[j] - prefix_A[i])

for i in range(m):
  for j in range(i + 1, m + 1):
    sub_arr_sum_B.append(prefix_B[j] - prefix_B[i])

cnt = 0
sub_arr_sum_counted_A = Counter(sub_arr_sum_A)

for b in sub_arr_sum_B:
  if T - b in sub_arr_sum_counted_A:
    cnt += sub_arr_sum_counted_A[T- b]

print(cnt)