N = int(input())

is_prime_numer = [False, False] + [True] * (1003001 + 1 - 2)

# 원래는 range 안에 N ** 0.5 + 1로 하는게 정석적임.
# 다만 if is_prime_number에서 즉 소수인 경우에서 팰린드롬인 수인지 확인할 것이므로 i가 N까지 모두 순회가 필요함. 
# 또한 어차피 밑에 for문은 실행되지 않으므로 그렇게 크게 성능 차이는 없을거임. 

for i in range(2, 1003001 + 1):
  if is_prime_numer[i]:
    if i >= N:
      # 팰린드롬인 수인지 확인하자.
      forward_str_i = str(i)
      reversed_str_i = str(i)[::-1]

      for k in range(len(str(i)) // 2):
        if forward_str_i[k] != reversed_str_i[k]:
          break
      else:
        print(i)
        break


    for j in range(i * i, 1003001 + 1, i):
      is_prime_numer[j] = False