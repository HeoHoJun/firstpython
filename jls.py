# 변수 num에 숫자형으로 값을 입력
num = int(input())

# 자릿수 판별기
if 1 <= num and num < 10:
  print('한 자리 숫자입니다.')
elif 10 <= num and num < 100:
  print('두 자리 숫자입니다.')
else:
  print('세 자리 숫자입니다.')