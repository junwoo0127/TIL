# 못푼 문제
# 고찰 : 방향을 돌리는 과정에서 계속해서 에러가 발생했는데 그 이유가 변수를 튜플로 두고 연산 처리를 계속 해서 코드를 이해하기 난잡해졌다
# 책에서는 x, y를 각각 따로 정의해서 풀이하여 좀 더 코드 이해가 빠르게 될 수 있었다.
# 조건을 정할 때 가본곳/안가본곳 리스트 하나와 육지/바다 리스트 하나를 정의해서 
# 두가지 조건을 만족 할 때 방향으로 이동하고 아니면 방향을 바꿔주는 방식으로 풀이하는 것이 포인트 같다. 
# 방향을 바꿔줄 때도 방향에 따른 연산이 필요하고 방향에 조건으로 4번을 다 돌게 되면 바라보는 방향을 유지한채로 한칸 뒤로가는 코드가 필요하다.
# 조건이 까다롭고 변수를 똑똑하게 정의 해야하는 문제 인 것 같다.

#n,m 입력 받음
n,m=map(int, input().split())

# d(n행 m열) 초기화 : 안간곳은 0으로 초기화 하기 위해
d = [[0] * m for _ in range(n)]

# x,y,direction 입력 받음
x, y, direction=map(int, input().split())

# 현재 좌표 방문 처리(0 ->1)
d[x][y] = 1 

array=[]

# map(바다와 육지로 구성)에 해당하는 array를 입력 받음
for i in range(n):
  array.append(list(map(int, input().split())))

# 연산을 위한 dx,dy 정의, 차례대로 북, 동, 남, 서
# 입력받을 때 조건이 0:북, 1:동, 2:남, 3:서 이기 때문임
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 왼쪽으로 회전 함수 정의
def turn_left():
  # 전역변수 direction은 turn_left함수를 만나면 시계 반대 방향으로 90도 회전함
  # 회전하면 방향이 바뀌는데 0(북)>1(동)>2(남)>3(서)>0(북) 순으로 바뀜
  # 따라서 direction이 0인 경우는 direction 3으로 바꿔줘야함. 앞에서 -1 연산을 했으므로 driection==-1경우 direction을 3으로 바꿔줌
  global direction
  direction-=1
  if direction==-1:
    direction=3

# 시뮬레이션 시작
count=1
turn_time=0

while True:
  #왼쪽으로 회전
  # 첫번째 조건 : 현재 방향을 기준으로 왼쪽 방향 부터! 이므로
  # 왼쪽으로 돌리는 연산 등장함
  turn_left()
  # x,y는 현재 위치 
  # x:1, y:1이면 내가 바라보는 블럭이 어딘지 알려면 dx, dy를 이용해서 index의 값을 이용해 바라보는 블럭의 값을 구해준다
  nx=x+dx[direction]
  ny=y+dy[direction]
  # 바라보는 블럭이 0 이거나(0:가보지 않은 곳, 1: 가본 곳) 그 위치가 육지면
  if d[nx][ny]==0 and array[nx][ny]==0:
    # 가본곳으로 체크하고 (0->1)
    d[nx][ny]=1
    # 현재 위치 갱신해준다음
    x=nx
    y=ny
    # 방문한 수 늘려주고
    count+=1
    # 몇번 돌았는지는 0으로 초기화
    turn_time=0
    continue
  #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    #한번 돌아준다
    turn_time+=1
  
  # 4번 돌았는데 갈수 있는 곳이 없으면
  # 바라보는 방향을 유지하고 한칸뒤로 간다
  if turn_time==4:
    nx=x-dx[direction]
    ny=y-dy[direction]
    #만약에 뒤로 이동한 칸이 육지라면
    if array[nx][ny]==0:
      #현재 위치 갱신하고
      x=nx
      y=ny
    # 뒤로 이동한 칸이 바다라면
    else:
    #끝낸다
      break
    # 4번 돌았을 때 처리해줬으므로 turn_time은 0으로 초기화
    turn_time=0

print(count)
