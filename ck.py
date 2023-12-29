# 변수 cookie에 먹은 쿠키의 개수를 입력
cookie = int(input())

# cookie가 음수이면 -1을 곱해 다시 cookie에 저장
if cookie < 0:
	cookie = cookie * -1
 
# cookie의 개수가 몇 개인지 출력
print(cookie) 