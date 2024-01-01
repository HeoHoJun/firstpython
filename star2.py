# input() 함수로 층수를 입력받아 저장
star = int(input())

# 입력받은 층수의 별자리를 출력
for i in range(1, star + 1):
  print('*' * i)