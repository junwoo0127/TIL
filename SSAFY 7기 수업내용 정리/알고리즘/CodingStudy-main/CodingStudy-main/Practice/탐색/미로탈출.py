# 미로탈출

#책에서의 방법
#queue를 이용해서 풀기 때문에 라이브러리 임포트
from collections import deque
# n행 m열의 배열의 리스트를 받음
n,m=map(int,input().split())
graph=[]
# n번씩 m개로 구성된 리스트를 받음
for i in range(n):
  graph.append(list(map(int,input())))

# 상, 하, 좌, 우 방향 결정 리스트
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 너비 우선 탐색 알고리즘 사용 > 최단 거리를 구하기에 적합
def bfs(x,y):
  queue=deque()
  #탐색 시작점인 (x,y)를 queue에 넣어줌
  queue.append((x,y))
  print('queue: ',queue)
  #queue의 원소가 없어질때 까지 반복
  while queue:
    # 가장 먼저 이동 가능한 좌표를 x,y에 할당
    x,y=queue.popleft()
    print('x',x,'y',y)
    # if문으로는 갈수 있는지 없는지에 관해 체크하고 for문을 이용해 상하좌우별로 체크
    for i in range(4):
      #nx, ny는 기준점 기준 상,하,좌,우 좌표임
      nx=x+dx[i]
      ny=y+dy[i]
      #만약에 기준점 기준 상,하,좌,우 어딘가가 미로의 범위를 초과하는 경우에는 다음 방향으로 전환 해줌 (ex)상->하)
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      #만약에 기준점 기준 상,하,좌,우 좌표에 몬스터가 있다해도 다음 방향으로 전환해줌
      if graph[nx][ny]==0:
        continue
      # 만약에 기준점 기준 상,하,좌,우 좌표에 갈 수 있는 길이 있다면
      # 해당 좌표에다가 이동하기 이전 x,y의 좌표값 더하기 1을 더해줌 (ex. 1->2)
      # 그리고 queue에다가 순서대로 가능좌표를 넣어줌
      if graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))
  return graph[n-1][m-1]

print(bfs(0,0))

# #상하좌우에 대해서 상,좌 부분을 넣으면 다시 루트를 되돌아가는 문제 발생
# 추후 손볼 예정
# #나의 방법
# n,m=map(int,input().split())
# # 입력리스트 Map을 선언해 줍니다
# Map=[]

# # Map 입력을 받습니다
# for i in range(n):
#   Map.append(list(map(int,input())))

# # 카운트를 0으로 초기화 해줍니다
# count=0

# #퍼즐 함수에서 재귀 함수를 이용해 나가는 최단거리를 체크할 것입니다
# def Puzzle(x,y):
#   #count를 함수안에서 사용하려면 global로 다시 선언해줍니다
#   global count

#   #범위를 초과하는 것들은 False를 return하게 끔 해줍니다
#   if x<0 or x>n-1 or y<0 or y>m-1:
#     return False
#   #맵에서는 0이면 괴물이 있고 1이면 괴물이 없습니다.
#   #우리는 괴물이 없는 곳으로 가야하기 때문에 1인경우를 방문해야 합니다
#   #또한 방문한 곳을 다시 방문해서는 안되기 때문에 1을 방문한 경우 0으로 세팅해 갈수 없게끔 합니다

#   if Map[x][y]==1 :  
#     Map[x][y]=0
#     count+=1
#     print(x,y)
#     #여기서 미로를 풀때 내가 있는 칸으로 '우'와 '아래'의 경우로만 재귀함수를 넣습니다
#     # 왜냐하면 시작점에서 되돌아가지 않으려면 우와 아래를 기준으로 탐색해야 하기 때문입니다.
#     Puzzle(x+1,y)
#     Puzzle(x,y+1)
#     #탐색이 끝나면 True를 반환하여 함수를 끝냅니다
#     return True
#   #괴물이 있는 곳이면 False를 반환하여 이전의 위치(함수)로 돌아갑니다
#   return False

# #문제에서는 1,1이 시작점이지만 0,0을 기준으로 문제를 풀이했기 때문에 0,0을 함수에 넣어줍니다
# Puzzle(0,0)
# #움직인 총 블럭을 출력합니다
# print(count)
