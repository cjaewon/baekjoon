"""
굉장히 힘들게 푼 문제로 여러 조건을 생각해봐야 하는 문제였던 것 같다.
"""

import sys

maxheap = [None for i in range(1000001)]
minheap = [None for i in range(1000001)]
maxend = 0
minend = 0
maxisused = {}
minisused = {}
abc123 = True

def maxheapify(curr):
  while curr * 2 <= maxend:
    if maxheap[curr * 2] > maxheap[curr] and curr * 2 + 1 <= maxend and maxheap[curr * 2] >= maxheap[curr * 2 + 1]:
      maxheap[curr * 2], maxheap[curr] = maxheap[curr], maxheap[curr * 2]
      curr = curr * 2
    elif maxheap[curr * 2] > maxheap[curr] and curr * 2 + 1 > maxend:
      maxheap[curr * 2], maxheap[curr] = maxheap[curr], maxheap[curr * 2]
      curr = curr * 2
    elif curr * 2 + 1 <= maxend and maxheap[curr * 2 + 1] > maxheap[curr] and maxheap[curr * 2 + 1] >= maxheap[curr * 2]:
      maxheap[curr * 2 + 1], maxheap[curr] = maxheap[curr], maxheap[curr * 2 + 1]
      curr = curr * 2 + 1
    else:
      break

def minheapify(curr):
  while curr * 2 <= minend:
    if minheap[curr * 2] < minheap[curr] and curr * 2 + 1 <= minend and minheap[curr * 2] <= minheap[curr * 2 + 1]:
      minheap[curr * 2], minheap[curr] = minheap[curr], minheap[curr * 2]
      curr = curr * 2
    elif minheap[curr * 2] < minheap[curr] and curr * 2 + 1 > minend:
      minheap[curr * 2], minheap[curr] = minheap[curr], minheap[curr * 2]
      curr = curr * 2
    elif curr * 2 + 1 <= minend and minheap[curr * 2 + 1] < minheap[curr] and minheap[curr * 2 + 1] <= minheap[curr * 2]:
      minheap[curr * 2 + 1], minheap[curr] = minheap[curr], minheap[curr * 2 + 1]
      curr = curr * 2 + 1
    else:
      break



def insert(val):
  global maxend, minend

  maxend += 1
  maxheap[maxend] = val

  minend += 1
  minheap[minend] = val

  curr = maxend
  while curr // 2 >= 1:
    if maxheap[curr // 2] < maxheap[curr]:
      maxheap[curr // 2], maxheap[curr] = maxheap[curr], maxheap[curr // 2]
    curr = curr // 2

  curr = minend
  while curr // 2 >= 1:
    if minheap[curr // 2] > minheap[curr]:
      minheap[curr // 2], minheap[curr] = minheap[curr], minheap[curr // 2]
    curr = curr // 2

def remove(type):
  global maxend, minend
  result = 0
  last = False

  if type == 1:
    if maxend == 0:
      return None
    
    while maxend >= 1: # maxend = 1? 
      
      result = maxheap[1]
      maxheap[1] = maxheap[maxend]
      maxheap[maxend] = None
      maxend -= 1
      last = False
      
      maxheapify(1)
    
      if not str(result) in maxisused:
        break
      elif maxisused[str(result)] < 1:
        break
      else:
        maxisused[str(result)] -= 1
        last = True
    maxheapify(1)

    if last:
      return None

    if str(result) in minisused and abc123:
      minisused[str(result)] += 1
    elif abc123:
      minisused[str(result)] = 1
  elif type == -1:
    if minend == 0:
      return
    while minend >= 1:
      
      result = minheap[1]
      minheap[1] = minheap[minend]
      minheap[minend] = None
      minend -= 1
      last = False

      minheapify(1)
        
      if not str(result) in minisused:
        break
      elif minisused[str(result)] < 1:
        break
      else:
        minisused[str(result)] -= 1
        last = True
    minheapify(1)

    if last:
      return None
    elif str(result) in maxisused and abc123:
      maxisused[str(result)] += 1
    elif abc123:
      maxisused[str(result)] = 1
  
  return result
for i in range(int(input())):
  maxheap = [None for i in range(1000001)]
  minheap = [None for i in range(1000001)]
  maxend = 0
  minend = 0
  maxisused = {}
  minisused = {}
  abc123 = True

  for j in range(int(input())):
    cmd, val = sys.stdin.readline().rstrip().split()
    val = int(val)

    if cmd == "I":
      insert(val)      
    elif cmd == "D":
      remove(val)
    # print("max", maxheap[0: 10], "min", minheap[0: 10])
    # print("maxisused", maxisused)
    # print("minisused", minisused)
  abc123 = False
  maxval = remove(1)
  minval = remove(-1)

  if maxval == None or minval == None:
    print("EMPTY")
  else:
    print(maxval, minval)
