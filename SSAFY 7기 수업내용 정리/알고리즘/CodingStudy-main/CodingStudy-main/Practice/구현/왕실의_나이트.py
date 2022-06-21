#왕실의 나이트
# 나의 방법 장단점 : 책에서의 해답이 튜플을 사용해서 좀더 코드의 가독성이 좋은 것 같다. 내 코드는 리스트 안에 때려 넣어서 조합을 일일이 확인해봐야하는데 튜플 형태로 들어간 것이 한눈에 보기 쉽다. 

#a2를 입력 시 a,2가 리스트에 들어감
data=input()
row=int(data[1])
# 부호를 10진수로 바꾸면 a는 97이다.
# 따라서 연산을 수월하게 하기 위해
# 96를 빼줘서 a->1, b->2, c->3의 형태로 바꾼다.
column=int(ord(data[0]))-96

count=0
#dx[i]와 dy[i]를 조합해서 움직일 수 있는 방향을 모두 정의한다.
#move_types=[LD,LU,RU,RD,UR,UL,DR,DL]
dx=[-2,-2,2,2,+1,-1,+1,-1]
dy=[+1,-1,-1,+1,-2,-2,+2,+2]

# 총 8번 연산해야 하므로 범위는 8
# 연산을 진행 하는 과정에서 그 결과 값이 기준에 부합하지 않는 경우는 다음 연산을 진행한다.
# 부합하는 연산들은 카운터를 세어 준다.

for i in range(8):
  x=row+dx[i]
  y=column+dy[i]
  if x<1 or x>8 or y<1 or y>8:
    continue
  count+=1
print(count)

#책 솔루션
input_data=input()
row=int(data[1])
column = int(ord(input_data[0])-int(ord('a')))+1
#ord() : 문자열을 아스키 코드로 변환하는 함수
#chr() : 아스키코드를 문자열로 변환하는 함수
#리스트 안에 튜플을 이용해서 방향 정의
steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0
for step in steps:
  #튜플도 리스트와 마찬가지로 []로 접근 가능함!
  next_row=row+step[0]
  next_column=column+step[1]
  if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
    result+=1
print(result)
