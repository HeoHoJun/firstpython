# break 문을 그대로 따라서 입력
i = 1
while True:
  print(i, '월 1만 원을 입금했습니다.')
  if i == 12:
    print('입금 완료! 12만 원을 수령하세요!')
    break
  i = i + 1