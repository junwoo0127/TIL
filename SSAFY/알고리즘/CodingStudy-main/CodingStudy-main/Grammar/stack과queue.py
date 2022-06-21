#스택 예제
stack=[]
#삽입
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
#최상단 원소부터 출력
print(stack[::-1])

#큐예제
from collections import deque

#큐 구현을 위해 deque 라이브러리 사용
queue=deque()

#선입선출
#First In First Out
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
print(list(queue)) #리스트로 변경
