#재귀함수가 더욱 간결
def factorial_iterative(n):
  result=1
  for i in range(1,n+1):
    result*=i
  return result

def factorial_recursive(n):
  #if문을 사용해 종료 조건을 만들어 줍니다
  if n<=1:
    return 1
  return n*factorial_recursive(n-1)

print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))
