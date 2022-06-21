#n시 59분 59초 중에서 3이 나오는 시간 몇개인지 구하기
#나의 풀이 : 전체 경우의 수에서 3이 등징하지 않는 경우의 수를 뺀다
#장단점 : 식이 간단하고 for문을 돌리지 않아서 연산 횟수가 작다. 책의 풀이 방식보다 코드에 대한 설명이 좀 더 상세하게 필요한 점이 단점 인 것 같다. 
n=int(input())
result=((n+1)*6*10*6*10) - ((n)*5*9*5*9)
print(result)

# 책의 풀이 : 하나씩 탐색해서 3이 등장하는 갯수를 구한다.
h=int(input())

count=0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        count+=1
print(count)
