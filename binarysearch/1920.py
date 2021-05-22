input()
inp = list(sorted(map(int, input().split())))
input()
oup = list(map(int, input().split()))
           

def binarysearch(start, end, k):
    mid = (start + end) // 2
    
    if start > end:
        return 0
    
    if inp[mid] == k:
        return 1
    elif inp[mid] > k:
        return binarysearch(start, mid - 1, k)
    elif inp[mid] < k:
        return binarysearch(mid + 1, end, k)

for i in oup:
    print(binarysearch(0, len(inp) - 1, i))
    

        
