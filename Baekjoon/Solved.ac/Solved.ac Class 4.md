## Class 4

> 1043 거짓말

```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
knowList = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & knowList:
            knowList = knowList.union(party)

cnt = 0
for party in parties:
    if party & knowList:
        continue
    cnt += 1

print(cnt)
```

> 1149 RGB 거리(DP)

```python
n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))
```

> 1167 트리의 지름

```python
from sys import stdin
from collections import deque

read = stdin.readline
V = int(read())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, read().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))


def bfs(start):
    visit = [-1] * (V + 1)
    que = deque()
    que.append(start)
    visit[start] = 0
    _max = [0, 0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                que.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e

    return _max


dis, node = bfs(1)
dis, node = bfs(node)
print(dis)
```

> 1238 파티(다익스트라)

```python
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e, x = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def dijkstra(start):
    q = []
    distance = [INF] * (v + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


result = 0
for i in range(1, v + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)
```

> 1504 특정한 최단 경로(다익스트라)

```python
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n, e = map(int, input().split())
s = [[] for i in range(n + 1)]
inf = sys.maxsize
for i in range(e):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])
v1, v2 = map(int, input().split())
def dijkstra(start):
    dp = [inf for i in range(n + 1)]
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        w, c = heappop(heap)
        for n_n, n_w in s[c]:
            wei = n_w + w
            if dp[n_n] > wei:
                dp[n_n] = wei
                heappush(heap, [wei, n_n])
    return dp
one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
cnt = min(one[v1] + v1_[v2] + v2_[n], one[v2] + v2_[v1] + v1_[n])
print(cnt if cnt < inf else -1)
```

> 1629 곱셈

```python
import sys
a,b,c = map(int,sys.stdin.readline().split())

def multi (a,n):
  if n == 1:
      return a%c
  else:
      tmp = multi(a,n//2)
      if n %2 ==0:
          return (tmp * tmp) % c
      else:
          return (tmp  * tmp *a) %c
          
print(multi(a,b))
```

> 1753 최단경로(다익스트라)

```python
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
#시작점 K
K = int(input())
#가중치 테이블 dp
dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]

def Dijkstra(start):
    #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    dp[start] = 0
    heapq.heappush(heap,(0, start))

    #힙에 원소가 없을 때 까지 반복.
    while heap:
        wei, now = heapq.heappop(heap)

        #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            #현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
            # = 다음 노드까지의 가중치(next_wei)
            next_wei = w + wei
            #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
            if next_wei < dp[next_node]:
                #계산했던 next_wei를 가중치 테이블에 업데이트.
                dp[next_node] = next_wei
                #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
                heapq.heappush(heap,(next_wei,next_node))

#초기화
for _ in range(E):
    u, v, w = map(int, input().split())
    #(가중치, 목적지 노드) 형태로 저장
    graph[u].append((w, v))


Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])
```

> 1865 웜홀(벨만-포드)

```python
import sys
input = sys.stdin.readline

def bf(start):
    dist[start] = 0
    for i in range(1, n+1):
        for s in range(1, n+1):
            for next, time in graph[s]:
                if dist[next] > dist[s] + time:
                    dist[next] = dist[s] + time
                    if i == n: #n번 이후에도 값이 갱신되면 음수 사이클 존재.
                        return True
    return False

TC = int(input())
for i in range(TC):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dist = [10001 for _ in range(n+1)]
    for j in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for k in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])

    negative_cycle = bf(1)
    if not negative_cycle:
        print("NO")
    else:
        print("YES")
```

> 1916 최소비용 구하기(데이크스트라)

```python
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
m = int(input())
inf = 100000000
s = [[] for i in range(n + 1)]
dp = [inf for i in range(n + 1)]
for i in range(m):
    a, b, w = map(int, input().split())
    s[a].append([b, w])
start, end = map(int, input().split())
def dijkstra(start):
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        if dp[n] < w:
            continue
        for n_n, wei in s[n]:
            n_w = w + wei
            if dp[n_n] > n_w:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
dijkstra(start)
print(dp[end])
```

> 1918 후위표기식(Stack)

```python
a = input()
stack = [] #스택
res='' #출력

for x in a:
    if x.isalpha(): #피연산자인지 아닌지 확인
        res+=x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x =='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res+=stack.pop()
            stack.pop()

#스택안에 남아있는 값들 pop            
while stack:
    res += stack.pop()
print(res)
```

