## Class 3 

> 1012 유기총 배추(BFS,DFS) https://www.youtube.com/watch?v=ansd5B27uJM

```python
dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    q = []
    q.append((a,b))
    graph[a][b] = 0

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))


for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
```

> BFS, DFS 최단경로 찾기

```python
def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)] # 미로의 크기만큼 생성
    queue = []              # 큐 생성
    queue.append((i, j))    # 시작점 인큐
    visited[i][j] = 1       # 시작점 방문표시
    while queue:            # 큐가 비어있지 않으면 반복
        i, j = queue.pop(0)     # t<-디큐
        if maze[i][j] == 3:   # visit(t) t에서 할 일 처리
            return 1            # 도착한 경우
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:  # i, j에 인접한 칸에 대해
            ni, nj = i+di, j+dj         # 주변 칸 좌표, 미로를 벗어나지 않고, 인접(벽이 아님)
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj] ==0:
                queue.append((ni,nj))   # 인큐
                visited[ni][nj] = visited[i][j] + 1
    return 0 # 도착지를 찾지 못한경우

def dfs(i, j, N):    # c 지나온 칸 수
    global ans
    if maze[i][j] == 3:   # 목적지에 도착하면 기존의 최소거리와 비교
        ans = 1
    else:
        maze[i][j] = 1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1:
                dfs(ni, nj, N)
    return

def dfs2(i, j, N):    # c 지나온 칸 수
    if maze[i][j] == 3:   # 목적지에 도착하면 기존의 최소거리와 비교
        return 1        # 찾으면 중단하는 경우
    else:
        maze[i][j] = 1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1:
                if dfs2(ni, nj, N):
                    return 1
        return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = fstart(N)

    # ans = bfs(sti, stj, N)
    # print(f'#{tc} {ans}')
    # ans = 0
    # dfs(sti, stj, N)
    # print(f'#{tc} {ans}')

    ans = dfs2(sti, stj, N)
    print(f'#{tc} {ans}')
```

> 1074 Z (분할정복, 재귀)

```python
# 분할정복
N, r, c = map(int, input().split())

ans = 0

while N != 0:

	N -= 1

	# 1사분면
	if r < 2 ** N and c < 2 ** N:
		ans += ( 2 ** N ) * ( 2 ** N ) * 0

	# 2사분면
	elif r < 2 ** N and c >= 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 1
		c -= ( 2 ** N )
        
	# 3사분면    
	elif r >= 2 ** N and c < 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 2
		r -= ( 2 ** N )
        
	# 4사분면    
	else:
		ans += ( 2 ** N ) * ( 2 ** N ) * 3
		r -= ( 2 ** N )
		c -= ( 2 ** N )
    
print(ans)

# 재귀
N, r, c = map(int, input().split())

def sol(N, r, c):

	if N == 0:
		return 0
        
	return 2*(r%2)+(c%2) + 4*sol(N-1, int(r/2), int(c/2))

print(sol(N, r, c))
```

> 1107 리모콘(브루트포스 알고리즘)

- 풀이: 

  **채널 N의 범위가 0<=N<=50,000이라고 했으므로 고장나지 않은 숫자중에 만들수 있는 모든 숫자를 살펴보면서 N과 가장 차이가 적은 번호를 찾으면 된다.**

   

  **이를 위해 버튼을 누를 수 있는 최대 번호를 100,0000으로 한다.**

   

  **1,000,000으로 하는 이유는\**누를 수 있는 번호가 500,000보다 클 수 있기때문에\** 500,000보다 크면서 모든 숫자를 다 거칠 수 있는 숫자이기 때문이다.**

   

  **따라서 1~1,000,000까지의 숫자를 반복문을 통해 살펴본다.**

   

  **각각의 숫자를 문자열로 변환후 문자열에 누를 수 없는 버튼이 있다면 다음 번호로 넘어간다.**

   

  **현재 살펴보고 있는 숫자에 누를 수 없는 버튼이 없다면 현재 숫자에서 N을 뺀 절댓값을 구한다.(채널입력후 목표채널로 가기위한 +,-의 크기)**

   

  **위에서 구한 절댓값에 누른번호의 길이(버튼 누른 횟수)를 더해야 최종적으로 버튼을 누른 횟수를 구할 수 있다.**

   

  **반복문을 통해 현재 살펴보고 있는 숫자와 100(현재 보고 있는 채널)을 뺀후 절댓값을 구해 위에서 구한값과 비교한다.->더 작은값 선택**

   

  **각각의 경우에서 위 과정을 반복해 최솟값이 나올때마다 그 값을 갱신해준다.**

```python
import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
break_num= list(map(int, input().split()))

# 현재 채널에서 +,-만 사용하여 이동하는 경우
min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        # 각 숫자의 버튼이 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in break_num:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))#(min_count,현재채널에서 목표채널로 가기위한 버튼 클릭 횟수)

print(min_count)
```

> 1389 케빈 베이컨의 6단계 법칙

```python
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph,start):
    num = [0] * (N+1)
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = 1
                num[i] = num[a] + 1
                q.append(i)
    return sum(num)

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
result = []
for i in range(1,N+1):
    visited = [0 for _ in range(N + 1)]
    result.append(bfs(graph, i))
print(result.index(min(result)) + 1)
```

> 1541 잃어버린 괄호(그리디 알고리즘)

![image-20220701184739623](Solved.ac%20Class%203.assets/image-20220701184739623.png)

![image-20220701184817093](Solved.ac%20Class%203.assets/image-20220701184817093.png)

![image-20220701184830561](Solved.ac%20Class%203.assets/image-20220701184830561.png)

```python
arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)
```

