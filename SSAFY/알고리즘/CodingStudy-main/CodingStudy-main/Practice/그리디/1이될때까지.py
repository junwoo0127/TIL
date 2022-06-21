# 1이 될때 까지
# 나의 방법 장단점
# 장점 : 책 풀이 두번째 방식을 보다 가독성 있게(사람들이 이해 하기 쉽게) 표현한 것이 장점인 것 같다.

n,k=map(int,input().split()) #n,k를 입력 받음 
count=0
while n!=1: #n이 1이면 탈출
  if n%k==0: #n이 k로 나누어 질 경우
    count+=1 # 카운트를 세주고
    n=n//k # 몫을 n에 저장한다
  else: # n이 k로 나눠지지 않을 경우
    n-=1 #n에서 1을 빼줌
    count+=1 # 카운트를 세주고
# n=1이 되면
# 총 카운트 출력
print(count)

# 책의 풀이 방법1 : 2중 whilw문
n,k=map(int,input().split())
result=0

# n이 k 보다 같거나 큰 경우 : 나눠지면 몫을 할당하고 나눠지지 않으면 1을 빼주면서 카운트
while n>=k: # n이 k보다 작을 경우 while문 탈출
  while n%k!=0: # n을 k로 나눴을 때 나머지가 0이면 탈출
    n-=1 # 나머지가 0이 아닌 경우 1을 빼줌
    result+=1 # 카운트를 하나 세어 주고
  n//=k # 나머지가 0이면 몫을 n값에 넣어주고
  result+=1 # 카운트를 세어 준다

# n이 k보다 작은 경우 : n=1 될때 까지 카운트 해줌
while n>1: # n이 1보다 같거나 작으면 while문 탈출
  n-=1 # n에 1을 빼주고
  result+=1 # 카운트를 세어 준다

print(result)

# 책의 풀이 방법2 : while문과 if문 활용
n, k = map(int, input().split())
result=0;

while True: 
  target=(n//k)*k #k로 나누어 떨어지는 수
  result += (n-target) # 1을 빼는 연산 횟수
  n=target 

  if n<k:
    break
  result+=1 #한번 수행하므로 1을 더해줌
  n//=k

  result += (n-1) #남은 수에 대해서 1씩 빼줌
  print(result)
