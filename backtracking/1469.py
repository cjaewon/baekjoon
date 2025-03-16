N = int(input())
seq = list(map(int, input().split()))

results = []

def dfs(seq, som_seq):
  if -1 not in som_seq:
    results.append(som_seq[:])
    return

  for i in range(N * 2):
    if som_seq[i] != -1: continue
    
    for elem in seq:
      if elem in som_seq: continue

      if i + elem + 1 < 2 * N and som_seq[i + elem + 1] == -1:
        som_seq[i] = elem
        som_seq[i + elem + 1] = elem 

        dfs(seq, som_seq)

        som_seq[i + elem + 1] = -1
        som_seq[i] = -1
        
    
    break


dfs(
  seq = seq,
  som_seq=[-1 for i in range(2 * N)],
)

if results:
  print(" ".join(map(str, sorted(results)[0])))
else:
  print(-1)