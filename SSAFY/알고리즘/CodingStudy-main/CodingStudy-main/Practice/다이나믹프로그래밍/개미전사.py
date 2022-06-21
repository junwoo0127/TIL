# 개미전사
# 다이나믹프로그래밍 사용 안하고 풀었음
# 어차피 개미전사가 식량창고 털때 최소 한칸 이상 떨어져야되니까
# 최대로 털라믄 좌우로 한칸씩 공백 제외하고 다 털어야하는데 두가지 그 경우가 밖에없음
# 0 x 0 x 이렇게 털거나 x 0 x 0 이렇게 털거나!
# 그래서 두가지 경우를 구해 값을 구하고 두가지 경우중 더 높은 값을 가진 것를 출력

n=int(input())
array=list(map(int,input().split()))

sum1=0
sum2=0

for i in range(n):
  if i%2==0:
    sum1+=array[i]
  else:
    sum2+=array[i]

print(max(sum1,sum2))

#책에서의 풀이
n=int(input())
array=list(map(int, input().split()))

d=[0]*100

d[0]=array[0]
d[1]=max(array[0],array[1])
# oxox일 때 oo를 합친값이 큰가
# x값이 큰가 판단해서 큰쪽으로 계속해서 연산
for i in range(2,n):
  d[i]=max(d[i-1],d[i-2]+array[i])

print(d[n-1])
