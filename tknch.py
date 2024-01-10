# math 모듈을 불러오세요
import math

# 7의 12제곱과 6의 13제곱 값을 순서대로 저장
num1 = math.pow(7, 12)
num2 = math.pow(6, 13)

# if 문에 알맞은 조건을 적어 답을 출력
if num1 > num2:
  print('7의 12제곱이 더 크다.')
else:
  print('6의 13제곱이 더 크다.')