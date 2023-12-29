# 변수 ans에 숫자 1~50 중 이 게임의 정담 숫자 하나를 골라 넣어라.
ans = 45

# 변수 num에 숫자를 입력
num = int(input())

# num이 ans보다 크면 '그 수보다 작아요.', '작으면 '그 수보다 커오.', 같으면 '정답!'을 출력
if num > ans:
  print('그 수보다 작아요.')
elif num < ans:
  print('그 수보다 커요.')
else:
  print('정답!')