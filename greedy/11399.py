input()

data = list(map(int, input().split()))
sorted_data = sorted(data)
datasum = 0

for i in range(0, len(sorted_data)):
  datasum += sum(sorted_data[:(i + 1)])

print(datasum)