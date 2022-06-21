#효율적인 화폐 구성
n,m=map(int,input().split())
array=[]
for i in range(n):
  array.append(int(input()))
  
d=[0]*30001
d[1]=1000000
#2부터 m까지 연산
for i in range(2,m+1):
  for j in array:
    #array 원소(화폐 종류)들을 모두 확인
    #총금액에서 해당화폐로 나눠져야 지급가능하므로
    # 나눠진다면 갯수를 저장하는 d 리스트에 총금액//화폐 = 화폐 개수와 이전 화폐의 총개수중에 최소값을 리스트에 저장
    if m%j==0:
      d[i]=min(m//j,d[i-1])
    else:
      continue

#위의 연산에서 배열에 저장된게 없으면 -1 출력
if d[m]==0:
  print(-1)
else:
  print(d[m])
