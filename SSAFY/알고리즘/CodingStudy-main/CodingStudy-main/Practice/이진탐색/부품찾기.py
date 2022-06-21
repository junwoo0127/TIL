#부품 찾기
#내가 작성한 코드 : 기존의 재귀함수를 이용한 이진탐색을 활용해 작성한 코드로 탐색하고자 하는 배열은 array1, 탐색의 target이 되는 배열은 array2로 잡고 for문을 돌리면서 array1에 array2의 원소들이 있는지 판단하는 코드를 작성 하였다.
n=int(input())
array1=list(map(int,input().split()))
array1.sort()
m=int(input())
array2=list(map(int,input().split()))
array2.sort()

def binary_search(array,target,start,end):
  if start>end:
    return None
  mid=(start+end)//2

  if array[mid]==target:
    return mid
  elif array[mid]>target:
    return binary_search(array,target,start,mid-1)
  else:
    return binary_search(array,target,mid+1,end)

for i in array2:
  result = binary_search(array1,i,0,n-1)
  if result==None:
    print("No", end=' ')
  else:
    print("yes", end=' ')

#책 풀이 방식
#이진탐색 version
def binary_search(array,target,start,end):
  #start=end가 되는 순간부터는 탐색을 해도 의미가 없기 때문에 탐색 종료
  while start<=end:
    mid=(start+end)//2
    #타겟이 기준과 같으면 타겟 반환
    if array[mid]==target:
      return mid
    #타겟이 기준보다 작으면 기준보다 왼쪽 범위에서 탐색
    elif array[mid]>target:
      end=mid-1
    #타겟이 기준보다 크면 기준보다 오른쪽 범위에서 탐색
    else:
      start=mid+1
  return None

#우선 정렬을 해야 탐색을 할 수 있음
n=int(input())
array=list(map(int,input().split()))
array.sort()
m=int(input())
x=list(map(int,input().split()))

#list x에 원소를 하나씩 탐색
for i in x:
  #array는 탐색해야하는 리스트
  #i가 array에 있는지 탐색
  #n은 array의 총 배열 크기
  result=binary_search(array,i,0,n-1)
  #탐색에 성공하면 yes출력, 실패하면 no 출력
  if result!=None:
    print('yes', end=' ')
  else:
    print('no',end=' ')

#집합 자료형 이용
n=int(input())
array=set(map(int,input().split()))
m=int(input())
x=list(map(int,input().split()))

for i in x:
  #집합 자료형이기에 해당 원소가 있는지 확인 가능
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ')
