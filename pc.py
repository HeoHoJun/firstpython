# my_list에 리스트 원소가 들어 있어요
my_list = [1, 2, 2, 3, 3, 3]

# my_list 안에 있는 원소 3의 개수를 변수에 저장
var = my_list.count(3)

# my_list가 [1, 2, 3]이 되도록 소괄호 안에 숫자를 입력해 원소 2와 3을 지우기
my_list.pop(1)  # [1, 2, 3, 3, 3]
my_list.pop(2)  # [1, 2, 3, 3]
my_list.pop(2)  # [1, 2, 3]

# 출력
print(my_list)