#BFS 알고리즘
from collections import deque

def bfs(graph, start, visited):
  #queue 구현을 위해 deque 라이브러리를 사용한다
  queue=deque([start])
  #queue=[1] 먼저 들어감
  #방문했으니까 1번 노드는 방문 체크 해줌
  visited[start]=True

#queue가 비어있지 않을때 까지 돔
#queue가 비어지면 while문 밖으로 나감
  while queue:
    #v는 queue중 가장 먼저 들어온 값을 pop한 값
    v=queue.popleft()
    # v 출력, v가 queue에 가장 먼저 들어온 값이므로 모이면 경로가 됨
    print(v,end=' ')
    # v와 연결된 노드를 차례로 돔, queue에다가 연결된 노드 중 방문하지 않은 노드들의 값들이 차례로 들어감. 
    for i in graph[v]:
      # 방문하지 않은 노드라면 queue에다가 노드를 넣어줌
      if not visited[i]:
        queue.append(i)
        # 방문했으니까 방문 체크 해주기
        visited[i]=True

# graph[n]의 값은 n노드와 연결된 노드 번호들임
graph=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 일단 모드 방문 안함으로 초기화
visited=[False]*9

bfs(graph,1,visited)
