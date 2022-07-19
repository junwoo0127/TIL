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

> 1620 나는야 포켓몬 마스터 이다솜

```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
```

> 1676 팩토리얼0의 개수

```python
from math import factorial
n = int(input())
cnt = 0
for x in str(factorial(n))[::-1]:
    if x != '0':
        break
    cnt += 1
print(cnt)

# 팩토리얼 재귀 호출로 만들기

def factorial(n):
    if n == 1:  # n이 1일 때
        return 1  # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)  # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함


print(factorial(5))
```

> 1697 숨바꼭질 (BFS)

```python
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=MAX and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)
MAX = 10 ** 5
visited = [0] * (MAX + 1)
n,k = map(int, input().split())

bfs()

# 출처: https://wook-2124.tistory.com/273
```

> 1764 듣보잡(set)

![image-20220702014655522](Solved.ac%20Class%203.assets/image-20220702014655522.png)

![image-20220702014708980](Solved.ac%20Class%203.assets/image-20220702014708980.png)

![image-20220702014725679](Solved.ac%20Class%203.assets/image-20220702014725679.png)

```python
N, M = map(int,input().split())

a = set()
for i in range(N):
    a.add(input())

b= set()
for i in range(M):
    b.add(input())

result = sorted(list(a.intersection(b)))

print(len(result))

for i in result:
    print(i)
```

> 1780 종이의 개수(분할정복,재귀) https://dailymapins.tistory.com/m/270

![image-20220705213130111](Solved.ac%20Class%203.assets/image-20220705213130111.png)

```python
# 분할정복
# divide Conquer
import sys
sys.setrecursionlimit(10**6)
input= sys.stdin.readline

N=int(input().rstrip())

board=[list(map(int,input().split())) for _ in range(N)]
zero=0
one=0
minus_one=0
def solve(y,x,n):
    global zero,one,minus_one
    # 종이가 모두 같은 수로 이루어져 있는지 확인
    init=board[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if board[i][j] != init:
                # 같은 수로 이루어져 있지 않다면, 9 등분을 합시다.
                for k in range(3):
                    for l in range(3):
                        solve(y+k*n//3,x+l*n//3,n//3)
                # 같지 않기 때문에, 이 loop는 종료해줍니다. 불필요한 반복을 하지 않습니다.
                return
    if init==0:
        zero+=1
    elif init==1:
        one+=1
    elif init==-1:
        minus_one+=1
    return

solve(0,0,N)

print(minus_one)
print(zero)
print(one)
```

> 1927 최소 힙

![image-20220705213010694](Solved.ac%20Class%203.assets/image-20220705213010694.png)

![image-20220705213028138](Solved.ac%20Class%203.assets/image-20220705213028138.png)

```python
import sys
import heapq
input = sys.stdin.readline

min_heap = []

for _ in range(int(input())):
    n = int(input())
    
    if n == 0:
        if len(min_heap):
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, n)
```

> 2178 미로탐색(bfs)

```py
import sys
import collections
input = sys.stdin.readline
    
n, m = map(int, input().split())    
maze = [list(map(int, ' '.join(input()).split())) for _ in range(n)]

# 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q = collections.deque([(0, 0)])
result = 0

while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 1:
                # 방문
                maze[nx][ny] = maze[x][y] + 1
                Q.append((nx, ny))

print(maze[n - 1][m - 1])
```

> 1992 쿼드트리(분할정복)

```python
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

def dfs(x,y,n):
    check = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != arr[i][j]:
                chec k = -1
                break
    if check == -1:
        print("(", end="")
        n = n // 2
        dfs(x,y,n)
        dfs(x,y+n,n)
        dfs(x+n,y,n)
        dfs(x+n,y+n,n)
        print(")",end="")
    elif check == 1:
        print(1, end="")
    else:
        print(0, end="")
dfs(0,0,n)

```

> 2579 계단 오르기(DP)

![image-20220704191256258](Solved.ac%20Class%203.assets/image-20220704191256258.png)

![image-20220704191239520](Solved.ac%20Class%203.assets/image-20220704191239520.png)

```python
import sys
input = sys.stdin.readline
arr = []
dp = []

l = int(input())
for _ in range(l):
    arr.append(int(input()))

dp.append(arr[0])
dp.append(max(arr[0]+arr[1],arr[1]))
dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))
for i in range(3,l):
    dp.append(max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1]))

print(dp.pop())
```

> 2606 바이러스(DFS)

```python
n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(n+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
 
dfs(1)
print(cnt)
```

> 2630 색종이 만들기(분할정복)

![KakaoTalk_20220705_172347873](Solved.ac%20Class%203.assets/KakaoTalk_20220705_172347873.png)

```python
import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

def solution(x, y, N) :
  color = paper[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j] :
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))
```

> 7576 토마토(bfs)

```python
# bfs 특 queue 사용하기
# deque 모듈 안쓰면 시간복잡도 박살남(pop(0)이 시간복잡도가 O(n)이고 popleft()가 O(1)이라고 함)
from collections import deque

m, n = map(int, input().split())
# 토마토 받아서 넣기. 이차원 리스트로 만들어질거.
matrix = [list(map(int, input().split())) for _ in range(n)]
# 좌표를 넣을거니까 []를 넣자.
queue = deque([])
# 방향 리스트. [dx[0], dy[0]]은 곧 [-1, 0]이고 이는 왼쪽으로 이동하는 위치이다.
# 그려보면 이해하기 편함
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# 정답이 담길 변수
res = 0

# queue에 처음에 받은 토마토의 위치 좌표를 append 시킨다
# n과 m을 사용하는걸 헷갈리지 말아야 함!
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

# bfs 함수. 한번 들어가면 다 돌고 나오니까 재귀 할 필요 없음
def bfs():
    while queue:
        # 처음 토마토 좌표 x, y에 꺼내고
        x, y = queue.popleft()
        # 처음 토마토 사분면의 익힐 토마토들을 찾아본다.
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            # 해당 좌표가 좌표 크기를 넘어가면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야 함(0).
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                # 익히고 1을 더해주면서 횟수를 세어주기
                # 여기서 나온 제일 큰 값이 정답이 될 것임
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    res = max(res, max(i))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(res - 1)
```

> 7662 이중 우선순위 큐

```python
import heapq

t = int(input())

for i in range(t):
    k = int(input())
    q1, q2 = [], []
    visited = [False] * k

    for j in range(k):
        com, num = input().split()

        if com == 'I':
            heapq.heappush(q1, (int(num), j))
            heapq.heappush(q2, (-int(num), j))
            visited[j] = True

        else:
            if num == '1':
                while q2 and not visited[q2[0][1]]:
                    heapq.heappop(q2)
                if q2:
                    visited[q2[0][1]] = False
                    heapq.heappop(q2)
            else:
                while q1 and not visited[q1[0][1]]:
                    heapq.heappop(q1)
                if q1:
                    visited[q1[0][1]] = False
                    heapq.heappop(q1)

    while q1 and not visited[q1[0][1]]:
        heapq.heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heapq.heappop(q2)

    if not q1 or not q2:
        print("EMPTY")
    else:
        a = -q2[0][0]
        b = q1[0][0]
        print("%d %d" % (a, b))
```

> 9095 1,2,3 더하기(DP프로그래밍)

![image-20220708113921160](Solved.ac%20Class%203.assets/image-20220708113921160.png)

```python
T = int(input())

def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n==3:
        return 4
    else:
        return sol(n-1) + sol(n-2) + sol(n-3)
    
for i in range(T) :
    n = int(input())
    print(sol(n))
```

> 11279 최대 힙

```python
import sys
import heapq

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
  m = int(sys.stdin.readline())
  if m == 0:
    if len(heap) == 0:
      print(0)
    else:
      print((-1)*heapq.heappop(heap))
  else:
    heapq.heappush(heap, (-1)*m)
```

> 11399 ATM(그리디)

```python
n = int(input())
s = list(map(int, input().split()))
num = 0
s.sort()
for i in range(n):
    for j in range(i + 1):
        num += s[j]
print(num)
```

> 11723 집합

```python
import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
```

> 11724 연결요소의 개수(그래프 이론, BFS)

```python
import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline


# dfs로 그래프를 탐색한다.
def dfs(start, depth):

    #해당 노드 방문체크 한다.
    visited[start] = True

    # 해당 시작점을 기준으로 계속해서 dfs로 그래프를탐색한다.
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]:  # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1  # 개수를 + 1
            visited[i] = True  # 방문 처리
        else:  # 연결된 그래프가 있다면
            dfs(i, 0)  # dfs탐색을 돈다.
            count += 1  # 개수를 +1

print(count)
```

> 11726 2*N(DP)

![image-20220712214944845](Solved.ac%20Class%203.assets/image-20220712214944845.png)

```python
s = [0, 1, 2]
for i in range(3, 1001):
  s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n] % 10007)
```

> 18870 좌표압축(정렬)

```python
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')
```

> 5430 AC(덱)

```python
import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if n == 0:
        arr = deque()

    flag = 0
    for j in p:
        if j == 'R':
            arr.reverse()
        elif j == 'D':
            if arr:
                arr.popleft()
            else:
                print("error")
                flag = 1
                break
    if flag == 0:
        print("["+",".join(arr)+"]")
```

> 7569 토마토(BFS 삼방향)

```python
import sys
from collections import deque
m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque([])
 
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)
    
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while(queue):
    x,y,z = queue.popleft()
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1
            
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)
```

> 9019 DSLR(BFS)

```python
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A,B = map(int,input().split())
    q = deque()
    q.append((A,""))
    visit = [False] * 10000
    
    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == B:
            print(path)
            break
        
        # 1
        num2 = (2*num)%10000
        if not visit[num2]:
            q.append((num2,path+"D"))
            visit[num2] = True
        # 2
        num2 = (num-1)%10000
        if not visit[num2]:
            q.append((num2,path+"S"))
            visit[num2] = True
        # 3
        num2 = (10*num+(num//1000))%10000
        if not visit[num2]:
            q.append((num2,path+"L"))
            visit[num2] = True
            
        # 4
        num2 = (num//10+(num%10)*1000)%10000
        if not visit[num2]:
            q.append((num2,path+"R"))
            visit[num2] = True
```

> 5525 IOIOI

```python
N = int(input())
M = int(input())
S = input()
answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)
```

> 6064 카잉 달력

```python
def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))
```

> 9375 패션왕 신해빈()

```py
# Counter 함수
from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    wear = []
    for j in range(n):
        a, b = input().split()
        wear.append(b)

    wear_Counter = Counter(wear)
    cnt = 1 # 각 종류마다 항목의 개수

    for key in wear_Counter:
        cnt *= wear_Counter[key] + 1

    print(cnt-1)
# 그냥
t = int(input())

for i in range(t):
    n = int(input())
    weardict = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]

    cnt = 1 # 각 종류마다 항목의 개수

    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)
```

> 9461 파도반 수열(DP)

```python
wh = [0 for i in range(101)]
wh[1] = 1
wh[2] = 1
wh[3] = 1
for i in range(0, 98):
    wh[i + 3] = wh[i] + wh[i + 1]
t = int(input())
for i in range(t):
    n = int(input())
    print(wh[n])
```

> 10026 적록색약(BFS,DFS)

```python
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == a[x][y] and c[nx][ny] == 0:
                    q.append([nx, ny])
                    c[nx][ny] = 1

n = int(input())
a = [list(map(str, input())) for _ in range(n)]
c = [[0]*n for _ in range(n)]
q = deque()

cnt = 0
for i in range(n):
    for j in range(n):
        if c[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if a[i][j] == 'R':
            a[i][j] = 'G'
c = [[0]*n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if c[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)
```

> 11047 동전 0(그리디 알고리즘)

```python
N, K = map(int, input().split()) 
coin_lst = list()
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K//coin_lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K%coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복

print(count)
```

> 11286 절댓값 힙(우선순위 큐)

```python
import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
```

> 11403 경로 찾기(플로이드-위셜)

```python
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
    
#플로이드-워셜 알고리즘
for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N): 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1


#출력
for row in graph:
    for col in row:
        print(col, end = " ")
    print()
```

> 11659 구간 합 구하기4

```python
import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]    # init prefix_sum    
 
temp = 0    
for i in arr:    # accumulate arr section 
    temp += i
    prefix_sum.append(temp)
 
for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])

```

> 11727 2*N 타일링 2

```python
s = [0, 1, 3]
for i in range(3, 1001):
  s.append((s[i - 2] * 2) + s[i - 1])
n = int(input())
print(s[n] % 10007)
```

