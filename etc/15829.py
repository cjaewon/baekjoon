L = int(input())
S = input()

r = 31
M = 1234567891

H = 0

for i, s in enumerate(S):
  H += ((ord(s) - 96) * r ** i) % M

print(H % M)