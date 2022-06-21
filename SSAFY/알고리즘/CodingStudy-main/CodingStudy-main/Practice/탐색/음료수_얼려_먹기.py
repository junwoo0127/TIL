# 음료수 얼려 먹기
# 못푼 문제
# 해당 문제를 풀기 위해서는 재귀함수를 이용해 탐색을 해야한다. 아직 탐색이 안된 곳의 방문 체크를 한후 주위의 구멍들을 찾아내고 끝에는 true를 반환하여 구멍 덩어리가 몇개인지를 카운트 할 수 있게 한다.

#n행 m열 받음
n,m=map(int, input().split())
graph=[]
#graph 받음 1:칸막이 0:구멍
for i in range(n):
  graph.append(list(map(int,input())))

#재귀함수 dfs 정의
def dfs(x,y):
  #범위에 벗어나면 False 반환
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  # 해당 원소가 구멍인 경우
  if graph[x][y]==0:
    #방문 처리
    graph[x][y]=1
    # 상하좌우로 구멍인지 아닌지 체크
    # 탐색을 하며 주변의 구멍인부분은 0->1로 모두 바꿔주고
    # 탐색을 끝낸다음 True를 반환해줌
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

#결과 초기값 0
result=0
for i in range(n):
  for j in range(m):
    # n이 5 m이 4일때
    # (0,0)>(0,1)>(0,2)>(0,3)>(0,4)
    #> (1,0)>(1,1)>(1,2)>(1,3)>(1,4) ... (5,4) 까지
    # 해당 좌표를 넣었을때 True가 반환되면
    # 카운트를 올려줌
    # 모든 좌표를 조사하면서 혹시 탐색이 안된 구멍 덩어리(0)들을 찾음
    if dfs(i,j)==True:
      result+=1
print(result)
