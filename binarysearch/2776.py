def solve():
  input()
  note1 = list(sorted(map(int, input().split())))
  input()
  note2 = list(map(int, input().split()))

  for n in note2:
    start = 0
    end = len(note1) - 1
    mid = (start + end) // 2
    isFound = False

    while start <= end:
      mid = (start + end) // 2
      if note1[mid] > n:
        end = mid - 1
      elif note1[mid] < n:
        start = mid + 1
      else: # note1[mid] == n
        isFound = True
        break
    
    print(int(isFound))
      

for i in range(int(input())):
  solve()