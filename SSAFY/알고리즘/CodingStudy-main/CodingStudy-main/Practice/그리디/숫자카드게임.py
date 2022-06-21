# 나의 방법 : 배열에 같은 행에서의 가장 작은 수를 넣고 그 배열을 다시 소팅해서 가장 큰 수를 출력한다.
n, m =map(int,input().split())
data=[]
data2=[]
for i in range(n):
  data=list(map(int, input().split()))
  data.sort()
  data2.append(data[0])
data2.sort()
print(data2[-1])

# min 함수 이용
n,m=map(int,input().split())
result=0
for i in range(n):
  data=list(map(int,input().split()))
  min_value=min(data) # 행중에 가장 작은 값을 min_value에 할당
  result=max(result,min_value) # for문을 돌면서 min_value와 이전 값들을 계속 비교해서 가장 큰 수 할당
print(result)

# 2중 반복문 구조 사용
n,m=map(int,input().split())

result=0
for i in range(n):
  data=list(map(int, input().split())) # n행에 m개의 숫자를 받는 역할
  min_value=10001 #첫번째 값과 비교할 min_value 할당
  for a in data: #data의 i번째 원소 안에 숫자들 중 가장 작은 값을 찾는 for문
    min_value=min(min_value,a) #min_value와 a를 비교했을 때 더 작은 값을 반환하여 min_value에 할당
  result=max(result,min_value) # 행마다의 minvalue를 비교하여 가장 큰 값을 result로 반환
print(result)
