from collections import deque
#입력 부분
m,n=map(int, input().split())
map=[list(map(int,input().split())) for _ in range(n)]
#bfs를 위한 방향 정의
dx=[-1,1,0,0]
dy=[0,0,-1,1]
#result값
res=0
#bfs구현을 위한 queue정의
queue=deque([])

#익은 토마토는 queue에 넣어줌
#익은 토마토를 시작점으로 상하좌우로 탐색을 해야하기 때문
for i in range(n):
  for j in range(m):
    if map[i][j]==1:
      queue.append([i,j])

# queue에 든것이 없을 때 까지
# 가장 먼저 들어간 값을 pop해주고
# 그 근처 상하좌우의 값들이 map에 벗어나지 않으면서 익지 않은 토마토면
# 이동 전 좌표의 값에서 1 더해준 값을 이동 후 값에 할당
# 이동한 좌표를 queue에 넣어주며 계속 탐색

def bfs():
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<=n-1 and 0<=ny<=m-1 and map[nx][ny]==0:
        map[nx][ny]=map[x][y]+1
        queue.append([nx,ny])

bfs()

# 2차원 map을 탐색하며 익지 않은 토마토가 있을 시 -1 출력후 프로그램 종료
# 익지 않은 토마토가 없을 시 리스트의 값들 중 가장 최대 값 찾아줌
# max로 2차원 리스트안의 1차원 리스트의 값중 가장 큰 값을 n번 돌면서 계속해서 비교해 줌
for i in map:
  for j in i:
    if j==0:
      print(-1)
      exit(0)
  res=max(res,max(i))

# 처음 익은 토마토 1에서 부터 값이 커진 것이므로 몇일 후인지는 res값에서 1을 빼준 값임
print(res-1)
