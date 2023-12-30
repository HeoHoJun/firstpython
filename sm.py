# 변수 score에 학생의 점수 입력
score = int(input())

# 점수에 따라 성적 출력
if score == 0:
  print('F')
elif score >= 88:
  print('A+')
elif score >= 77:
  print('A0')
else:
  print('B+')