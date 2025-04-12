N = int(input())
liquids = sorted(map(int, input().split()))

min_sum = float("inf")
min_sum_list = []

for i in range(N):
  for j in range(i + 1, N):
    start = j + 1
    end = N - 1

    while start <= end:
      mid = (start + end) // 2
      
      if liquids[i] + liquids[j] + liquids[mid] > 0:
        if abs(liquids[i] + liquids[j] + liquids[mid]) < min_sum:
          min_sum = abs(liquids[i] + liquids[j] + liquids[mid])
          min_sum_list = [liquids[i], liquids[j], liquids[mid]]

        end = mid - 1
      elif liquids[i] + liquids[j] + liquids[mid] < 0:
        if abs(liquids[i] + liquids[j] + liquids[mid]) < min_sum:
          min_sum = abs(liquids[i] + liquids[j] + liquids[mid])
          min_sum_list = [liquids[i], liquids[j], liquids[mid]]

        start = mid + 1
      else:
        print(liquids[i], liquids[j], liquids[mid])
        exit()
  
for i in min_sum_list:
  print(i, end=" ")