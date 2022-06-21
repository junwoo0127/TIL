# 원소가 n 개인 list 입력 받기
n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# n,m,k를 공백을 구분해 입력 받기
n, m, k=map(int,input().split())

print(n, m, k)

# sys 라이브러리를 사용하여 속도가 빠른 입력
import sys
data = sys.stdin.readline().rstrip()
print(data)

# 같은 줄에 변수 출력하기
a=1
b=2
print(a,b)

# 줄바꿔서 변수 출력하기
a=1
b=2
print(a)
print(b)

# 변수를 출력할 경우 문자열로 바꿔줘야 함! 
answer=7
print("정답은" +str(answer))
print("정답은", str(answer), "입니다") #변수 좌우로 공백 출력됨

#f-string 사용한 출력 방법
print(f"정답은 {answer}입니다")
