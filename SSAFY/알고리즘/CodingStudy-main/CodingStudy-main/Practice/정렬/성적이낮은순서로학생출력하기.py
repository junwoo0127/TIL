#내가 푼 풀이 방식
#두번째 원소만 반환하는 함수를 이용하여 점수만 오름차순으로 정렬
# 책에서의 람다를 이용한 방식은 좀 더 코드가 간결하고 짧다는 장점이 있다.
n=int(input())
student_info=[]

for i in range(n):
  #튜플 형식으로 받아줍니다
  student_info.append(tuple(map(str,input().split())))

def setting(data):
  #두번째 점수 데이터만 반환하는 함수
  return data[1]

#점수를 오름차순으로 정렬
student_info.sort(key=setting)

#튜플에 든 첫번째 원소값만 print 해줌
for i in range(len(student_info)):
  print(student_info[i][0],end=' ')

#책에서의 풀이 방식
n=int(input())
array=[]
for i in range(n):
  input_data=input().split()
  #입력받은 값들을 쌍으로 하는 튜플로 list array에 넣어준다
  array.append((input_data[0],int(input_data[1])))
  
# lambda는 정렬되기 전에 호출되며 student의 원소를 받아서 student[1]을 반환한다
array=sorted(array,key=lambda student: student[1])

for student in array:
  print(student[0], end=' ')
