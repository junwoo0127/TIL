#상하좌우
#for문 안에서 continue와 break의 차이 : continue는 반복을 끝내지 않고 i만 증가 시키지만 break문을 사용하면 반복을 끝내 버린다.
# 내가 푼 방식 장단점 : 단점을 살펴 보면 책에서 분 방식은 R, L, U, D 방향 별로 이동하는 값을 하나의 리스트에 x,y로 분리하여 정의해서 나의 코드보다 연산 횟수를 줄 일 수 있었고 범위또한 마지막 if 문에서 걸러서 연산 횟수를 한번으로 줄일 수 있다.
# 장점은 L, R, U, D에 대한 연산을 각각 조건문에 처리했기 때문에 코드의 가독성이 좋은 것 같다.

n=int(input())
data=[]

data.append(1)
data.append(1)

dir=input().split()

for i in dir:
  if i=='R':
    if data[1]==5:
      continue
    data[1]+=1

  elif i=='L':
    if data[1]==1:
      continue
    data[1]-=1

  elif i=='U':
    if data[0]<=1:
      continue
    data[0]-=1

  elif i=='D':
    if data[0]>=5:
      continue
    data[0]+=1

print(data[0],data[1])

# 책에서 푼 방식
n=int(input())
x,y=1,1
plans=input().split()

# L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

# 입력값을 하나씩 끄집어 내서
for plan in plans:
  # L, R, U, D 인지 체크
  for i in range(len(move_types)):
    # 해당하는 방향에서의 값 더하기
    if plan==move_types[i]:
      nx=x+dx[i]
      ny=y+dy[i]
  # 만약에 범위를 초과할 시, 다음 순서로 이동
  if nx<1 or ny<1 or nx>n or ny>n:
    continue
    # x,y 결과 좌표에 연산한 좌표 할당
  x,y=nx,ny

print(x,y)
