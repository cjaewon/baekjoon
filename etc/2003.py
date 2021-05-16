n, m = map(int, input().split())
data = list(map(int, input().split()))

presum = 0
count = 0

end = 0

for start in range(n):
    while m > presum and end < n:
        presum += data[end] 
        end += 1
    
    if m == presum:
        count += 1
        
    presum -= data[start]
print(count)