#sys 라이브러리
import sys
#한줄 입력 받고 rstrip()함수 꼭 호출, 엔터는 줄바꿈 기호로 입력되고 rstrip()을 통해서 공백 문자를 제거 할 수 있음. 
input_data=sys.stdin.readline().rstrip()

print(input_data)
