# 기차에 승객이 3명 있어요
train = ['우영우', '서목화', '채송아']

# 서울역: 승객 '박은빈'을 맨 뒤에 태우세요
train.append('박은빈')
print('서울역 도착. //', train)

# 대전역: 1등석 승객 '송지원'을 맨 앞에 태우세요
train.insert(0, '송지원')
print('대전역 도착. //', train)

# 부산역: 종착역이니 사전순으로 정렬
train.sort()
print('부산역 도착. //', train)
print('오늘도 기차를 이용해 주셔서 감사합니다.')