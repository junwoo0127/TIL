#인접행렬

INF=999999999

#2차원 리스트를 이용한 인접 행렬
graph=[
  [0,7,5],
  [7,0,INF],
  [5,INF,0]
]

print(graph)

# 인접행렬2

graph=[[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))
print(graph)

#DFS 예제
def dfs(graph,v,visited):
  # 처음 v=1일때 visited리스트에 방문했다고 표시
  # for문에 돌아가면서 순서대로 방문할 수 있는 곳으로 노드 v가 결정된다
  visited[v]=True
  # 방문한곳은 출력해줍니다
  print(v, end=' ')
  # graph[v]에는 v노드 다음에 갈수 있는 노드들이 리스트에 담겨져 있다
  # graph[1]인 경우 [2,3,8]이 담겨 있는데 순서대로 방문하지 않은 곳만 재귀함수에 넣어 방문해 준다
  # for문이 끝났을 때는 재귀함수로 모든 경로가 print됨
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

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

#방문 했는지 안했는지 판단을 위한 리스트
# visited=[0,0,0,0,0,0,0,0]로 초기화
visited=[False]*9

#1번 노드부터 DFS에 따른 순서를 출력해 봅시당
dfs(graph,1,visited)
