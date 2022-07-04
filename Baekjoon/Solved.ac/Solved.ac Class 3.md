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

![image-20220702135059420](C:\Users\김준우\AppData\Roaming\Typora\typora-user-images\image-20220702135059420.png)

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

![image-20220702151714498](C:\Users\김준우\AppData\Roaming\Typora\typora-user-images\image-20220702151714498.png)

![image-20220702151552663](C:\Users\김준우\AppData\Roaming\Typora\typora-user-images\image-20220702151552663.png)

![image-20220702151639577](C:\Users\김준우\AppData\Roaming\Typora\typora-user-images\image-20220702151639577.png)



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

