# 조건에 맞게 my_max() 함수 만들기
def my_max(nums):
  max_num = nums[0]
  for i in nums:
    if i > max_num:
      max_num = i
  return max_num

# 다음 리스트에서 최댓값이 무엇인지 확인
print(my_max([1, 2, 10, 9, 3, 7, 0, 99, 27, 85]))