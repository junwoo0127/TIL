#재귀함수
#자기자신을 다시 호출하는 함수
#종료 조건을 명시하여야 함수의 무한 호출을 막을 수 있다.

def recursive_function(i):
  #i가 100이면 함수를 호출하지 않고 종료
  if i==100:
    return

  print(i, '번째 재귀함수에서', i+1,'번째 재귀 함수를 호출합니다.')
  recursive_function(i+1) 
  #recursive_funciton(100)일때 함수를 나옴. 
  #recursive_function(99)에서 recursive_function(100)을 호출 했으므로 다음 명령('99번째 재귀 함수를 종료합니다') 실행
  #역시 recursive_function(98)에서 recursive_function(99)를 호출했으므로 '98번째 재귀 함수를 종료합니다' 실행
  # 그렇게 반복적으로 최종 i=1일때 까지 실행시켜줌
  
  print(i,'번째 재귀 함수를 종료합니다.')

recursive_function(1)
