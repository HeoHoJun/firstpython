# 변수 num에 판별할 숫자 입력
num = int(input())

# num이 짝수이면 '(숫자) 짝수입니다.', 홀수이면 '(숫자) 홀수입니다.'를 출력
if num % 2 == 0:
  print('짝수입니다.')
else:
  print('홀수입니다.')