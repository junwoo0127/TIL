#계수정렬
#O(N+K) :기수 정렬과 더불어 가장 빠르다고 볼 수 있음
#데이터의 특성을 파악하기 어렵다면 퀵정렬 이용이 효율적

array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
#max():리스트 중에 가장 큰 값
count=[0]*(max(array)+1)

for i in range(len(array)):
  count[array[i]]+=1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')
