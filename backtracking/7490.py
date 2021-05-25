"""
백트래킹을 활용해서 숫자들의 연산자를 바꿔서 0으로 만드는 문제였다.
어려운 점은 연산자 중에 숫자를 합치는 공백 연산자가 포함되어 있다는 점 이였다.

처음에는 i + 2 까지 구현하다 i + 3을 어떻게 해야하지 고민했다.
prev 를 넘길려고 했는데 그렇게 되면 연산자 또한 같이 넘겨야 하여 코드가 복잡해질 것 같았는데


i + 2를 구현한듯이 i + 3 을 구현하는 코드를 작성했다. i + 4 부터는 최대 9까지 수열이기 때문에 나올 수가 없어서 따로 추가하지는 않았다.
마지막으로 1 바로 뒤에 공백이 되는 경우를 생각 안 해서 틀렸는데 예외를 추가하여 제출하니 정답이였다. 
"""

t = int(input())

result = []

# i = 인덱스, n = 1, 2, 3 .. N, sum = 합, text = 결과 텍스트
def tracker(i, n, sum, text):
  global result

  if n <= i:
    if sum == 0 and text[-1] == str(n):
      result.append(text)
    return

  if i == 1:
    tracker(i + 1, n, ((i) * 10 + i + 1), str(i) + " " + str(i + 1))
    tracker(i + 2, n, ((i) * 100 + (i + 1) * 10 + i + 2), str(i) + " " + str(i + 1) + " " + str(i + 2))
  

  tracker(i + 1, n, sum + (i + 1), text + "+" + str(i + 1))
  tracker(i + 1, n, sum - (i + 1), text + "-" + str(i + 1))
  tracker(i + 2, n, sum + ((i + 1) * 10 + i + 2), text + "+" + str(i + 1) + " " + str(i + 2))
  tracker(i + 2, n, sum - ((i + 1) * 10 + i + 2), text + "-" + str(i + 1) + " " + str(i + 2))

  tracker(i + 3, n, sum + ((i + 1) * 100 + (i + 2) * 10 + i + 3), text + "+" + str(i + 1) + " " + str(i + 2) + " " + str(i + 3))
  tracker(i + 3, n, sum - ((i + 1) * 100 + (i + 2) * 10 + i + 3), text + "-" + str(i + 1) + " " + str(i + 2) + " " + str(i + 3))



for i in range(t):
  n = int(input())
  result = []
  tracker(1, n, 1, "1")
  print("\n".join(sorted(result)))
  print()