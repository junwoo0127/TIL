#피보나치 함수 소스코드
#O(2^n)
#n이 커질 수록 수행 시간이 기하 급수적으로 늘어남
def fibo(x):
  if x==1 or x==2:
    return 1
  return fibo(x-1) + fibo(x-2)

print(fibo(4))

#메모이제이션을 사용한 피보나치 수열
#O(n)
d=[0]*100
def fibo(x):
  if x==1 or x==2:
    return 1
  if d[x] !=0:
    return d[x]
  d[x]=fibo(x-1)+fibo(x-2)
  return d[x]

print(fibo(99))

#탑다운 방식 : 재귀 함수를 이용해 다이나믹 프로그래밍 하는 방식(하향식)
#호출되는 함수 확인
d=[0] * 100
def pibo(x):
  print('f('+str(x)+')', end=' ')
  if x==1 or x==2:
    return 1
  if d[x]!=0:
    return d[x]
  d[x]=pibo(x-1)+pibo(x-2)
  return d[x]
pibo(99)

#바틈 업 방식 : for문을 이용해서 다이나믹 프로그래밍을 하는 방식(상향식)
d=[0]*100
d[1]=1
d[2]=1
n=99

for i in range(3, n+1):
  d[i]=d[i-1]+d[i-2]

print(d[n])
