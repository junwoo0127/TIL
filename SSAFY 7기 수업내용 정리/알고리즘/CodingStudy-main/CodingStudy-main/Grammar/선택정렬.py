#선택정렬
array=[7,5,9,0,3,1,6,2,4,8]

#array의 원소 갯수만큼 반복하다
for i in range(len(array)):
  min_index=i
  # i보다 큰 범위에서 끝까지
  # 기준점(array[min_index])보다 작은 원소가 있다면
  # i번째 원소와 작은 원소의 위치를 바꿔준다
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index=j
  #스와프 : 특정 리스트가 주어졌을 때 변수의 위치를 변경하는 작업
  array[i], array[min_index]=array[min_index], array[i]

print(array)

#swap코드
array=[3,5]
array[0],array[1]=array[1],array[0]

print(array)

#시간복잡도 : 2중 반복문을 사용하므로 O(N^2)
