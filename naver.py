# 조건에 맞게 neverland() 함수를 만들기
def neverland(q):
  first = q.pop(2)
  q.sort()
  return [first] + q

# 대기 시간이 다음과 같을 때 지은이가 놀이 기구를 타는 순서를 확인
q = [30, 10, 20, 50, 40, 60]
print(neverland(q))