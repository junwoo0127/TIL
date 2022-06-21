# 떡볶이 떡 만들기
# 내가 푼 방식
# 내가 푼 방식은 함수를 이용해 나머지 떡의 길이 합을 구해 조건을 만족하면 h를 리턴해주는 방식을 사용했고 책의 경우는 이진탐색을 활용해 범위를 좁혀나가는 방식으로 해결했다. 
# 나의 경우는 처음에 배열을 내림차순으로 정렬해서 가장 큰 떡의 길이에서 부터 h의 범위를 제한해주므로 연산횟수를 줄일 수 있고 책의 방식은 이진 탐색으로 점차 연산횟수가 줄어드는 장점을 가진다.
# h기준으로 큰값, 작은 값을 판별하는 함수필요
# 절단기 h값보다 큰값은 큰값-h를 해서 잘려진 값을 리턴
# 절단기 h보다 작은 값은 잘려지지 않으므로 0 리턴
def search(target,h):
  if target<=h:
    return 0
  else:
    return target-h

# 최대 h를 구하는 함수
# h가 될수 있는 가장 큰 값인 입력받은 값 중 가장 큰 값부터 0까지 for문을 돌면서 탐색
# h가 어떤 값일 때 입력받은 array 원소들을 search함수에 각각 넣어보며 합계를 구함. 합계가 조건에 만족하면 h값을 return하여 최대로 될수 있는 값을 구할 수 있음. 
def binary_search(array,m):
  global sum
  
  global h
  
  for h in range(array[0],-1,-1):
    sum=0
    for i in array:
      sum=sum+search(i,h)
    if sum>=m:
      return h
    else:
      continue
  
n,m=map(int,input().split())
array=list(map(int,input().split()))
array.sort(reverse=True)

result = binary_search(array,m)

print(h)

#책에서 푼 방식
n,m=list(map(int,input().split(' ')))
array=list(map(int,input().split()))

start=0
end=max(array)

result=0
while(start<=end):
  total=0
  mid=(start+end)//2
  for x in array:
    if x>mid:
      total+=x-mid
  if total<m:
    end=mid-1
  else:
    result=mid
    start=mid+1
    print(result,start)
print(result)
